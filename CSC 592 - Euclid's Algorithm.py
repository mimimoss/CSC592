#ask user for input of two numbers
firstNumber = int(input("Please enter a number: "))
secondNumber = int(input("Please enter another number: "))

#make table headers
i = 0
index = str("i")
q = str("q")
m = str("m")
n = str("n")
r = str("r")
print(f"{index:>5}|{q:>5}{m:>5}{n:>5}{r:>5}")
print(" ----------------------------")

#swap the numbers if the first number input is smaller than the second
if firstNumber < secondNumber:
    (firstNumber,secondNumber) = (secondNumber,firstNumber)

#if the second number does not equal 0 loop
while secondNumber != 0:
    #mod
    remainder = firstNumber%secondNumber
    #how many times the second number goes into the first, rounding down if there is a remainder
    floorDivision = firstNumber//secondNumber
    #euclids algorithm
    firstNumber = floorDivision * secondNumber + remainder
    #fill the table
    i = i+1
    print(f"{i:>5}|{floorDivision:>5}{firstNumber:>5}{secondNumber:>5}{remainder:>5}")
    #put the second number where the first number was
    firstNumber = secondNumber
    #put the remainder where the second number was
    secondNumber = remainder
    
print("The greatest common denominator is:", firstNumber)
    

