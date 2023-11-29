if __name__ == "__main__":
    pi_sum = 0
    sign = 1

    for i in range(1, 1001, 2):
        pi_sum += sign * 1/i
        sign *= -1

    pi = 4 * pi_sum
    print("Число Пи:", pi)