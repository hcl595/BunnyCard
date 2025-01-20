from shutil import copytree, copy2
# from model import calculate_file_hash
import hashlib
import os
import threading
import time
from tkinter import Tk, Button, Image, filedialog, Entry, messagebox, ttk
# from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import ProcessPoolExecutor

gui = Tk()
# pool = ThreadPoolExecutor()


global srcHash, dstHash, srcFiles, dstFiles
srcHash = []
dstHash = []
srcFiles = []
dstFiles = []
d = 0

def calculate_file_hash(file_path, hash_algorithm='sha256', chunk_size=8192):
    """
    计算文件的哈希值。
    :param file_path: 文件路径
    :param hash_algorithm: 哈希算法（默认为sha256）
    :param chunk_size: 读取文件时的块大小（默认为8192字节）
    :return: 文件的哈希值
    """
    print(file_path)
    hash_obj = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()

def get_files(srcDir, dstDir):
    for filepath,dirnames,filenames in os.walk(r''+srcDir):
        for filename in filenames:
            srcFiles.append(os.path.join(filepath,filename))

    for filepath,dirnames,filenames in os.walk(r''+dstDir):
        for filename in filenames:
            dstFiles.append(os.path.join(filepath,filename))




# def openFloder(inputplace):
#     folder_path = filedialog.askdirectory() # 打开文件
#     inputplace.delete(0)  # 清空
#     inputplace.insert(0,folder_path)  #写入路径

def openSrcFloder():
    folder_path = filedialog.askdirectory() # 打开文件
    srcDir.delete(0,"end")  # 清空
    srcDir.insert(0,folder_path)  #写入路径

def openDstFloder():
    folder_path = filedialog.askdirectory() # 打开文件
    dstDir.delete(0,"end")  # 清空
    dstDir.insert(0,folder_path)  #写入路径
    

def get_dir_size(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size

def copying(src_dir, dst_dir):
    threading.Thread(target=copytree, args=(src_dir, dst_dir,False,None,copy2,False,True)).start()
    
def __update_progress(dst_dir, src_dir):
    pb["value"] = get_dir_size(dst_dir)
    print(get_dir_size(dst_dir))
    print(get_dir_size(src_dir))
    if pb["value"] >= pb["maximum"]:
        gui.after_cancel(__update_progress)
        pb["maximum"] = 100
        pb["value"] = 0
        get_files(src_dir, dst_dir)
        gui.after(100, __checkHarsh, dst_dir, src_dir, d)
    else:
        gui.after(100, __update_progress, dst_dir, src_dir)

def __checkHarsh(dst_dir, src_dir, d):
    pb["maximum"] = len(dstFiles)
    pb["value"] = d
    if d  < len(dstFiles):
        if (calculate_file_hash(srcFiles[d])) != (calculate_file_hash(dstFiles[d])): 
            # if the hash of the source and destination directories are not the same
            messagebox.showerror(message="The directories("+ srcFiles[d-1] +","+ dstFiles[d-1] +") are not the same,please try again")
            # raise Exception("The directories are not the same,please try again")
        d = d + 1
        gui.after(100, __checkHarsh, dst_dir, src_dir, d)
    else:
        messagebox.showinfo(message="Copy Completed")
        d = 0
        gui.after_cancel(__checkHarsh)

def copyCard(src_dir, dst_dir):
    if src_dir == dst_dir:
        messagebox.showerror(message="The source and destination directories are the same")
    elif not src_dir:
        messagebox.showerror(message="Please enter the source directory")
    elif not dst_dir:
        messagebox.showerror(message="Please enter the destination directory")
    elif not os.path.exists(src_dir):
        messagebox.showerror(message="The source directory does not exist")
    else:
        copying(src_dir, dst_dir)
        pb["maximum"] = get_dir_size(src_dir)
        gui.after(100, __update_progress, dst_dir, src_dir)

            

gui.title("Bunny copycard")
gui.geometry("300x200")


pb = ttk.Progressbar(length=200, mode="determinate")
pb.grid(row=5, column=2,)
pb["maximum"] = 100
pb["value"] = 0


# Label(gui,text="请输入文件路径：")
srcDir = Entry(gui,text="输入文件")
srcDir.grid(row = 1,column = 2)
btn = Button(gui,text="选择",command=openSrcFloder)
btn.grid(row = 1,column = 1)

# Label(gui,text="请输入文件路径：")
dstDir = Entry(gui,text="输出文件")
dstDir.grid(row = 2,column = 2)
btn = Button(gui,text="选择",command=openDstFloder)
btn.grid(row = 2,column = 1)
# dst_dir = filedialog.askdirectory()

Button(gui,text="确定",command=lambda:copyCard(srcDir.get(),dstDir.get())).grid(row = 3,column = 2)
Button(gui,text="取消").grid(row = 3,column = 1)


gui.mainloop()



