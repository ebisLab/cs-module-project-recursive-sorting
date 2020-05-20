# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # base case
    a = 0
    b = 0
    # this is where the merging happens

    for i in range(elements):
        # if you've gone through all the values in A --> you will store the rest of B
        if len(arrA) == a:  # read through everything in a
            merged_arr[i] = arrB[b]
            b += 1  # incremented the index
        elif len(arrB) == b:
            merged_arr[i] = arrA[a]
            a += 1
        # compare the current values where the pointer is at
        elif arrA[a] > arrB[b]:
            # overriding zero with the number
            merged_arr[i] = arrB[b]
            b += 1
        else:
            # overriding zero with the number
            merged_arr[i] = arrA[a]
            a += 1
        # keep track of where you're at list A and list B
        # take the first element of each list and compare them
            # increment the new element index
        # take the smallest number -> assign that --> merged_arr
        # what ever is left over take add it to the marged_arr


# elements steps
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # if lenght of array is greater than 1,-->
    if len(arr) > 1:
        # find middle
        mid = len(arr)//2
        # they will become 2 different arrays left, right
        # recursive merge_sort calls over and over until we get to 1 or base statement kicks in
        left = merge_sort(arr[0:mid])
        right = merge_sort(arr[mid:])
        # this is infinite until i reach one
        # merge things in the right order until recursive stops
        arr = merge(left, right)  # puts them in order

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
