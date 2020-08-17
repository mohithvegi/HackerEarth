# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cartag-948c2b02/

word = list(input())

vowels = ['A','E','I','O','U','Y']

result = "valid"

# DDXDDD-DD

try:
    c = word[2]
    if c in vowels:
        result = "invalid"
    else:
        n1 = int(word[0])
        n2 = int(word[1])
        n3 = int(word[3])
        n4 = int(word[4])
        n5 = int(word[5])
        n6 = int(word[7])
        n7 = int(word[8])
        condition1 = (n1+n2)%2
        condition2 = (n3+n4)%2
        condition3 = (n4+n5)%2
        condition4 = (n6+n7)%2
        if((condition1 != 0) or (condition2 != 0) or (condition3 != 0) or (condition4 != 0)):
            result = 'invalid'

except:
    print("Error..")

finally:
    print(result)