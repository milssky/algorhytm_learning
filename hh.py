nums = []
for i in range(10, 1000+1):
    a = bin(i)[2:]
    a = a[1:]
    b = ''
    ind = 0
    for el in a:
        if el == '0':
            ind += 1
            continue
        else:
            b += el
            break
    if b + a[ind + 1:] != '':
        nums.append(b + a[ind + 1:])
print(len(set(nums)))
