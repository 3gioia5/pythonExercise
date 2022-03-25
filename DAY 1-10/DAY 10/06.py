# 백준2576

numbers = list()

for i in range(7):
    i = int(input())

    if i % 2 != 0:
        numbers.append(i)

if len(numbers) == 0:
    print(-1)
else:
    print(sum(numbers))
    print(min(numbers))
