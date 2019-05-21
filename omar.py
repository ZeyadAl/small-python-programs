# calculate the number of vowels in a given file
word=""
fi ="/Users/zeyad/Desktop/big_data.txt"
f=open(fi)
for line in f:
    word+=line
    
def main():
    Vowels = 0
    i = 0
    list1= ["o", "a", "i", "e", "u", "O", "A", "I", "E", "U"]
    while i < len(word):
        if word[i] in list1:
            Vowels += 1
        i+=1
    print('Number of vowels is: ' + str(Vowels))
main()

