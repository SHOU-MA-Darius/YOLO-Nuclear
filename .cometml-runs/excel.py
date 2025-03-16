import csv

def transpose_csv(input_file, output_file):
    # 读取原始 .csv 文件的数据
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # 转置数据
    transposed_data = []
    max_cols = max(len(row) for row in rows)
    for i in range(max_cols):
        transposed_row = []
        for row in rows:
            if i < len(row):
                transposed_row.append(row[i])
            else:
                transposed_row.append('')
        transposed_data.append(transposed_row)

    # 找到 Distance_gps 和 Distance_vl 所在的行索引
    gps_index = None
    vl_index = None
    for idx, row in enumerate(transposed_data):
        if row[0] == 'Distance_gps':
            gps_index = idx
        elif row[0] == 'Distance_vl':
            vl_index = idx

    # 删除小于-100000的值所在的行，但保留 Distance_gps 和 Distance_vl 的行
    cleaned_transposed_data = []
    for idx, row in enumerate(transposed_data):
        if idx == gps_index or idx == vl_index:
            cleaned_transposed_data.append(row)
        else:
            try:
                if all(float(cell) >= -100000 for cell in row[1:]):
                    cleaned_transposed_data.append(row)
            except ValueError:
                cleaned_transposed_data.append(row)

    # 写入转置后的数据到新的 .csv 文件
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_transposed_data)

# 调用函数进行转置
input_file = 'E:/TaiShanCsv/example1.sv.csv'  # 输入文件名
output_file = 'E:/TaiShanCsv/suc.sv.csv'  # 输出文件名

transpose_csv(input_file, output_file)
