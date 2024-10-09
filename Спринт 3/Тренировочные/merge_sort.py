# Сортировка слиянием
# Гоше дали задание написать красивую сортировку слиянием. Поэтому Гоше обязательно надо реализовать отдельно функцию merge и функцию merge_sort.
# Реализуйте эти две функции.


def merge(arr, lf, mid, rg):
    arr_merg = []
    left = arr[lf:mid]
    right = arr[mid:rg]
    l, r = 0, 0
    while (l < len(left)) & (r < len(right)):
        if left[l] <= right[r]:
            arr_merg.append(left[l])
            l += 1
        else:
            arr_merg.append(right[r])
            r += 1
    while l < len(left):
        arr_merg.append(left[l])
        l += 1
    while r < len(right):
        arr_merg.append(right[r])
        r += 1
    return arr_merg


def merge_sort(arr, lf, rg):
    if len(arr) == 1:
        return arr
    else:
        mid = (rg - lf) // 2
        left = arr[lf:mid]
        merge_sort(left, 0, len(left))
        right = arr[mid:rg]
        merge_sort(right, 0, len(right))
        arr[lf:rg] = merge(left+right, 0, mid, len(arr))
        