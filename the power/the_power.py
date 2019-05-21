while(1>0):
    x=int(input('choose a number '))#choosing a number
    n=int(input('choose the power '))
    if n==1:
        print( str(x) + " is a number of the 1st power")
    else:
         if n==2:
             if (x**(1/2)==int(x**(1/2))):
                print( str(x) + " is a square number")
             else: print ( str(x) + ' is NOT a square number')
         else:
             if n==3:
                 if (x**(1/3)==int(x**(1/3))):
                    print( str(x) + " is a cube number")
                 else: print ( str(x) + ' is NOT a cube number')
             else:
                if (x**(1/n)==int(x**(1/n))):
                    print (str(x) + ' is a number of the '+ str(n)+'th power')
                else: print ( str(x) + ' is NOT a number of the '+ str(n)+'th power')


    


