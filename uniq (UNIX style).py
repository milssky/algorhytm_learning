def uniq(seq):
    i = 0
    result = []
    temp = ''
    while i < len(seq):
        temp = seq[i]
        if i + 1 < len(seq) and temp == seq[i + 1]:
            i += 1
            continue
        result.append(temp)
        i += 1

    return result


if __name__ == '__main__':
    print(uniq(['foo']))
