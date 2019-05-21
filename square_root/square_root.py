#first you need to start with a guess, g
import random
g= random.randint(1,1000)
#choose a number to find its root, say x
while (1>0):
        x= int(input('Choose a number '))
        while (g!=(g+x/g)/2):
                g=(g+x/g)/2
        print(g)
        print(x**(1/2))



        
#accuracy test number 7778899654120099
