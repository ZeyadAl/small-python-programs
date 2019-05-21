'''
This is inspired by a youtube video (https://www.youtube.com/watch?v=QPZ0pIK_wsc)
based on a article suggests a test for hiring programmers
by asking them to write this program
'''
import time
t1= time.time()
i=1
for i in range(1,101):
    if i%3==0 and i%5==0 :
        print ("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print ("Buzz")
    else :
        print(i)
t2 = time.time()
print (t2-t1)
int()
    
'''
#you can change
for i in range(1,101)
by
while i<101:
and then add at the end
i+=1

I imported the time module to find which way is faster
it seems like they are pretty much the same speed
'''

#actully there is a better way of doing it
'''
output =''
for i in range(1,101):
    if i%3==0: output += 'Fizz'
    if i%5==0: output += 'Buzz'

    if output=='': output+= str(i)
    print (output)
    output=''
'''
