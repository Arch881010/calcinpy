#This File contains all 'Functions'.
import os
def clear():
    os.system('cls')
import math
cache = '0'

def startup():
    while(True):
        print("Type only the letters provided to trigger that type.")
        print("s - Subtract. a - Add. m - Multiply. d - Divide. p - Power to. sq - Square root.")
        command = input("Enter a command -> ")
        if (command == 'a'):
            add()
        elif (command == 's'):
            sub()
        elif (command == 'm'):
            mul()
        elif (command =='d'):
            div()
        elif (command =='p'):
            power()
        elif (command == 'sq'):
            squareroot()
        elif (command == 'end'):
            return False
        elif (command == 'update'):
            from calcFuncWriter import calcFuncWrite
            calcFuncWrite()
            clear()
            print("Updated functions.")
        elif(command == ''):
            clear()
        else:
            clear()
            print("Invalid Command.")
def add():
    clear()
    one = int(input("What is the first number being from? "))
    two = int(input("What is the second number thats adding to the first? "))
    try:
        cache = one+two
    except:
        cache = "ERROR; Please use only numbers."
    os.system('cls')
    print(cache,"is the answer.")
    return cache
def sub():
    clear()
    one = int(input("What is the first number being subtracted from? "))
    two = int(input("What is the second number? The number subtracting the first. "))
    try:
        cache = one-two
    except:
        cache = "ERROR; Please use only numbers."
    clear()
    print(cache,"is the answer.")
def mul():
    clear()
    one = int(input("What is the first number?"))
    two = int(input("What is the second number?"))
    try:
        cache = one*two
    except:
        cache = "ERROR; Please use only numbers."
    clear()
    print(cache, 'is your answer.')
def div():
    clear()
    one = int(input("What is the first number? First/Second"))
    two = int(input("What is the second number?"))
    try:
        cache = one/two
    except:
        cache="ERROR; Please use only numbers."
    clear()
    print(cache, 'is your answer.')
def power():
    clear()
    one = int(input("What is the number being towards the power to? First^Second "))
    two = int(input("What is the second number to the power of? "))
    try:
        cache = power(one, two)
    except:
        cache="ERROR; Please use only numbers."
    clear()
    print(cache, 'is your answer.')
def squareroot():
    clear()
    one = int(input("What is the number being squarerooted? "))    
    try:
        cache = math.isqrt(one)
        cache = ("~"+str(cache))
    except:
        cache="ERROR; Please use only numbers."
    clear()
    print(cache,'is your answer.')
    