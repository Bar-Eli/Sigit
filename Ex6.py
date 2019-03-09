"""
    Exercise 6:
    Map function
"""


def my_map(func, lst):
    """
    Run a given function on any item of a given list
    :param func: function (works on one item of the list)
    :param lst: A list
    :return: All of the list items' result of the given function (new list).
    """
    result = []
    for i in lst:
        result.append(func(i))
    return result


def add(x):
    """
    Example of a function on an item of a list.
    :param x: A number
    :return: The number + 2
    """
    return x+2


def main():
    """
    Main program example.
    """
    print(my_map(lambda x: x * 2, [1, 2, 3, 4])) # Map list with lambda function.
    print(my_map(add, [1, 2, 3, 4])) # Map list with regular function.


if __name__ == '__main__':
    main()
