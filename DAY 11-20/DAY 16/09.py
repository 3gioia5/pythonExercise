# 백준10707

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x_price = a * p

if p > c:
    y_price = b + (p - c) * d
else:
    y_price = b

if x_price > y_price:
    print(y_price)
else:
    print(x_price)
