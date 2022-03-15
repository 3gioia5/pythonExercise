# 백준2475

numbers = list(map(int, input().split()))
final_number = 0

for i in numbers:
    final_number += i * i

print(final_number % 10)