# 백준2592
# 런타임 에러

numbers = list()
for i in range(10):
    number = int(input())
    numbers.append(number)

count = {}
for i in numbers:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

print(sum(numbers) // 10)
print(max(count, key=count.get))
