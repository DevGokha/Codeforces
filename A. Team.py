n = int(input())
t = 0
for _ in range(n):
  a , b, c = map(int,input().split())
  if (a+b+c) >=2:
    t+=1
print(t)
