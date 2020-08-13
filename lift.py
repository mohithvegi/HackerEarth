# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/lift-queries/

T = int(input())

queries = []

for t in range(T):
    N = int(input())
    queries.append(N)

result = []

liftB = 7
liftA = 0

try:
    for i in range(len(queries)):
        d1 = abs(liftB - queries[i])
        d2 = abs(queries[i] - liftA)

        if (d1 >= d2):
            liftA = queries[i]
            result.append('A')
        else:
            liftB = queries[i]
            result.append('B')

except:
    print("Something went wrong..")

finally:
    for i in result:
        print(i)