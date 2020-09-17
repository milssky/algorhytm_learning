import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def tokenizer(expr):
    tokens = []
    stack = []
    open_parenthesis_positions = dict()
    close_parenthesis_position = dict()

    i = 0
    while i < len(expr):
        if expr[i] == ' ':
            i += 1
            continue
        if expr[i].isdigit():
            j = i
            while i + 1 < len(expr) and (expr[i + 1].isdigit() or expr[i + 1] == '.'):
                i += 1
            tokens.append(float(expr[j: i + 1]))
        else:
            if expr[i] == '(':
                stack.append(len(tokens))
            if expr[i] == ')':
                j = len(tokens)
                open_parenthesis_positions[j] = stack.pop()
                close_parenthesis_position[open_parenthesis_positions[j]] = j
            tokens.append(expr[i])

        i += 1
    return tokens, open_parenthesis_positions, close_parenthesis_position


def calc(e):
    tokens, op, cl = tokenizer(e)

    def eval_muldiv(tokens):
        variable, operator = 1, '*'
        for token in tokens:
            if isinstance(token, float):
                variable = OPERATORS[operator](variable, token)
            else:
                operator = token
        return variable

    def dfs(idx_st, idx_en):
        idx = idx_st
        tokens_no_par = []
        while idx <= idx_en:
            if tokens[idx] == '(':
                v = dfs(idx + 1, cl[idx] - 1)
                tokens_no_par.append(v)
                idx = cl[idx]
            else:
                tokens_no_par.append(tokens[idx])

            idx += 1
        tokens_no_neg = []
        idx = 0
        while idx < len(tokens_no_par):
            if tokens_no_par[idx] != '-':
                tokens_no_neg.append(tokens_no_par[idx])
            else:
                if idx > 0 and isinstance(tokens_no_par[idx - 1], float):
                    tokens_no_neg.append('-')
                else:
                    j = idx
                    while not isinstance(tokens_no_par[idx], float):
                        idx += 1
                    n_neg = idx - j
                    v = tokens_no_par[idx] * ((-1) ** (n_neg % 2))
                    tokens_no_neg.append(v)
            idx += 1
        idx_addsub = [-1]
        for idx, token in enumerate(tokens_no_neg):
            if token == '+' or token == '-':
                idx_addsub.append(idx)

        v, o = 0, '+'
        for i in range(1, len(idx_addsub)):
            j, k = idx_addsub[i - 1], idx_addsub[i]
            v1 = eval_muldiv(tokens_no_neg[j + 1: k])
            v = OPERATORS[o](v, v1)
            o = tokens_no_neg[k]

        v = OPERATORS[o](v, eval_muldiv(tokens_no_neg[idx_addsub[-1] + 1:]))
        return v

    return dfs(0, len(tokens) - 1)


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
    # for test in tests:
    #     print(calc(test[0]))
    calc(tests[2][0])