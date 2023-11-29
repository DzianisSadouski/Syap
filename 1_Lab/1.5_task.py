if __name__ == "__main__":
    shop_inventory = {
        'Моторное масло': ['Высококачественное моторное масло для всех типов двигателей', 25.99, 100],
        'Тормозные колодки': ['Прочные тормозные колодки для безопасного вождения', 49.99, 50],
        'Воздушный фильтр': ['Эффективный воздушный фильтр для оптимальной работы двигателя', 12.99, 75],
        'Свечи зажигания': ['Премиальные свечи зажигания для лучшей эффективности топлива', 7.99, 120],
        'Трансмиссионное масло': ['Трансмиссионное масло для плавных переключений передач', 19.99, 80],
        'Аккумулятор': ['Долговечный аккумулятор для надежного пуска', 99.99, 30],
    }

    while True:
        print("\nМеню:")
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Вся информация")
        print("5. Покупка")
        print("6. До свидания")

        choice = input("Выберите пункт меню (1-6): ")


        if choice == '1':
            item = input("Введите название продукции: ")
            if item in shop_inventory:
                print(f"Описание: {shop_inventory[item][0]}")
            else:
                print("Такой продукции нет в магазине.")
        elif choice == '2':
            item = input("Введите название продукции: ")
            if item in shop_inventory:
                print(f"Цена: {shop_inventory[item][1]}")
            else:
                print("Такой продукции нет в магазине.")
        elif choice == '3':
            item = input("Введите название продукции: ")
            if item in shop_inventory:
                print(f"Количество: {shop_inventory[item][2]}")
            else:
                print("Такой продукции нет в магазине.")
        elif choice == '4':
            for item, info in shop_inventory.items():
                print(f"{item}: {info[0]}, Цена: {info[1]}, Количество: {info[2]}")
        elif choice == '5':
            item = input("Введите название продукции (или 'n' для выхода): ")
            if item == 'n':
                break
            quantity = int(input("Введите количество: "))
            if item in shop_inventory and shop_inventory[item][2] >= quantity:
                price = shop_inventory[item][1] * quantity
                shop_inventory[item][2] -= quantity
                print(f"Покупка совершена. Сумма: {price}, Остаток: {shop_inventory[item][2]}")
            elif item in shop_inventory:
                print("Недостаточно товара на складе.")
            else:
                print("Такой продукции нет в магазине.")
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите от 1 до 6.")
