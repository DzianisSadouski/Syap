import functools

def process_list(lst):
    numbers = [item for item in lst if isinstance(item, (int, float))]
    words = [item for item in lst if isinstance(item, str)]

    sum_numbers = sum(numbers)
    product_numbers = 1 if not numbers else functools.reduce(lambda x, y: x * y, numbers)

    print("Список слов:", words)
    print("Сумма чисел:", sum_numbers)
    print("Произведение чисел:", product_numbers)
    print("Три наибольших элемента:", sorted(numbers, reverse=True)[:3])


if __name__ == "__main__":
    sample_list = [1, 34, 'qwerty', 12, 13, 16, 'Love', 'Python']
    print("Исходный список:", sample_list)
    process_list(sample_list)
