# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/e-maze-in-1aa4e2ac/

directions = list(input())

x = 0
y = 0
i=0

try:
    while(i<len(directions)):
        if(directions[i] == 'L'):
            x = x-1
        elif(directions[i] == 'R'):
            x = x+1
        elif (directions[i] == 'D'):
            y = y-1
        elif (directions[i] == 'U'):
            y = y+1
        i+=1

except:
    print("Error!!!")

finally:
    print(str(x) + " " + str(y))