"""
    Exercise 7:
    decorate a function, saving its result saving time for future use.
"""
import time # used to simulate a complicated function (takes long time to run).


def decorate(func):
    """
    Provide cache decorator for functions,
    :param func: Function to decorate.
    :return: The function decorated.
    """
    memory = {}

    def inner_func(x):
        """
        Save results in dictionary and return them if the function is called again with the same parameters.
        :param x: Parameter of the given function.
        :return: Result of the function on x
        """
        if x not in memory:
            memory[x] = func(x)
        return memory[x]

    return inner_func


def foo(n):
    """
    Simulation of a complicated function (waits 5 seconds).
    :param n: A number.
    :return: The number doubled.
    """
    time.sleep(5)
    return n * 2


if __name__ == '__main__':

    foo = decorate(foo)

    print(foo(40))
    print(foo(20))
    print(foo(40))