# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/description/

T = int(input())

for t in range(T):
    seat = int(input())

    result = ""

    try:
        while(seat<=108):
            remainder = seat%12

            if(remainder == 1):
                result = str(seat+11) + " WS"
                break
            elif(remainder == 2):
                result = str(seat+9) + " MS"
                break
            elif (remainder == 3):
                result = str(seat+7) + " AS"
                break
            elif (remainder == 4):
                result = str(seat+5) + " AS"
                break
            elif (remainder == 5):
                result = str(seat+3) + " MS"
                break
            elif (remainder == 6):
                result = str(seat+1) + " WS"
                break
            elif (remainder == 7):
                result = str(seat-1) + " WS"
                break
            elif (remainder == 8):
                result = str(seat-3) + " MS"
                break
            elif (remainder == 9):
                result = str(seat-5) + " AS"
                break
            elif (remainder == 10):
                result = str(seat-7) + " AS"
                break
            elif (remainder == 11):
                result = str(seat-9) + " MS"
                break
            elif (remainder == 0):
                result = str(seat-11) + " WS"
                break
    except:
        print("Some error occured!")
    finally:
        print(result)