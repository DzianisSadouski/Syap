def min_even_element(tpl):
    even_numbers = [num for num in tpl if num % 2 == 0]
    if even_numbers:
        return min(even_numbers)
    else:
        return tpl[0]


if __name__ == "__main__":
    input_tuple = (3, 7, 11, 5, 9, 15, 8, 2, 10)
    print("Исходный кортеж:", input_tuple)
    result = min_even_element(input_tuple)
    print("Наименьший четный элемент кортежа:", result)
