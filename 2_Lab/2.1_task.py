import functools

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Введите число от 0 до 1000: "))
            if 0 <= num <= 1000:
                break
            else:
                print("Введите число в диапазоне от 0 до 1000.")
        except ValueError:
            print("Ошибка ввода. Введите целое число.")

    prime = True
    if num < 2:
        prime = False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break

    print(f"Число {num} простое: {prime}")
