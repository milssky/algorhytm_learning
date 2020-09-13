n = int(input())
acc = []
i = 0
while True:
    i += 1
    if i * 2 < n:
        acc.append(i)
        n = n - i
    else:
        acc.append(n)
        break

print(len(acc))
print(" ".join(map(str, acc)))
