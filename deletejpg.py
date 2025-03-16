import os

# 指定目标目录
directory = 'E:/datasets/coco/综合信息系统'

# 遍历目标目录中的所有文件
for filename in os.listdir(directory):
    # 检查文件是否以.jpg结尾
    if filename.endswith('.bmp'):
        # 构建对应的.txt文件名
        txt_filename = filename[:-4] + '.txt'
        # 检查.txt文件是否存在
        if not os.path.exists(os.path.join(directory, txt_filename)):
            # 如果不存在对应的.txt文件，删除该.jpg文件
            os.remove(os.path.join(directory, filename))
            print(f'Deleted {filename}')