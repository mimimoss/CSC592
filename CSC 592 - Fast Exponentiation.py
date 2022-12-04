#Implement the following pseudocode known as fast exponentiation algorithm and share your GitHub code.

#get the inputs from the user
def main():
    e = int(input("Enter exponent: "))
    x = int(input("Enter base: "))
    n = e-1
    #grid()
    expMod(x, e, n)

#perform exponentiation algorithm
def expMod(x, e, n):
    binary = bin(e)[2:]
    y = x
    
    #for each binary in the exponent given perform equation
    for i in range(len(binary)):
        y = (y * y) % n

        #if the binary equals 1 multiply y by the base given
        if binary[i] == '1':
            y = (y * y) % n
    print(y)

#make grid
##def grid():
##    index = str("i")
##    binary = str("binary")
##    squaringy = str("squaring y")
##    multiplyingy = str("multiplying y")
##    print(f"{index:>5}|{binary:>5}{squaringy:>5}{multiplyingy:>5}")
        

if __name__ == "__main__":
    main()
