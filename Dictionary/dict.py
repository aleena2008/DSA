import collections

# Sum of all items in a dictionary ------------------------------------------------------------------------------------------------------------------------------------------

def sum_of_dict(dict):
    sum = 0
    for i in dict:
        sum+=dict[i]
    return sum

# Find common elements in three sorted arrays by dictionary intersection -----------------------------------------------------------------------------------------------------------------

def common_elts(arr1, arr2, arr3):
    dict = collections.defaultdict(lambda:None)
    common=[]
    for i in arr1:
        dict[i]="Present"
    for i in arr2:
        if (dict[i]):
            dict[i]="Present2"
    for i in arr3:
        if (dict[i]=="Present2"):
            common.append(i)
    return common

# Key with maximum unique values ----------------------------------------------------------------------------------------------------------------------------------------------

def max_unique_values(dic):
    print("Max unique values")
    unique = 0
    unique_key = None
    for i in dic.keys():
        temp = 0
        temp = dict()
        un = 0
        for j in dic[i]:
            if (temp.get(j)==None):
                un+=1
                temp[j]=1
        if un>unique:
            unique = un
            unique_key = i
    return unique_key

# Count characters in string ---------------------------------------------------------------------------------------------------------------------------------------------------------

def count_chars(strng):
    dic = collections.defaultdict(lambda:0)
    for i in strng:
        dic[i]+=1
    
    # dic contains list of all chars and frequency

    x = list(filter(lambda x: dic[x]>1, dic.keys()))
    dic = sorted(dic.items(), key = lambda x:(x[1], x[0]))
    return dict(dic)

# Get dict with repeat characters as value ---------------------------------------------------------------------------------------------------------------------------------------------

def repeat_chars(strng):
    dic = collections.defaultdict(lambda:[])
    for i in strng:
        dic[i].append(i)
    return dict(dic)

# Replace String by Kth Dictionary value --------------------------------------------------------------------------------------------------------------------------------------

def replace_string(lst, dic, k):
    for i in range(len(lst)):
        if dic.get(lst[i])!=None:
            t = lst[i]
            lst[i] = dic[t][k]

    return (lst)


# Given String, replace it’s words from lookup dictionary. -------------------------------------------------------------------------------------------------------------------

def replace_lut(test_str, dic):
    lst = test_str.split(" ")
    for i in range(len(lst)):
        if dic.get(lst[i])!=None:
            lst[i] = dic[lst[i]]
    return (" ".join(lst))


# test_str = "geekforgeeks best for geeks"
# lut = {"geeks" : "all CS aspirants"} 


lst = [6,6,6,6,1,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5]
print(count_chars(lst))
