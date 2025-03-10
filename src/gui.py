
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


from shutil import copytree, copy2
import hashlib
import os
import threading
import time
from tkinter import Tk, Button, Image, filedialog, Entry, messagebox, ttk, Label, Frame

global srcFileNames, dstFileNames, srcFiles, dstFiles, d, pbp, pbi, hbp, hbi
srcFileNames = []
dstFileNames = []
srcFiles = []
dstFiles = []
global ProcessingFileA
ProcessingFileA = ''
ProcessingFileB = ''
ProcessingFileC = ''
ProcessingFileD = ''
d = 0
s = 0
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
    for filepath,dirnames,filenames in os.walk(r''+srcDir):
        for filename in filenames:
            srcFileNames.append(os.path.join(filename))
    for filepath,dirnames,filenames in os.walk(r''+dstDir):
        for filename in filenames:
            dstFileNames.append(os.path.join(filename))

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
    try:
        threading.Thread(target=copytree, args=(src_dir, dst_dir,False,None,copy2,False,True)).start()
    except:
        raise

    
def __update_progress(dst_dir, src_dir):
    pb["maximum"] = get_dir_size(src_dir)
    pb["value"] = get_dir_size(dst_dir)
    global ProcessingFileA
    ProcessingFileA = dst_dir+f"{pb["value"]/1024/1024} MB"
    if get_dir_size(dst_dir) >= get_dir_size(src_dir):
        window.after_cancel(__update_progress)
        get_files(src_dir, dst_dir)
        s - 0
        window.after(100, __checkHarsh, dst_dir, src_dir, d, s)
    else:
        window.after(100, __update_progress, dst_dir, src_dir)

def __checkHarsh(dst_dir, src_dir, d, s):
    hb["maximum"] = len(dstFiles)
    hb["value"] = d
    if d  < len(dstFiles):
        print(srcFileNames[s] == dstFileNames[d])
        if srcFileNames[s] == dstFileNames[d]:
            if (calculate_file_hash(srcFiles[s])) != (calculate_file_hash(dstFiles[d])): 
                # if the hash of the source and destination directories are not the same
                messagebox.showerror(message="The directories("+ srcFiles[d-1] +","+ dstFiles[d-1] +") are not the same,please try again")
                # raise Exception("The directories are not the same,please try again")
            else:
                pass
            d = d + 1
        else:
            s = d + 1
        print(srcFileNames[s])
        print(dstFileNames[d])
        time.sleep(10000)
        window.after(100, __checkHarsh, dst_dir, src_dir, d, s)
    else:
        messagebox.showinfo(message="Copy Completed")
        d = 0
        window.after_cancel(__checkHarsh)

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
        window.after(100, __update_progress, dst_dir, src_dir)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x768")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    241.0,
    768.0,
    fill="#BFBFBF",
    outline="")

canvas.create_rectangle(
    241.0,
    0.0,
    1024.0,
    768.0,
    fill="#3F3F3F",
    outline="")

canvas.create_text(
    9.0,
    186.0,
    anchor="nw",
    text="Bunny Card",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)

canvas.create_rectangle(
    338.0,
    87.0,
    949.0,
    144.0,
    fill="#CCFFF2",
    outline="")

canvas.create_rectangle(
    338.0,
    187.0,
    949.0,
    244.0,
    fill="#FFCCE2",
    outline="")

canvas.create_rectangle(
    338.0,
    287.0,
    949.0,
    344.0,
    fill="#FFF07F",
    outline="")

canvas.create_rectangle(
    338.0,
    387.0,
    949.0,
    444.0,
    fill="#F2F2F2",
    outline="")

canvas.create_rectangle(
    338.0,
    487.0,
    949.0,
    544.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    338.0,
    490.0,
    949.0,
    547.0,
    fill="#F2F2F2",
    outline="")

canvas.create_text(
    356.0,
    102.0,
    anchor="nw",
    text="原始地址",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    708.0,
    117.0,
    image=entry_image_1
)
srcDir = Entry(
    bd=0,
    bg="#C7FFF1",
    fg="#000716",
    highlightthickness=0
)
srcDir.place(
    x=481.0,
    y=102.0,
    width=454.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    708.0,
    216.0,
    image=entry_image_2
)
dstDir = Entry(
    bd=0,
    bg="#FFCCE2",
    fg="#000716",
    highlightthickness=0
)
dstDir.place(
    x=481.0,
    y=201.0,
    width=454.0,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    756.5,
    414.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F2F2F2",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=578.0,
    y=399.0,
    width=357.0,
    height=28.0
)

