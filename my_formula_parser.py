import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


class Token:
    def __init__(self, _token_type, _value):
        self.value = _value
        self.type = _token_type

    def __repr__(self):
        return f'[{self.value}]'


class Tokenizer:
    def __init__(self, _formula_str: str):
        self.formula_str = _formula_str.replace(' ', '')
        self.result = []
        self.number_buffer = []
        self.tokenize()

    def tokenize(self):
        for index in range(len(self.formula_str)):
            value = self.formula_str[index]

            if self.is_digit(value):
                self.number_buffer.append(value)

            elif value == '.':
                self.number_buffer.append(value)

            elif self.is_operator(value):
                self.clear_number_buffer_as_literal()
                self.result.append(Token("Operator", value))

            elif self.is_left_parenthesis(value):
                if len(self.number_buffer) > 0:
                    self.clear_number_buffer_as_literal()
                    self.result.append(Token("Operator", "*"))
                self.result.append(Token("Left parenthesis", value))

            elif self.is_right_parenthesis(value):
                self.clear_number_buffer_as_literal()
                self.result.append(Token("Right parenthesis", value))

        if len(self.number_buffer) > 0:
            self.clear_number_buffer_as_literal()


    def is_digit(self, ch):
        return ch.isdigit()

    def is_operator(self, ch):
        return ch in '+-/*'

    def is_left_parenthesis(self, ch):
        return ch == '('

    def is_right_parenthesis(self, ch):
        return ch == ')'

    def clear_number_buffer_as_literal(self):
        if len(self.number_buffer) > 0:
            self.result.append(Token('Literal', ''.join(self.number_buffer)))
            self.number_buffer = []

def calc(expr: str):
    pass


if __name__ == '__main__':
    tests = [
        ["1 + 1", 2],
        ["8/16", 0.5],
        ["3 -(-1)", 4],
        ["2 + -2", 0],
        ["10- 2- -5", 13],
        ["(((10)))", 10],
        ["3 * 5", 15],
        ["-7 * -(6 / 3)", 14]
    ]
    for test in tests:
        print(Tokenizer(test[0]).result)
