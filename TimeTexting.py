'''
This program is used to estimate the texting time with someone over WhatsApp. The program needs the exported chat file (you need the time to be 24h not 12h). The program calculates the time differences between each 2 consecutive messages and if it's at least one the program counts that as a minute of texting. The program can be improved in terms of writing style and other things.
'''
chat=input("Enter the path of the chat file: ")
file=open(chat)

store=[]
store1=[]
store2=[]
store3=[]
for line in file:
    
    if line[0]=='[':
        
        list1=line.split(']')
        store.append(list1[0])

for line in store:
    list1=line.split(' ')
    store1.append(list1[1])

for line in store1:
    list1=line.split(':')
    store2.append(list1[1])

T=0
for line in store2:
    store3.append(int(line))
for i in range(len(store)-1):
    if store3[i+1]-store3[i]==1:
        T+=1

print("The estimated texting time is", str(T), "min")

'''
outF=open(chat, 'w')
outF.write("The estimated texting time is:", str(T), "min")
outF.close()
print('Done!')
'''
