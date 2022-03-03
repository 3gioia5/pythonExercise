# 팰린드롬 판별기

def is_palindrome(word):
    for left in range(len(word)):
        right = len(word) - 1 - left
    if word[left] != word[right]:
        return False
    return True

# 테스트
print(is_palindrome('토마토'))
print(is_palindrome('racecar'))
print(is_palindrome('potter'))