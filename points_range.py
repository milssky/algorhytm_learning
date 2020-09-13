import random


def quick_sort_ranges(array: list, sort_start: int, sort_end: int) -> None:

    if sort_start >= sort_end:
        return

    first_pointer, last_pointer = sort_start, sort_end
    pivot = array[random.randint(sort_start, sort_end)][1]

    while first_pointer <= last_pointer:

        while array[first_pointer][1] < pivot:
            first_pointer += 1

        while array[last_pointer][1] > pivot:
            last_pointer -= 1

        if first_pointer <= last_pointer:
            array[first_pointer], array[last_pointer] = array[last_pointer], array[first_pointer]

            first_pointer, last_pointer = first_pointer + 1, last_pointer - 1

    quick_sort_ranges(array, sort_start, last_pointer)
    quick_sort_ranges(array, first_pointer, sort_end)


def get_result_ranges(ranges:list) -> list:
    quick_sort_ranges(ranges, 0, len(ranges) - 1)
    points = []
    for range in ranges:
        if len(points) == 0 or range[0] > points[-1]:
            points.append(range[1])

    return points


def main() -> None:
    range_lenght = int(input())
    ranges = []
    for _ in range(0, range_lenght):
        ranges.append([int(i) for i in input().split()])

    points = get_result_ranges(ranges)
    print(len(points))
    print(" ".join(map(str, points)))


if __name__ == '__main__':
    main()

