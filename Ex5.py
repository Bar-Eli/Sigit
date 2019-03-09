"""
    Exercise 5:
    Validate Israeli ID number.
"""


def validate_id(id_num):
    """

    :param id_num: An Israeli ID number (as a string)
    :return: bool indicating whether the number is valid or not.
    """
    factor = 1
    sum_dig = 0
    for c in id_num[:-1]:
        dig = int(c)
        dig *= factor
        sum_dig += (dig % 10) + (dig // 10)
        factor = 3 - factor

    return str(10 - sum_dig % 10) == id_num[-1]


def main():
    """
    Main program example.
    """
    print(validate_id("123456782"))
    print(validate_id("123456789"))


if __name__ == '__main__':
    main()
