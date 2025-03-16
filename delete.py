import os
import shutil


def move_jpg_files(src_folder, dst_folder):
    # 检查目标文件夹是否存在，不存在则创建
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    # 遍历源文件夹及其子文件夹
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith('.bmp'):
                src_file_path = os.path.join(root, file)

                # 处理目标文件夹中可能存在的同名文件，自动重命名
                dst_file_path = os.path.join(dst_folder, file)
                counter = 1
                while os.path.exists(dst_file_path):
                    dst_file_path = os.path.join(dst_folder, f"{os.path.splitext(file)[0]}_{counter}.bmp")
                    counter += 1

                # 移动文件
                shutil.move(src_file_path, dst_file_path)
                print(f"已移动: {src_file_path} -> {dst_file_path}")


# 使用示例
src_folder = 'E:/datasets/coco/综合信息系统'  # 源文件夹路径
dst_folder = 'E:/datasets/coco/综合信息系统'  # 目标文件夹路径

move_jpg_files(src_folder, dst_folder)
