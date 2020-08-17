# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/arithmetic-progression-1-81131fa7/

T = int(input())

for t in range(T):
    numbers = list(map(int, input().split()))
    A = numbers[0]
    B = numbers[1]
    C = numbers[2]

    d1 = (B-A)
    d2 = (C-B)

    diff = 0

    try:
        diff = abs(d1-d2)
    except:
        print("error....")
    finally:
        if(diff%2 == 0):
            print(int(diff/2))
        else:
            print(int(diff/2)+1)