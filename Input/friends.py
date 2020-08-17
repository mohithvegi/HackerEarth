# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/friends-relationship-1/

def pattern(N):
    lines = []
    for i in range(N):
        r = ""
        for i1 in range(i+1):
            r += '*'
        for i2 in range(2*(N-i-1)):
            r += '#'
        for i3 in range(i+1):
            r += '*'

        lines.append(r)

    return lines


if __name__ == '__main__':

    T = int(input())
    for t in range(T):
        N = int(input())
        lines = pattern(N)

        try:
            for line in lines:
                print(line)
        except:
            print("something went wrong...")