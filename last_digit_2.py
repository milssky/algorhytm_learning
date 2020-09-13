def last_digit(n1, n2):
    return pow(n1, n2, 10)


if __name__ == '__main__':
    print(last_digit(4, 1))
    print(last_digit(4, 2))
    print(last_digit(9, 7))
    print(last_digit(10, 10 ** 10))
    print(last_digit(2 ** 200, 2 ** 20))
