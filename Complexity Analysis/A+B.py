# https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/practice-problems/algorithm/a-b-4/

while(True):
    try:
        numbers = list(map(int, input().split()))
        print(sum(numbers))
    except EOFError:
        break