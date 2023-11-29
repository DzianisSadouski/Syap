import functools

def process_argument(argument):
    try:
        if isinstance(argument, list):
            sum_numbers = sum(item for item in argument if isinstance(item, (int, float)))
            print(f"Сумма чисел в списке: {sum_numbers}")
        elif isinstance(argument, dict):
            sorted_values = sorted((value for value in argument.values() if isinstance(value, (int, float))), reverse=True)[:3]
            print(f"Три наибольших значения в словаре: {sorted_values}")
        elif isinstance(argument, int):
            digit_sum = sum(int(digit) for digit in str(argument))
            print(f"Сумма цифр числа: {digit_sum}")
        elif isinstance(argument, str):
            word_count = len(argument.split())
            print(f"Количество слов в строке: {word_count}")
        else:
            raise TypeError("Неподдерживаемый тип аргумента.")
    except TypeError as te:
        print(f"Ошибка: {te}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def get_input_argument():
    try:
        input_str = input("Введите аргумент (число, список, словарь или строку): ")
        # Попробуем преобразовать введенный текст в число
        try:
            return int(input_str)
        except ValueError:
            # Если не удалось преобразовать в число, попробуем в список
            try:
                return eval(input_str)
            except:
                # В случае неудачи возвращаем строку
                return input_str
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    argument = get_input_argument()
    process_argument(argument)
