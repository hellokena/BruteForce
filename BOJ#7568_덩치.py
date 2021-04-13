import sys
array = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    weight, height = map(int, sys.stdin.readline().rstrip().split())
    array.append([weight, height])

def solution(n,array):
    for i in array:
        rank = 1
        for j in array:
            if i[0]!=j[0] and i[1]!=j[1]:
                if i[0]<j[0] and i[1]<j[1]:
                    rank += 1
        print(rank, end=' ')

solution(n,array)
