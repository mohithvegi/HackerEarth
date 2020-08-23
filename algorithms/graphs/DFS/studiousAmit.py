# https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/studious-amit-and-his-last-semester-b1fd76ee/submissions/

T = int(input())

for t in range(T):
    courses = {}
    visited = []
    N, M = map(int, input().split())
    for i in range(N):
        courses[i + 1] = -1
        visited.append(i + 1)
    for m in range(M):
        u, v = map(int, input().split())
        courses[u] = v

    count = 0
    flag = False

    for c1 in courses:
        c2 = courses[c1]
        if c2 in courses:
            if courses[c2] == c1:
                flag = True
                break

    if (flag):
        print(0)
    else:
        print(1)