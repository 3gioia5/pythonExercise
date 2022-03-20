# 백준5565

total_price = int(input())
prices = []

for i in range(9):
    price = int(input())
    prices.append(price)

print(total_price - sum(prices))
