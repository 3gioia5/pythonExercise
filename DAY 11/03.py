# 백준5543

burgers = list()
for i in range(3):
    burgers.append(int(input()))

drinks = list()
for i in range(2):
    drinks.append(int(input()))

print(min(burgers) + min(drinks) - 50)
