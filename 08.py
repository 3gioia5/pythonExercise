# 1부터 1000까지 자릿수 더한 값 리턴하기

def sum_digit(number):
    total = 0
    str_num = str(number)

    for i in str(number):
        total += int(i)

    return total


i = 1
value = 0

for i in range(1001):
    value += sum_digit(i)

print(value)