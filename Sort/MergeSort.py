arr = [5, 6, 7, 3, 4, 2, 54, 32, 84, 31]


def merge(arr, s, mid, e):
    left = arr[s: mid+1]
    right = arr[mid+1: e+1]
    i = 0
    j = 0
    k = s
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1


def merge_sort(arr, s, e):
    if s < e:
        mid = (s+e)//2
        merge_sort(arr[s: mid], s, mid)
        merge_sort(arr[mid+1: e], mid+1, e)
        merge(arr, s, mid, e)


merge_sort(arr, 0, len(arr)-1)
print(arr)
