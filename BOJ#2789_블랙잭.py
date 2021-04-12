import sys

def solution(n,m,cards) :
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                temp = cards[i] + cards[j] + cards[k]
                if temp <= m: result = max(temp, result)
    print(result)

n,m = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
solution(n,m,cards)
