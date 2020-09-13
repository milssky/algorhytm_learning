# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s: str):
    from collections import Counter
    if s:
        return list(Counter(s).items())
    else:
        return None


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs: list, s: str) -> str:
    return ""


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs: list, bits: str) -> str:
    return ""


if __name__ == '__main__':
    string = 'aaaabcc'
    freqs = frequencies(string)
    print(freqs)
