# 백준11653
# 시간 너무 오래 걸림

n = int(input())
i = 2

while n != 1:
    if n % i == 0:
        print(i)
        n = n // i
    else:
        i += 1
