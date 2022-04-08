# 백준11948

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

science = [a, b, c, d]
society = [e, f]

print(sum(science) - min(science) + max(society))