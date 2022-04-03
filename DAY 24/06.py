# 백준11557

t = int(input())
s = dict()

for _ in range(t):
    for i in range(int(input())):
        school, alcohol = map(str, input().split())
        alcohol = int(alcohol)

        s[school] = alcohol

    m = max(s.values())
    reverse_s = dict(map(reversed, s.items()))
    print(reverse_s[m])
