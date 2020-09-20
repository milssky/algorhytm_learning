# https://www.codewars.com/kata/527fde8d24b9309d9b000c4e

def break_pieces(shape):
    pass


if __name__ == '__main__':
    shape = '\n'.join(["+------------+",
                       "|            |",
                       "|            |",
                       "|            |",
                       "+------+-----+",
                       "|      |     |",
                       "|      |     |",
                       "+------+-----+"])

    solution = ['\n'.join(["+------------+",
                           "|            |",
                           "|            |",
                           "|            |",
                           "+------------+"]),
                '\n'.join(["+------+",
                           "|      |",
                           "|      |",
                           "+------+"]),
                '\n'.join(["+-----+",
                           "|     |",
                           "|     |",
                           "+-----+"])]


    print(break_pieces(shape))
    print(solution)
