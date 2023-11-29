if __name__ == "__main__":
    print("Деление 10 на число:")
    while True:
        try:
            number = int(input("Введите число: "))
            result = 10 / number
            print(f"Результат деления: {result}")
            break
        except ValueError as ve:
            print(f"Ошибка: {ve}")
        except ZeroDivisionError:
            print("Ошибка деления на ноль.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
