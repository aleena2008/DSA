#To rotate an array arr in direction left/right n times  ------------------------------------------------------------------------------------------------------------------

def rotate(arr, dir, n):
    arr = arr.split()
    n = n%len(arr)
    
    rot = []
    if (dir=='l'):
        rot = arr[n:] + arr[:n]
    elif (dir=='r'):
        rot = arr[len(arr)-n:] + arr[:len(arr)-n]
    else:
        print("Invalid")

    rot = " ".join(rot)
    return rot

# arr = input("Enter array: ")
# dir = input("Enter left or right(l/r): ")
# n = int(input("Enter number of rotations: "))

# print("Rotated array: ", rotate(arr, dir, n))

# Swap two numbers ------------------------------------------------------------------------------------------------------------------------------------------------------------

def swap (a, b):
    print("swapping", a, b)
    temp = b
    b = a
    a = temp
    return (a, b)

# Sort an array -----------------------------------------------------------------------------------------------------------------------------------------------------------

def sort(arr):
    print("sorting")
    n = len(arr)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if(arr[j]<arr[min]):
                min=j
            arr[min], arr[i] = swap(arr[min], arr[i])
    return arr

# Re-arrange an array such that arr[i]=i -------------------------------------------------------------------------------------------------------------------------------------------

def arrange(arr):
    print("ärranging")
    i=0
    while (i<len(arr)):
        if(arr[i]==i) or (arr[i]==-1):
            print("arr[i] equal to", i)
            i+=1
        elif (arr[i] != i) & (arr[i] != -1):
            print("before", i, arr[i], arr[arr[i]])
            # (arr[i], arr[arr[i]]) = swap(arr[i], arr[arr[i]])
            temp = arr[i]
            arr[i] = arr[arr[i]]
            arr[temp] = temp
            # arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
            print("swapped", arr[i], arr[arr[i]], arr)
        else:
            i+=1

                
# Rearrange positive and negative numbers in O(n) time and O(1) extra space -------------------------------------------------------------------------------------------------------

def alternate_pos_neg(arr):
    print("alternate_pos_neg")
    pos=0
    for i in range(len(arr)):
        if (arr[i]<0):
            arr[i], arr[pos] = arr[pos], arr[i]
            pos+=1
    if (pos>len(arr)-pos):
        arr = arr[::-1]
        pos = len(arr)-pos

    
    j = pos if (pos%2!=0) else pos+1
      
    i=0
    while i<pos:
        arr[i], arr[j] = arr[j], arr[i] 
        i+=2
        j+=2
        
    print(arr)    

    return

# Reorder an array according to given indexes

    # 50  40  70  60  90
    # 3   0   4    1   2

    # swap from index array
    # take index[i] t correct place

    # 60  40  70  50  90
    # 1   0    4   3  2

    # 40  60  70  50  90
    # 0    1   4   3   2

    # 40  60  90  50  70
    # 0    1   2   3   4

def arrange_index(arr, index):
    ptr = 0
    for i in range(len(index)):
        print("before", i, arr, index)
        if (i!=index[i]):
            arr[index[i]], arr[i] = arr[i], arr[index[i]] 
            print(index[i], index[index[i]])
            t = index[i]
            index[i] = index[index[i]]
            index[t] = t
            # index[i], i = i, index[i]
            print("after", arr, index)

# arr = input("Enter array: ")
# arr = [eval(i) for i in arr.split()]

# index = input("Enter index array")
# index = [eval(i) for i in index.split()]


# Getting pivot element ------------------------------------------------------------------------------------------------------------------------------------

def get_pivot(arr):
    print("getting pivot")
    n = len(arr)
    low = 0
    high = n-1
    
    while (low<high):
        mid = int(low + (high-low)/2)

        if mid==low:
            return mid
        if mid==high:
            return mid+1
        if (arr[mid]<arr[low]): 
            if arr[mid-1]>=arr[mid]:
                return mid
            else:
                high = mid-1
        elif (arr[mid]>arr[low]):
            if arr[mid+1]<=arr[mid]:
                return mid+1
            else:
                low = mid+1

    if (high==low and low==mid):
        return mid  
    return 0

# Binary Search -----------------------------------------------------------------------------------------------------------------------------------

def binary_search(arr, key):
    print("binary searching", arr, key)
    n = len(arr)
    low = 0
    high = n-1
    
    while (low<=high):
        mid = int(low + (high-low)/2)

        if (arr[mid]==key):
            return mid
        elif (arr[mid]>key):
            high = mid-1
        else:
            low = mid+1

# Search an element in a sorted and rotated array --------------------------------------------------------------------------------------------------------------------------------

def search_sorted_rotated(arr, key):
    print("search in sorted rotated")
    pivot = get_pivot(arr)
    print("pivot", pivot)
    if key<=arr[-1]:
        arr = arr[pivot:]
        index = pivot + binary_search(arr, key)
    else:
        arr = arr[:pivot]
        index = binary_search(arr, key)
    print(index)

# arr = input("Enter array: ")
# arr = [eval(i) for i in arr.split()]
# elt = int(input("Enter key: "))

# Find the Rotation Count in Rotated Sorted array --------------------------------------------------------------------------------------------------------------------------

def rotation_count(arr):
    count = get_pivot(arr)
    print(count)

# K-th Largest Sum Contiguous Subarray ----------------------------------------------------------------------------------------------------------------------------------

def Kth_largest_sum(arr, k):
    n = len(arr)
    sum = [[arr[0]]]
    for i in range(1, n):
        print(i)
        # for _ in range(i):
        sum.append([0]*i)
        sum[i].append(arr[i])
    print(sum)
    for i in range(n):
        for j in range(i+1, n):
            print("i, j", i, j)
            if (j>i):
                print("&&&", i, j-1)
                print(sum[i][j-1]+ arr[j])

                sum[i].append(sum[i][j-1]+arr[j])
                print(sum)
            print(sum)
    print("\n\n\nfinal", sum)

    sums = []
    for i in range(n):
        for j in range(i, n):
            sums.append(sum[i][j])
    sums.sort()
    print(sums, len(sums)-k)
    print(sums[len(sums)-k])

    
    return

import time


# arr = [eval(i) for i in arr.split()]
# k = int(input("Enter k : "))

# t=time.time()

# dic = dict()

# for i in arr:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i] = 1


# dic = sorted(dic.items(), key=lambda x:x[1])
# dic = (dic[len(dic)-k:])
# for x,y in dic:
#     print(x)

# print(time.time()-t)

import time

def K_most_frequent(arr, k):
    arr = [1, 2, 2, 3, 3, 3]
    k = 2
    t = time.time()
    dic = dict()

    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    dic = sorted(dic.items(), key=lambda kv: kv[1])

    for i in range(len(dic) - 1, len(dic) - k - 1, -1):
        print(dic[i][0])
    
    
arr = input("Enter array: ")
arr = [eval(i) for i in arr.split()]
k = int(input("Enter k : "))

K_most_frequent(arr, k)

