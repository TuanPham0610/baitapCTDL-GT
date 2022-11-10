n = input("Check string: ")


def palindrome():

    if n == n[::-1]:
        print("String is palindrome")

    elif n.islower() == n[::-1]:
        print("String is palindrome")

    elif n[::-1].capitalize() == n:
        print('String is palindrome')
            
    else:
        print("String is not palindrome")

palindrome()
