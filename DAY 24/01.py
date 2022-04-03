# 백준4504

n = int(input())

while True:
    number = int(input())

    if number == 0:
        break

    if number % n == 0:
        print("{} is a multiple of {}.".format(number, n))
    else:
        print("{} is NOT a multiple of {}.".format(number, n))
