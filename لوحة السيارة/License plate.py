'''
This Python program is used to output all the possibilities for the license plate of a car.
The story is basically that my friend got hit by a car and the driver flied away.
My friend only memorized parts of the license plate. He called me to know what are
the possible outcomes. I gave him a list of all the possibilities using this program.
'''

'''
This was used to make list2 but it's no longer needed and it takes time
that can be utilized
list1 = []
x= 'ABJDRSXTEGKLZNHUV'
for i in range(0,17):
    list1.append(x[i])
'''
list2=['A', 'B', 'J', 'D', 'R', 'S', 'X', 'T', 'E',
       'G', 'K', 'L', 'Z', 'N', 'H', 'U', 'V']

for i in range(0,10):
    for j in range(0,10):
        for m in list2:
            print(m, 'K J', '  ', '4', str(i), str(j), '9')
