# 백준5597

total = list()

for a in range(1, 31):
    total.append(a)

for _ in range(28):
    submit = int(input())
    total.remove(submit)

total.sort()
for i in total:
    print(i)
