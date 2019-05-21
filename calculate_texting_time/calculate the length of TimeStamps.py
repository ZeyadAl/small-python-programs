chat='/Users/zeyad/Desktop/test2.txt'
file=open(chat)
lengthOfTimeStamps=[]
for line in file:
    lengthOfTimeStamps.append(len(line))
print(len(set(lengthOfTimeStamps)))

print('دن')
