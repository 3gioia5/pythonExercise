# 백준1302

n = int(input())
sold = dict()

for i in range(n):
    title = input()

    if title not in sold:
        sold[title] = 1
    else:
        sold[title] += 1

best = max(sold.values())
best_seller = list()

for title, amount in sold.items():
    if amount == best:
        best_seller.append(title)

print(sorted(best_seller)[0])
