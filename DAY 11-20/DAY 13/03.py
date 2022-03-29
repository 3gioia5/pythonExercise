# 선형탐색 구현해 보기

def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
    return None

element = int(input())
some_list = list(map(int, input().split(", ")))

print(linear_search(element, some_list))
