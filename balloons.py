# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/mojtaba-prepares-contest-29b2a044/


T = int(input())

for t in range(T):

    l1 = list(map(int, input().split()))
    cost_green = l1[0]
    cost_purple = l1[1]

    cost1 = 0
    cost2 = 0

    n = int(input())

    array1 = []
    array2 = []

    for i in range(n):
        l = list(map(int, input().split()))
        array1.append(l[0])
        array2.append(l[1])

    try:
        for index in range(n):
            cost1 += (array1[index]*cost_green) + (array2[index]*cost_purple)
            cost2 += (array2[index] * cost_green) + (array1[index] * cost_purple)

    except:
        print("Error!!!!")

    finally:
        if(cost1 < cost2):
            print(cost1)
        else:
            print(cost2)