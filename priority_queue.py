import sys


class PriorityQueue:
    def __init__(self):
        self.data = []

    def inset(self, element: int) -> None:

        self.data.append(element)
        index = len(self.data)

        while len != 1 and self.data[int(index / 2) - 1] < self.data[index - 1]:
            self.data[int(index / 2) - 1], self.data[index - 1] = self.data[index - 1], self.data[int(index / 2) - 1]
            index = int(index / 2)

    def extract_max(self) -> int:
        max_value = self.data[0]

        if len(self.data) > 1:
            del self.data[-1]

            index = 1
            data_len = len(self.data)

            first_child = 2 if data_len > 1 else None
            second_child = 3 if data_len > 2 else None

            while first_child and self.data[first_child - 1] > self.data[index - 1] or \
                    second_child and self.data[second_child - 1] > self.data[index - 1]:

                if first_child and second_child and self.data[first_child - 1] > self.data[second_child - 1] or not second_child:

                    self.data[first_child - 1], self.data[index - 1] = self.data[index - 1], self.data[
                        first_child - 1]
                    index = first_child
                else:
                    self.data[second_child - 1], self.data[index - 1] = self.data[index - 1], self.data[
                        second_child - 1]
                    index = second_child

                first_child = (2 * index) if data_len >= (2 * index) else None
                second_child = (2 * index + 1) if data_len >= (2 * index + 1) else None
            else:
                self.data = []

            return max_value


if __name__ == "__main__":
    inst = PriorityQueue()

    operation_count = int(sys.stdin.readline())
    result_list = []

    for _ in range(0, operation_count):
        operation = sys.stdin.readline()

        if 'Insert' in operation:
            value = int(operation.split()[1])
            inst.inset(value)
        else:
            result_list.append(str(inst.extract_max()))

    print('\n'.join(result_list))
