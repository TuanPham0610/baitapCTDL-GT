string = input('Nhap string: ') 

if string == string[::-1]:
    print('String is palindrome')

elif string[::-1].islower() == string:
    print('String is palindrome')

elif string[::-1].capitalize() == string:
    print('String is palindrome')

elif string[::-1].islower() == string[::-1].capitalize() == string:
    print('String is palindrome')

else:
    print('String is not palindrome')

