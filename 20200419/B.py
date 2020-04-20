n, m = map(int,input().split()) 
li = list(map(int,input().split()))

if (n - sum(li)) < 0:
    print(-1)
else:
    print(n - sum(li))

