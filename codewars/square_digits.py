def square_digits(num):
    return 0 if num == 0 else int(''.join([str(int(n)**2) for n in str(num)]))
    # return ''.join([str(int(n)**2) for n in str(num)])
    # return ' '.join((int(n)**2) for n in str(num))


print(square_digits(9119))
print(square_digits(0))
