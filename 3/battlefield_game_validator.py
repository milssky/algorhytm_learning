def validator(field):
    n, m = len(field), len(field[0])

    def checkCell(i, j):  # check if parameters are in range
        if 0 <= i < n and 0 <= j < m: return field[i][j]
        return 0

    def findCell(i, j):  # return size of ship
        if checkCell(i + 1, j + 1) or checkCell(i + 1,
                                                j - 1): return 10  # check if there's ship on SE or SW (South,East,West)
        if checkCell(i + 1, j) and checkCell(i, j + 1): return 10  # check if there's ship on the right and bottom
        field[i][j] = 2
        if checkCell(i + 1, j): return findCell(i + 1,
                                                j) + 1  # if there's ship on bottom,continue to find ship in that dir
        if checkCell(i, j + 1): return findCell(i, j + 1) + 1
        return 1

    ships = [0, 0, 0, 0, 0]
    for i in range(n):
        for j in range(m):
            if checkCell(i, j) == 1:
                size = findCell(i, j)
                if size > 4:
                    return False  # the largest ship size is 4
                else:
                    ships[size] += 1
    if ships[1:] == [4, 3, 2, 1]:
        return True
    else:
        return False


if __name__ == '__main__':
    battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print(validator(battleField))