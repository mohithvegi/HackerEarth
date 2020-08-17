# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/duration/

def duration(SH, SM, EH, EM):
    total_time = (60*EH + EM) - (60*SH + SM)
    return total_time

if __name__ == '__main__':

    N = int(input())

    for n in range(N):
        time = list(map(int, input().split()))
        duration_in_mins = duration(time[0], time[1], time[2], time[3])
        hours = 0
        minutes = 0

        try:
            if(duration_in_mins >= 60):
                minutes = duration_in_mins%60
                hours = int(duration_in_mins/60)
            else:
                minutes = duration_in_mins

        except:
            print("Error......")

        finally:
            print(str(hours) + " " + str(minutes))