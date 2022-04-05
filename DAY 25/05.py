# 백준2108
# 실패...

n = int(input())
numbers = list()

for _ in range(n):
    numbers.append(int(input()))

# 산술평균
print(round(sum(numbers) / n))

# 중앙값
n_nums = sorted(numbers)
print(n_nums[int(n / 2)])

# 최빈값
counts = dict()
for i in range(1, n + 1):
    counts[i] = []

maxCount = 1
count = 1
for j in range(1, n):
    if numbers[j] == numbers[j - 1]:
        count += 1
    else:
        counts[count].append(numbers[j - 1])
        if maxCount < count:
            maxCount = count
            count = 1
    if j == n - 1:
        counts[count].append(numbers[j])
        if maxCount < count:
            maxCount = count

if n == 1:
    counts[1].append(numbers[0])

counts[maxCount].sort()
if len(counts[maxCount]) == 1:
    print(counts[maxCount][0])
else:
    print(counts[maxCount][1])

# 범위
print(max(numbers) - min(numbers))