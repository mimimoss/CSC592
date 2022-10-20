firstNumber = int(input("Please enter a number: "))
secondNumber = int(input("Please enter another number: "))
i = 0
index = str("i")
q = str("q")
m = str("m")
n = str("n")
r = str("r")
print(f"{index:>5}|{q:>5}{m:>5}{n:>5}{r:>5}")
print(" ----------------------------")

if firstNumber < secondNumber:
    (firstNumber,secondNumber) = (secondNumber,firstNumber)

while secondNumber != 0:
    remainder = firstNumber%secondNumber
    floorDivision = firstNumber//secondNumber
    firstNumber = floorDivision * secondNumber + remainder
    i = i+1
    print(f"{i:>5}|{floorDivision:>5}{firstNumber:>5}{secondNumber:>5}{remainder:>5}")
    firstNumber = secondNumber
    secondNumber = remainder
print("The greatest common denominator is:", firstNumber)
    

