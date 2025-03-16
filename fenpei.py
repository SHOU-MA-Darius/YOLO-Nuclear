import os
import shutil
import random


def split_files(source_folder, folder_A, folder_B, ratio=0.8):
    # 确保目标文件夹存在
    os.makedirs(folder_A, exist_ok=True)
    os.makedirs(folder_B, exist_ok=True)

    # 获取所有.jpg文件及其对应的.txt文件
    files = [f for f in os.listdir(source_folder) if f.endswith('.bmp')]

    # 打乱文件顺序
    random.shuffle(files)

    # 计算分配的数量
    split_index = int(len(files) * ratio)

    # 分配文件
    for i, file_name in enumerate(files):
        base_name = os.path.splitext(file_name)[0]
        jpg_file = os.path.join(source_folder, base_name + '.bmp')
        txt_file = os.path.join(source_folder, base_name + '.txt')

        if i < split_index:
            # 移动到A文件夹
            shutil.move(jpg_file, os.path.join(folder_A, base_name + '.bmp'))
            if os.path.exists(txt_file):
                shutil.move(txt_file, os.path.join(folder_A, base_name + '.txt'))
        else:
            # 移动到B文件夹
            shutil.move(jpg_file, os.path.join(folder_B, base_name + '.bmp'))
            if os.path.exists(txt_file):
                shutil.move(txt_file, os.path.join(folder_B, base_name + '.txt'))


# 使用示例
source_folder = 'E:/datasets/coco/综合信息系统'  # 源文件夹路径
folder_A = 'E:/datasets/coco/综合信息系统/train'  # A文件夹路径
folder_B = 'E:/datasets/coco/综合信息系统/val'  # B文件夹路径

split_files(source_folder, folder_A, folder_B)
