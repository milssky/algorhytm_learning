def huffman_decode(encoded, code):
    sx = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break
    return "".join(sx)


if __name__ == '__main__':
    k, l = input().split()
    code = {}
    for i in range(int(k)):
        code.update([input().split()])

    print(code)
