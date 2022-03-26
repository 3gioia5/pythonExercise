# 백준1009
# 틀림

t = int(input())

for i in range(5):
    a, b = map(int, input().split())

    if a ** b % 10 == 0:
        print(10)
    else:
        print(a ** b % 10)
