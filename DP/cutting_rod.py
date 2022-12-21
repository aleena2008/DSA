def cut_rod(arr, n):
    cut = [0]
    arr.insert(0,0)

    cut.append(arr[1])

    for i in range(2, n+1):
        best = max(arr[j]+cut[i-j] for j in range(i,0,-1))
        cut.append(best)
    print(cut[-1])

arr = [ 3,5,8,9,10,17,17,20 ]
size = len(arr)
cut_rod(arr, size)