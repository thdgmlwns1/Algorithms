import sys
input=sys.stdin.readline

N=int(input())


line=[]
for _ in range(N):
  line.append(int(input()))


line.sort(reverse=True)

sum=0
tip=0
for i in range(N):
  tip=line[i]-(i)
  if tip>0:
    sum+=tip

print(sum)
