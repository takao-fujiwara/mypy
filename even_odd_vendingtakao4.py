
def even_odd_vending(num):

    if (num % 2) == 0:
        print('Even')
    else:
        print('Odd')
    count = 1
    while count <= 9:
        num += 2
        print(num)
        # increment the count of numbers printed
        count += 1


def enter_number():
    while True:
        num = float(input('Enter an integer: (Exit is -Number): '))
        if num.is_integer() and num >= 0:
            even_odd_vending(int(num))
        else:
            break


if __name__ == '__main__':
    try:
        enter_number()

    except ValueError:
        print('Please enter number')
        enter_number()
