# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/bricks-game-5140869d/

bricks = int(input())

result = ""

round = 1

try:
    while(bricks>0):
        bricks = bricks - round
        if(bricks<1):
            result = "Patlu"
            break
        if(bricks <= round*2):
            result = "Motu"
            break
        bricks = bricks - (2*round)
        round += 1

except:
    print("Error.....")

finally:
    print(result)