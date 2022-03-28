# 백준2744

word = input()
ans = []

for i in word:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        ans.append(i.upper())
    else:
        ans.append(i.lower())

for i in ans:
    print(i, end='')
