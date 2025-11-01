import sys
input=sys.stdin.readline


board=input()


count=0
result=[]
for i in board:
    if i=='X':
        count+=1
    else:
        if count%2==1:
            print(-1)
            break
        else:
            count_a=count//4
            count_b=count%4
            result.append('A'*count_a*4)
            result.append('B'*count_b)
            if i=='.':
                result.append('.')
        count=0

print(*result)