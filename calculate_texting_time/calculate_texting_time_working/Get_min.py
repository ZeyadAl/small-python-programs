chat='/Users/zeyad/Desktop/calculate_texting_time/Tm.txt' #the chat file
save='/Users/zeyad/Desktop/calculate_texting_time/Tim.txt' #file to write TimeStamps
file=open(chat) 
outF=open(save, 'w')
store=[]
T=0
for line in file:
    store.append(int(line))
for i in range(len(store)-1):
    if store[i+1]-store[i]==1:
        T+=1

outF.write(str(T))
outF.close()

print('دن')
