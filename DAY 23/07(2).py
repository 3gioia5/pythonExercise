# 백준1225

a, b = input().split()
x = 0
y = 0

for i in range(len(a)):
    x += int(a[i])
for i in range(len(b)):
    y += int(b[i])

print(x * y)
