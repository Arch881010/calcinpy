#This File contains all 'Functions'.
import os
def clear():
    os.system('cls')

cache = '0'

def startup():
    while(True):
        print("Type only the letters provided to trigger that type.")
        print("s - Subtract. a - Add. m - Multiply. d - Divide. p - Power to. sq - Square root.")
        print("Adding a 'c' in front of any uses the cached number from the previous answer.")
        command = input("Enter a command -> ")
        if (command == 'a'):
            add()
        elif (command == 's'):
            sub()
        elif (command == 'end'):
            return False
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
