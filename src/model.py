import hashlib

def calculate_file_hash(file_path, hash_algorithm='sha256', chunk_size=8192):
    """
    计算文件的哈希值。
    :param file_path: 文件路径
    :param hash_algorithm: 哈希算法（默认为sha256）
    :param chunk_size: 读取文件时的块大小（默认为8192字节）
    :return: 文件的哈希值
    """
    
    hash_obj = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()


# # 示例使用

# file_path1 = input("请输入文件路径：")
# file_path2 = './test/src/test.txt'


# hash_value1 = calculate_file_hash(file_path1)
# hash_value2 = calculate_file_hash(file_path2)


# print(f'The SHA-256 hash of the file is: {hash_value1}')
# print(f'The SHA-256 hash of the file is: {calculate_file_hash(file_path2)}')

# if hash_value1 != hash_value2:
#     print(f"The files are different")

