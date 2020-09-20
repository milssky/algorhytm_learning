from itertools import cycle


def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])


def encode_rail_fence_cipher(string, n):
    p = rail_pattern(n)
    return ''.join(sorted(string, key=lambda i: next(p)))


def decode_rail_fence_cipher(string, n):
    p = rail_pattern(n)
    indexes = sorted(range(len(string)), key=lambda i: next(p))
    result = [''] * len(string)
    for i, c in zip(indexes, string):
        result[i] = c
    return ''.join(result)


if __name__ == '__main__':
    print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3))
    print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3))
