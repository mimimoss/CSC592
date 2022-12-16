import random

#randomly output 5 numbers
def numberGenerator():
    i = 0
    while i < 5:
        randomBit = f'{random.getrandbits(32):=032b}'
        
        if i == 0:
            b1 = randomBit
            b1Last = int(str(b1)[-1])
            print('b1 | ',randomBit,' | ',b1Last)
        elif i == 1:
            b2 = randomBit
            b2Last = int(str(b2)[-1])
            print('b2 | ',randomBit,' | ',b2Last)
        elif i == 2:
            b3 = randomBit
            b3Last = int(str(b3)[-1])
            print('b3 | ',randomBit,' | ',b3Last)
        elif i == 3:
            b4 = randomBit
            b4Last = int(str(b4)[-1])
            print('b4 | ',randomBit,' | ',b4Last)
        elif i == 4:
            b5 = randomBit
            b5Last = (str(b5)[-1])
            print('b5 | ',randomBit,' | ',b5Last)
        i = i + 1
        
    bitPrime = ('00000000000000000000000001' + str(b1Last) + str(b2Last) + str(b3Last) + str(b4Last) + b5Last + '1')
    numberPrime = int(bitPrime, 2)
    print('--------------------------------------------------')
    print('Number | ',numberPrime,' | ',bitPrime,'\n')
    
    return numberPrime

def isMillerRabinPassed(numberPrime):
    maxDivisionsByTwo = 0
    ec = numberPrime-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == numberPrime-1)
 
    def trialComposite(round_tester):
        if pow(round_tester, ec, numberPrime) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, numberPrime) == numberPrime-1:
                return False
        return True
 
    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, numberPrime)
        if trialComposite(round_tester):
            return False
    return True

def getPrimeNumber():
    number = numberGenerator()
    while True:
        if not isMillerRabinPassed(number):
            newNumber = number
            print(number, "is not a prime\n")
            getPrimeNumber()
            break
        else:
            global prime
            prime = number
            print(prime, "is perhaps a prime\n")
            break
    return prime

# function to find gcd
def gcd(a, b):
        while b:
                a, b = b, a%b
        return a

# function to find extended gcd
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

# function to find modular inverse
def modinv(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m
            
if __name__ == '__main__':
    m = 0
    while m < 2:
        if m < 1:
            firstPrime = getPrimeNumber()
        if m == 1:
            secondPrime = getPrimeNumber()
            if secondPrime == firstPrime:
                secondPrime = getPrimeNumber()
        m = m + 1
            
    if secondPrime > firstPrime:
        (firstPrime,secondPrime) = (secondPrime,firstPrime)

    print('--------------------------------------------------\n')
    print("your first prime is: ", firstPrime, "\nyour second prime is: ", secondPrime)
    n = firstPrime * secondPrime
    phi = (firstPrime-1)*(secondPrime-1)
    r = random.randint(2,100) # For efficiency 2 < e < 100
    while True:
            if gcd(r, phi) == 1:
                    break
            else:
                    r += 1
    e = r

    d = modinv(e, phi)
    print('p =', firstPrime,'| q =', secondPrime,'| n =', n,'| e =', e,'| d =', d)
    #conver to 32bit binary
    print('p =',f'{firstPrime:032b}')
    print('q =',f'{secondPrime:032b}')
    print('n =',f'{n:032b}')
    print('e =',f'{e:032b}')
    print('d =',f'{d:032b}')


