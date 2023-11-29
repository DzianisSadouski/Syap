import json

def write_data_to_file(file_name):
    try:
        with open(file_name, 'w') as file:
            print("Введите данные (пустая строка для завершения):")
            while True:
                line = input()
                if not line:
                    break
                file.write(line + '\n')
        print(f"Данные записаны в файл {file_name}")
    except Exception as e:
        print(f"Произошла ошибка при записи данных в файл: {e}")


def copy_lines_with_single_word(input_file, output_file):
    try:
        with open(input_file, 'r') as f1, open(output_file, 'w') as f2:
            lines = f1.readlines()
            for line in lines:
                words = line.split()
                if len(words) == 1:
                    f2.write(line)
        print(f"Строки с одним словом скопированы в файл {output_file}")
    except Exception as e:
        print(f"Произошла ошибка при копировании строк: {e}")


def find_longest_word(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            words = [word for line in lines for word in line.split()]
            longest_word = max(words, key=len)
            print(f"Самое длинное слово в файле {file_name}: {longest_word}")
    except Exception as e:
        print(f"Произошла ошибка при поиске самого длинного слова: {e}")

if __name__ == "__main__":
    file1 = "F1.txt"
    file2 = "F2.txt"
    write_data_to_file(file1)
    copy_lines_with_single_word(file1, file2)
    find_longest_word(file2)
