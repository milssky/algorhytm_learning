def main():
    d = {}
    for i in range(174457, 174505 + 1):
        delimiter = 0
        for j in range(2, i // 2):
            if i % j == 0:
                delimiter += 1
                if delimiter > 2:
                    break
                d[delimiter] = j
        if delimiter == 2:
            print(d[1], d[2])


if __name__ == '__main__':
    main()
