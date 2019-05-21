chat='/Users/zeyad/Desktop/calculate_texting_time/T.txt' #the chat file
save='/Users/zeyad/Desktop/calculate_texting_time/Tm.txt' #file to write TimeStamps
file=open(chat) 
outF=open(save, 'w')
store=[]
for line in file:
    list1=line.split(':')
    store.append(list1[1])
for line in store:
  # write TimeStamp to output file
  outF.write(line)
  outF.write("\n")
outF.close()

print('دن')
