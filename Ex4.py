"""
    Exercise 4:
    Compress a string.
"""


def compress_string(st):
    """
    Compress a string, replace char sequences with the char and the number of times it appears
    :param st: A given string
    :return: The compressed version of the string
    """
    new_str = st[0]
    count = 0
    for c in st:
        if c == new_str[-1]:
            count += 1
        else:
            new_str += str(count) + c
            count = 1
    new_str += str(count)
    return new_str


def main():
    """
    Main program example.
    """
    print(compress_string("abcaadddcc"))
    print(compress_string("aabbb"))


if __name__ == '__main__':
    main()

