# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/split-house-547be0e9/

N = int(input())

sequence = list(input())

flag = False

try:
    for i in range(N-1):
        if(sequence[i]=='H' and sequence[i+1]=='H'):
            flag = True
            break
        elif(sequence[i]=='.'):
            sequence[i] = 'B'
    if(sequence[N-1] == '.'):
        sequence[N-1] = 'B'

except:
    print("Oops!!!")

finally:
    result = ""
    for c in sequence:
        result += c
    if(flag):
        print("NO")
    else:
        print("YES")
        print(result)