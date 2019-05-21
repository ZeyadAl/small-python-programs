chat='/Users/zeyad/Desktop/calculate_texting_time/_t.txt' #the chat file
save='/Users/zeyad/Desktop/calculate_texting_time/_T1.txt' #file to write TimeStamps
file=open(chat) 
outF=open(save, 'w')
store=[]
for line in file:
    #read the lines that start with '['
    if line[0]=='[':
        #storing TimeStamp only
        list1=line.split(']')
        store.append(list1[0])
for line in store:
  # write TimeStamp to output file
  outF.write(line)
  outF.write("\n")
outF.close()

print('دن')
