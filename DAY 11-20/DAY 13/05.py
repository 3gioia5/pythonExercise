# 백준10833

n = int(input())
remainder = 0

for i in range(n):
    student, apple = map(int, input().split())
    remainder += (apple % student)

print(remainder)
