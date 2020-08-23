# https://www.hackerearth.com/problem/algorithm/children-love-candies/

Q = int(input())

for q in range(Q):
    N, T = map(int, input().split())
    for t in range(T):
        if(N%2 == 0):
            N = N - (N/2)
        else:
            N = N - (N+1)/2
        N = N - N//4

    print(int(N))