def print_sums(sums, m, n):
    for i in range(m):
        print(i)
        for j in range(n):
            print(sums[i][j], end=" ")
        print("\n")

def get_subsets(sums, m, n, sum):

    # for i in range(sum, -1, -1):
    #     for j in range(n-1, -1, -1):
    #         print(" ")

    j=n-1
    i=sum

    while j>0:
        print("*", i, j)
        if sums[i][j] == sums[i][j-1]:
            j-=1
        else:
            print(set[j])
            print (set[j], get_subsets(sums, i-set[j]+1, n, sum-set[j]))




def subset_sum(set, sum):
    sums = [[0 for i in range(len(set))] for j in range(sum+1)]

    for i in range(len(set)):
        sums[0][i]=1

    for i in range(1, sum+1):
        for j in range(0, len(set)):
            if i-set[j]>=0:
                if j-1>=0:
                    sums[i][j] = sums[i][j-1] + sums[i-set[j]][j]
                else:
                    sums[i][j] = sums[i-set[j]][j]
            else:
                sums[i][j] = sums[i][j-1]
    print_sums(sums, sum+1, len(set))
    if sums[-1][-1]:
        print("Number of ways of getting the sum is ", sums[-1][-1])
    else:
        print("Sum not possible")

    get_subsets(sums, sum+1, len(set), sum)


set = [3, 34, 4, 12, 5, 2]
sum = 17

subset_sum(set, sum)