def main():
    with open('24.txt', 'r') as f:
        text = f.read()

    prev_ch = ''
    length = 1
    max_length = 1
    for ch in text:
        if prev_ch != ch and (prev_ch != '' or ch != ''):
            length += 1
        else:
            if length > max_length:
                max_length = length
            length = 1
        prev_ch = ch
    print(max_length)

if __name__ == '__main__':
    main()