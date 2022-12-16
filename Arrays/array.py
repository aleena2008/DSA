#To rotate an array arr in direction left/right n times

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


arr = input("Enter array: ")
dir = input("Enter left or right(l/r): ")
n = int(input("Enter number of rotations: "))


print("Rotated array: ", rotate(arr, dir, n))