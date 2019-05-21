import turtle

my_1= turtle.Turtle()

def EQTri(x):
    my_1.forward(x)
    my_1.left(120)
    my_1.forward(x)
    my_1.left(120)
    my_1.forward(x)

def EQTRI(x):
    my_1.right(120)
    my_1.forward(x)
    my_1.right(120)
    my_1.forward(x)


    

EQTri(100)
EQTRI(100)

for i in range(3):
    my_1.forward(100)
    EQTRI(100)
EQTRI(100)
