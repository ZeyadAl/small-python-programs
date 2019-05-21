'''
You are given a list of numbers and you want to find
the max sum of 2 consecutive elements in the list
'''
list1=[3,4,2,5,4,6,1,1,2]
list2=[]
def ma(lst):
    for i in range(len(list1)-1):
        list2.append(list1[i]+list1[i+1])
    return max(list2)
