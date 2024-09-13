# Đọc từ điển từ file china.txt
def read_translation_dict(translation_file):
    translation_dict = {}
    with open(translation_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Tách mỗi dòng thành hai phần: từ Trung Quốc và bản dịch
            parts = line.strip().split(':')
            if len(parts) == 2:
                chinese_text, english_text = parts
                translation_dict[chinese_text] = english_text
    return translation_dict

# Thay thế các từ Trung Quốc trong file ip.merge.txt
def replace_chinese_text(input_file, output_file, translation_dict):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            # Tách các phần tử giữa các ký tự phân cách '|'
            parts = line.strip().split('|')
            # Thay thế các phần tử nếu chúng có trong từ điển
            translated_parts = [translation_dict.get(part, part) for part in parts]
            # Ghi lại dòng đã thay thế vào file đầu ra
            file.write('|'.join(translated_parts) + '\n')

    print(f"Đã thay thế các đoạn văn bản và lưu vào {output_file}.")

# Định nghĩa các file đầu vào và đầu ra
translation_file = 'china.txt'
input_file = 'ip.merge.txt'
output_file = 'ip.merge.translated.txt'

# Đọc từ điển dịch
translation_dict = read_translation_dict(translation_file)

# Thay thế văn bản Trung Quốc trong file ip.merge.txt
replace_chinese_text(input_file, output_file, translation_dict)
