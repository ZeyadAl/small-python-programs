def f(n):
    x= int(n**(1/2))+1
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
while True:
    n= int(input('Type in a positive intger '))
    f(n)
