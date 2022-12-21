def get_max_gold(gold, n, m):
    collect_gold = [[0 for i in range(m+2)] for i in range(n+2)]
    print(collect_gold)

    for i in range(1,n+1):
        for j in range(1,m+1):
            collect_gold[i][j] = gold[i-1][j-1]
    print(collect_gold)

    for j in range(n-1,0,-1):
        for i in range(1, m+1):
            print(collect_gold[i][j])
            print('&&&', (collect_gold[i-1][j+1], collect_gold[i+1][j+1]))
            collect_gold[i][j] += max(collect_gold[i-1][j+1], collect_gold[i+1][j+1])

    print(collect_gold)






gold = [[1, 3, 3],
    [2, 1, 4],
    [0, 6, 4]]
 
m = 3
n = 3
get_max_gold(gold, n, m)