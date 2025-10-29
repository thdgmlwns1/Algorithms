import sys
input= sys.stdin.readline

a,b=input().split()

result=[]
for i in range(2,37):
    for j in range(2,37):
        if i==j:
            continue
        try:
            if int(a,i)==int(b,j):
                result.append((int(a,i),i,j))
        except:
            pass


if len(result)==0:
    print("Impossible")
elif len(result)==1:
    print(*result[0])
else:
    print("Multiple")
    

