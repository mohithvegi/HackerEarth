# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/magical-word/

import math

primes = [37, 41, 43, 47, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

def checkPrime(N):

    count=0
    if(N==2 or N==3):
        return True
    else:
        for i in range(2, int(math.sqrt(N))+1):
            if(N%i == 0):
                count += 1
                break
    if count>0:
        return False
    else:
        return True

def nearestPrime(number, primes):
    length = len(primes)
    if(primes[0] > number):
        return primes[0]
    elif(primes[length-1] < number):
        return primes[length-1]
    else:
        for i in range(length-1):
            if(number>primes[i] and number<primes[i+1]):
                d1 = number - primes[i]
                d2 = primes[i+1] - number
                if(d1 <= d2):
                    return primes[i]
                else:
                    return primes[i+1]

if __name__ == '__main__':

    T = int(input())
    for t in range(T):
        N = int(input())
        string = list(input())

        for index in range(N):
            character = string[index]
            asci = ord(character)
            if not checkPrime(asci):
                primeAscii = nearestPrime(asci, primes)
                primeCharacter = chr(primeAscii)
                if not primeCharacter.isalpha():
                    if asci<65:
                        string[index] = 'C'
                    elif asci>122:
                        string[index] = 'q'
                else:
                    string[index] = primeCharacter
            else:
                if asci<65:
                    string[index] = 'C'
                elif asci>122:
                    string[index] = 'q'

        result = ""
        for s in string:
            result += s

        print(result)