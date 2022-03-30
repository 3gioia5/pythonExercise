# 백준10987

word = input()
ans = 0

for i in word:
    if i in 'aeiou':
        ans += 1

print(ans)
