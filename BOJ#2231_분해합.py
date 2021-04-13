import sys
n = int(sys.stdin.readline().rstrip())

def solution(n):
    for i in range(1,n+1):
        array = list(map(int, str(i)))
        result = sum(array) + i
        if result==n:
            print(i)
            break
        if i==n: print(0)

solution(n)
