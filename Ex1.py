"""
    Exercise 1:
    Simulation of an ATM.
"""


def check_code(client):
    """
    Validate client's code from input.
    :param client: dictionary representing the ATM user.
    :return: True if the typed code matches the client's False after 5 failed attempts.
    """
    print("Enter code:")
    code = input()
    attempts = 1
    while code != client["code"] and attempts < 5:
        print("Your code is incorrect, try again.")
        attempts += 1
        code = input()
    return code == client["code"]


def withdraw_money(client):
    """
    Withdraw money from client's account (change balance).
    :param client: dictionary representing the ATM user.
    :return: None
    """
    print("Enter sum to withdraw (50, 20 or any other):")
    client["balance"] -= int(input())


def print_balance(client):
    """
    Print the balance in the account of a given client.
    :param client: dictionary representing the ATM user.
    :return: None
    """
    print("Balance:", client["balance"])


def change_code(client):
    """
    Change client's code (from input).
    :param client: dictionary representing the ATM user.
    :return: None
    """
    print("Enter new code:")
    client["code"] = input()


def main():
    """
    Example of a main program, using the ATM features by input.
    :return: None
    """
    client = {"balance": 2700, "code": "1234"}
    atm_options = {"A": print_balance, "B": withdraw_money, "C": change_code}

    if not check_code(client):
        print("Too many attempts, you're blocked")
        return

    print("Choose action for the ATM: \n" +
          "A -- print balance. \n" +
          "B -- withdraw money. \n" +
          "C -- change code. \n" +
          "Any other key -- exit.")

    x = input()
    while x in atm_options.keys():
        atm_options[x](client)
        # print(client) # DEBUG print
        if not check_code(client):
            print("Too many attempts, you're blocked")
            return
        print("Choose another action: ")
        x = input()


if __name__ == '__main__':
    main()
