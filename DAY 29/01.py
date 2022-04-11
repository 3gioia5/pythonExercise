# 백준18406

n = list(input())
front = n[:len(n) // 2]
back = n[len(n) // 2:]

sum_f = 0
sum_b = 0
for i in range(len(front)):
    sum_f += int(front[i])
    sum_b += int(back[i])

if sum_f == sum_b:
    print("LUCKY")
else:
    print("READY")
