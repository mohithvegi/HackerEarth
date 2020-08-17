# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/a-movement-1/

N = int(input())

position = N
steps = 0

try:
    while(position > 0):
        if(position >= 5):
            position = position-5
            steps += 1
        elif(position == 4):
            position = position-4
            steps += 1
        elif(position == 3):
            position = position-3
            steps += 1
        elif(position == 2):
            position = position-2
            steps += 1
        elif(position == 1):
            position = position-1
            steps += 1

except:
    print("Error....")

finally:
    print(steps)