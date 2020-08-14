# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/sum-it-if-you-can-4867f851/

number = list(input())

S = 0

try:
    for i in range(len(number)):
        S = S + ((i+1)*int(number[i]))

except:
    print("Index out of bound...")

finally:
    if(len(number) != 10):
        print("Illegal ISBN")
    else:
        if(S%11 != 0):
            print("Illegal ISBN")
        else:
            print("Legal ISBN")