# 백준11721

word = input()

for i in range(len(word)):
    line = word[(i * 10):(i * 10 + 10)]
    print(line)
