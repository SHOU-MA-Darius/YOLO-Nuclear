import os

def delete_images_without_txt(src_folder):
    # 获取源文件夹中的所有文件名
    files = os.listdir(src_folder)

    # 遍历所有文件
    for file in files:
        # 只处理图片文件（例如jpg和png），你可以根据需要扩展支持的图片格式
        if file.endswith(('.jpg', '.jpeg', '.png')):
            # 构建对应的txt文件名
            txt_file = os.path.splitext(file)[0] + '.txt'
            txt_file_path = os.path.join(src_folder, txt_file)

            # 检查对应的txt文件是否存在
            if not os.path.exists(txt_file_path):
                # 构建图片文件的完整路径
                image_file_path = os.path.join(src_folder, file)
                # 删除图片文件
                os.remove(image_file_path)
                print(f"Deleted: {file}")
# 示例用法
src_folder = 'E:\datasets\hyh-new\hyh-new\二期\hyh_y4#_20240524-0610/2024-0524-0610'
delete_images_without_txt(src_folder)
