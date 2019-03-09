"""
    Exercise 2:
    Calculate sum of numbers given by user
"""


def sum_input_lst():
    """Calc sum of a list of numbers given separately

    :return: the sum of the list.
    """
    print("Enter numbers:")
    x = input()
    sum = 0
    while x != 'stop':
        sum += int(x)
        x = input()
        
    return sum


def sum_coded_list():
    """Calc sum of a list of integers given as one string

    :return: the sum of the list.
    """
    print("Enter numbers:")
    lst_str = input()
    lst = lst_str.split(',')
    sum_lst = 0
    for x in lst:
        sum_lst += int(x)
    return sum_lst


def main():
    """Main function, choose input method of the list

    :return: None
    """
    print("This script calculates the sum of a list of given numbers")
    print('Choose input method:')
    print('A -- all the numbers at once, B -- each number separately')
    ex = input()
    if ex == 'A':
        lst_sum = sum_coded_list()
    else:
        lst_sum = sum_input_lst()
    print("The sum is", lst_sum)


if __name__ == '__main__':
    main()
