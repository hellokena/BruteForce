import sys

def solution(num) :
    result = 0
    for i in range(1, num+1):
        # 1부터 99까지는 모두 한수이다.
        if i < 100: result += 1
        else: # 입력값으로 1000보다 작은 수가 주어지기 때문에 3자리수임
            temp = list(map(int, str(i)))
            print(temp)
            if temp[1]-temp[0] == temp[2]-temp[1]: result += 1
    print(result)

num = int(sys.stdin.readline().rstrip())
solution(num)
