dic = dict()

for i in range(10):
    unique = 0
    unique_key = None
    for i in dic.keys():
        temp = dict()
        un = 0
        for j in dic[i]:
            if (temp.get(j)==None):
                un+=1
            else:
                temp[j]=1
        if un>unique:
            unique = un
            unique_key = i
        del(temp)