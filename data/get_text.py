import re

# Tạo biểu thức chính quy để tìm các ký tự Trung Quốc
chinese_pattern = re.compile(r'[\u4e00-\u9fff]')

# Đọc dữ liệu từ file ip.merge.txt
input_file = 'ip.merge.txt'
output_file = 'china.txt'

# Sử dụng set để lưu các đoạn văn bản Trung Quốc và loại bỏ trùng lặp
chinese_texts = set()

# Đọc dữ liệu từ file và xử lý từng dòng
with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        # Tách các phần tử giữa các ký tự phân cách '|'
        parts = line.strip().split('|')
        for part in parts:
            # Kiểm tra xem phần tử có chứa ký tự Trung Quốc không
            if chinese_pattern.search(part):
                chinese_texts.add(part)

# Lưu các đoạn đã lọc vào file china.txt
with open(output_file, 'w', encoding='utf-8') as file:
    for text in chinese_texts:
        file.write(text + '\n')

print(f"Đã lưu các đoạn văn bản Trung Quốc vào {output_file}.")
