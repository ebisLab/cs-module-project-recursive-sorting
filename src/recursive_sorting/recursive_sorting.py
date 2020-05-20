# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    # base case
if len(arrA) == 0 or len(arrB) == 0:
    return arrA+arrB
elif not len(arrA) == 0 or not len(arrB) == 0:
    # return arrA + arrB

    a = 0  # smallest index of a
    b = 0  # smallest index of b
    lenA = len(arrA)
    for i in range(elements):
        if a = lenA:
            merged_arr[i] = arrB[b]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # for i in range(len(arr)):
    # merge_sort(arr, 0, len(arr)-1)  # arra, start index, and ending index

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    L = arr[start:mid]
    R = arr[mid:end]
    L.append(len(arr))
    R.append(len(arr))
    i = j = 0

    for k in range(start, end+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
