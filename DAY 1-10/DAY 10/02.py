# 백준10886

n = int(input())
positive = 0
negative = 0

for i in range(n):
    opinion = input()

    if opinion == '0':
        negative += 1
    elif opinion == '1':
        positive += 1

if negative > positive:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
