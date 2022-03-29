# 선택정렬 구현

def selection_sort(list):
    for i in range(len(list) - 1):
        min, min_index = list[i], i

        for j in range(i + 1, len(list)):
            if min > list[j]:
                min, min_index = list[j], j

        list[i], list[min_index] = min, list[i]

    return list

new_list = [3258, 342, 32, 64, 8, 19]
print(selection_sort(new_list))
