'''
You are given a list of lists and elements and you want to keep all the elements (even the one inside the lists)
but they all should be in one list
'''
#x= lambda a: a+1
#lst[i][j] for j in range(len(lst[i])) for i in range(len(lst))]
#lst2=[[4,5,6], 7, [7]]
#fl= lambda a: a
#print (fl(lst2))
lst=[[4,3,2],3,4,5,[4]]
def f(lst):
    lst_fl=[]
    for i in range(len(lst)):
        try:
            for j in range (len(lst[i])):
                lst_fl.append(lst[i][j])
        except:
            lst_fl.append(lst[i])
    return lst_fl
            
