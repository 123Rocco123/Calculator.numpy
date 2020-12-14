import math
import numpy as np
import sympy as sp

def start():
    choices = ["1) Algebra", "2) Discrete", "3) Calculus"]
    for x in choices:
        print(x)

    choice = input("\nWhat kind of operation do you want to do? ")
    
    if choice == "1":
        algebra()
    elif choice == "3":
        calculus()

def algebra():
    choices = ["\n1) Linear Equations", "2) Factorization"]
    msg ="What kind of algebraic equation do you want to solve?"

    for x in choices:
        print(x)

    kind_of = input("\nWhat kind of algebraic equation do you want to solve? ")

    if kind_of == "1":
        print("".center(len(msg), "-"))
        x = int(input("\nWhat is the value of the first x? "))
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
        
    elif kind_of == "2":
        poly = input("What is the largest power on a varaible in your polynomial? ")

        if poly == "2":
            print("".center(len(msg), "-"))
            x = int(input("\nWhat is the value of the squared variable? "))
            y = int(input("\nWhat is the value of the varaible? "))
            z = int(input("\nWhat is the value of the constant? "))

            r = int(input("\nWhat is the value of x? "))

            p = np.polyval([x,y,z], r)
            #This will create the polynomial
        elif poly == "3":
            print("".center(len(msg), "-"))
            r = int(input("\nWhat is the value of the cubed variable? "))
            x = int(input("\nWhat is the value of the squared variable? "))
            y = int(input("\nWhat is the value of the varaible? "))
            z = int(input("\nWhat is the value of the constant? "))

            q = int(input("\nWhat is the value of x? "))

            p = np.polyval([r,x,y,z], q)
        print("The answer was", p)

def calculus():
    choice = int(input("\nInsert the level of differentiation: "))
    #This will tell the differentiation attribute how many times the equation has to be differentiated. 
    x = sp.Symbol("x")
    #This states that "x" is a symbol rather than a string.

    print("Insert equation: ")
    equation = input()

    diffd_equ = (sp.diff(equation, x, choice))
    print(diffd_equ)

    with open("history.txt", "w") as history:
        history.write(str(diffd_equ))

def discrete():
    pass

start()