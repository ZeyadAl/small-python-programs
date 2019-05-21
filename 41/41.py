#Function that determines if the number is prime or not
def Prime_or_not(n):
    if n==1:
        print(n, 'is NOT a prime number')
    else:
        if n%2==0:
            if n==2:
                print(n, 'is a prime number')
            else:
                print(n, 'is NOT a prime number')
        else:
            for i in range(3,x,2):
                if n%i==0:
                    print(n, 'is NOT a prime number')
                    return
            print(n, 'is a prime number')
#The numbers in the list are what you get when you subtitute the numbers 1to41 in the equation x**2-x+41
a= int(input('choose the first number '))
b= int(input('choose the last number '))
l=[]
for i in range(a, b+1):
    m= i**2-i+41
    l.append(m)
for n in l:
    x= int(n**(1/2))+1
    Prime_or_not(n)

y= input()
