import sys
input=sys.stdin.readline


coin=int(input())


count_5=0
count_2=0

count_5=coin//5
na=coin%5

if na%2==0:
  count_2=na//2
else:
  count_5+=-1
  count_2=(na+5)/2

if coin==1 or coin==3:
  print(-1)
else:
  print(int(count_5+count_2))


