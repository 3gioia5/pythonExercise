# 백준2577

A = int(input())
B = int(input())
C = int(input())

new_number = list(str(A * B * C))

answer = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in new_number:
    answer[int(i)] += 1
for ans in answer:
    print(ans)
