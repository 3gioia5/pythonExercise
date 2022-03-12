# 백준11720

n = int(input())
numbers = input()
count = 0

for i in range(n):
    count += int(numbers[i])
print(count)