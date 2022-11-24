def calcFuncWrite():
    newFuncWriter = open('calcFunc.py','w')
    calcFunctxt = open('calcFunc.txt', 'r')
    calcFunctxt = calcFunctxt.read()
    newFuncWriter.writelines(calcFunctxt)
    newFuncWriter.close()