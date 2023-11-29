def create_char_count_dict(text):
    char_count_dict = {}
    for char in text:
        if char.isalpha():
            char_count_dict[char] = char_count_dict.get(char, 0) + 1
    return char_count_dict


if __name__ == "__main__":
    input_string = 'An apple a day keeps the doctor away'
    char_count_dict = create_char_count_dict(input_string)
    print("Словарь из строки:", char_count_dict)