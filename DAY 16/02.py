# 백준2587

numbers = list()

for i in range(5):
    numbers.append(int(input()))

numbers.sort()

print(int(sum(numbers) / 5))
print(numbers[2])
