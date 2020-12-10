
import math
import numpy as np

choices = ["1) Algebra", "2) Discrete"]
for x in choices:
    print(x)

choice = input("\nWhat kind of operation do you want to do? ")

def algebra():
    choices = ["\n1) Linear Equations", "2) Factorization"]
    msg ="What kind of algebraic equation do you want to solve?"

    for x in choices:
        print(x)

    kind_of = input("\nWhat kind of algebraic equation do you want to solve? ")

    if kind_of == "1":
        print("".center(len(msg), "-"))
        x = int(input("What is the value of the first x? "))
        x1 = int(input("What is the value of the second x? "))

        y = int(input("What is the value of the first y? "))
        y1 = int(input("What is the value of the second y? "))

        c = int(input("What is the value of the constant in the first equation? "))
        c1 = int(input("What is the value of the constant in the second equation? "))

        A = np.array([[x,y], [x1,y1]])
        #This will create a new array(similar to a list).
        b = np.array([c,c1])
        z = np.linalg.solve(A,b)

        print(z)
        
    elif kind_of == "Factorization":
        pass

def discrete():
    pass

if choice == "1":
    algebra()