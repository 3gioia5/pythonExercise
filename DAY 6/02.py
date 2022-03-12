# 백준4673
# 내가 유도했지만 사용할 수 없던 식: n + (n // 10) + (n % 10)

natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)
