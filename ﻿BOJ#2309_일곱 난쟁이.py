import sys
dwarf = []
for i in range(9):
    dwarf.append(int(sys.stdin.readline().rstrip()))

def solution(dwarf):
    for i in range(9):
        for j in range(i+1, 9):
            if 100 == sum(dwarf)-dwarf[i]-dwarf[j]:
                num1, num2 = dwarf[i], dwarf[j]
                dwarf.remove(num1)
                dwarf.remove(num2)
                dwarf.sort()
                for d in dwarf:
                    print(d)
                exit()

solution(dwarf)
