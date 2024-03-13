arr = [7, 3, 2, 6, 5, 56, 9, 98, 52]
arr1 = [5, 6, 3, 7, 9, 4, 15, 2, 78, 45]


def partition(arr, p, r):
    pivot = arr[p]
    i = p
    j = r
    while i <= j:
        if arr[i] > pivot:
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            i += 1
    arr[p], arr[j] = arr[j], arr[p]
    return arr, j


def quick_sort(arr, p, r):
    if p < r:
        arr, q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)
    return arr


arr = quick_sort(arr, 0, len(arr)-1)
print(arr)
