def count_vowels_consonants(text):
    vowels = "aeiouAEIOUауоиэыАУОИЭЫ"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

    vowels_count = sum(1 for char in text if char in vowels)
    consonants_count = sum(1 for char in text if char in consonants)

    if vowels_count == consonants_count:
        print("Гласные буквы в тексте:", ', '.join(char for char in text if char in vowels))

    print(f"Количество гласных: {vowels_count}, количество согласных: {consonants_count}")


if __name__ == "__main__":
    text = input("Введите текст: ")
    count_vowels_consonants(text)
