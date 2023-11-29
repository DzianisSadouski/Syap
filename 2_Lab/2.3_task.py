import functools

def find_positive_row(matrix):
    try:
        for row in matrix:
            if all(element > 0 for element in row):
                return row, sum(row)
        raise ValueError("В матрице нет строки, все элементы которой положительны.")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    matrix = [
        [-1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Исходная матрица:")
    for row in matrix:
        print(row)
    result = find_positive_row(matrix)
    print(f"Первая строка с положительными элементами: {result[0]}, Сумма: {result[1]}")
