'''
you are given a string to find the greatest conssuctive string in it that 
'''

t='massachusetts'
a=t[0]
list1=[]
list2=[]
for i in range(len(t)-1):
    if t[i]>t[i+1]:
        list1.append(a)
        a=''
    else:
        a+=t[i+1]

for i in range(len(list1)):
    list2.append(len(list1[i]))
m=max(list2)
p=list2.index(m)
print(list1[p])
