import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}



class Token():
    def __init__(self, _value, _token_type):
        self.value = _value
        self.type = _token_type


class Tokenizer:
    def __init__(self, _formula_str):
        self.formula_str = _formula_str
        self.result = []
        self.letter_buffer = []
        self.number_buffer = []

    def tokenize(self):
        pass

    def is_digit(self, ch):
        return ch.isdigit()

    def is_comma(self, ch):
        return ch == ',' or ch == '.'

    def is_operator(self, ch):
        return ch in '+-/*'

    def is_letter(self, ch):
        return ch.isalpha()

    def is_left_parenthesis(self, ch):
        return ch is '('

    def is_right_parenthesis(self, ch):
        return ch is ')'






if __name__ == '__main__':
    pass