canvas.create_text(
    356.0,
    201.0,
    anchor="nw",
    text="目标地址",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)

canvas.create_text(
    356.0,
    301.0,
    anchor="nw",
    text="校验方式",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)

canvas.create_text(
    472.0,
    301.0,
    anchor="nw",
    text="SHA256",
    fill="#FFF07F",
    font=("Inter ExtraBold", 24 * -1)
)

canvas.create_text(
    356.0,
    399.0,
    anchor="nw",
    text="目的地文件夹名",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:copyCard(srcDir.get(),dstDir.get()),
    relief="flat"
)
button_1.place(
    x=796.0,
    y=481.0,
    width=128.0,
    height=75.0
)

canvas.create_rectangle(
    7.0,
    625.0,
    232.0,
    760.0,
    fill="#D8CC6C",
    outline="")

canvas.create_rectangle(
    7.0,
    625.0,
    232.0,
    685.0,
    fill="#FFF07F",
    outline="")

canvas.create_rectangle(
    7.0,
    475.0,
    232.0,
    610.0,
    fill="#A9D8CD",
    outline="")

canvas.create_text(
    19.0,
    637.0,
    anchor="nw",
    text="校验进度",
    fill="#000000",
    font=("PingFangSC Medium", 15 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    191.5,
    648.0,
    image=entry_image_4
)

hb = ttk.Progressbar(length=200, mode="determinate")
hb["maximum"] = 100
hb["value"] = 0
hb.place(
    x=19.0,
    y=658.0,
    width=200.0,
    height=10.0,
)
entry_4 = Label(
    bd=0,
    fg="#000716",
    text=int(hb["value"]/hb["maximum"]),
    highlightthickness=0
)
entry_4.place(
    x=160.0,
    y=637.0,
    width=63.0,
    height=20.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    119.0,
    706.0,
    image=entry_image_5
)
entry_5 = Label(
    bd=0,
    text=ProcessingFileC,
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=19.0,
    y=696.0,
    width=200.0,
    height=18.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    119.0,
    737.0,
    image=entry_image_6
)
entry_6 = Label(
    bd=0,
    text=ProcessingFileD,
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=19.0,
    y=727.0,
    width=200.0,
    height=18.0
)

canvas.create_rectangle(
    7.0,
    475.0,
    232.0,
    535.0,
    fill="#C7FFF1",
    outline="")

canvas.create_text(
    19.0,
    487.0,
    anchor="nw",
    text="复制进度",
    fill="#000000",
    font=("PingFangSC Medium", 15 * -1)
)

pb = ttk.Progressbar(length=200, mode="determinate")
pb["maximum"] = 100
pb["value"] = 0
pb.place(
    x=19.0,
    y=508.0,
    width=200.0,
    height=10.0,
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    191.5,
    498.0,
    image=entry_image_7
)
entry_7 = Label(
    bd=0,
    text=int(pb["value"]/pb["maximum"]),
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=160.0,
    y=487.0,
    width=63.0,
    height=20.0
)



image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    112.0,
    106.0,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=openSrcFloder,
    relief="flat"
)
button_2.place(
    x=903.0,
    y=105.0,
    width=24.0,
    height=22.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=openDstFloder,
    relief="flat"
)
button_3.place(
    x=903.0,
    y=205.0,
    width=24.0,
    height=22.0
)

def refresh(ProcessingFileA,ProcessingFileB):
    entry_8 = Label(bd=0,text=ProcessingFileA,fg="#000716",highlightthickness=0
    ).place(x=16.0,y=554.0,width=200.0,height=18.0)
    entry_9 = Label(bd=0,text=ProcessingFileB,fg="#000716",highlightthickness=0
    ).place(x=16.0,y=585.0,width=200.0,height=18.0)
    window.after(100, refresh,ProcessingFileA,ProcessingFileB)

window.resizable(False, False)
window.mainloop()
