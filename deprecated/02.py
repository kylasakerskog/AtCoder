A, B, M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
minimum = a[0]+b[0]

for k in range(M):
    x,y,c = map(int,input().split())
    tmp = a[x-1]+a[y-1]-c
    if minimum > tmp:
        minimum = tmp

a.sort()
b.sort()

for i in a:
    if i + b[0] > minimum:
        break
    for j in b:
        tmp = i + j
        if minimum > tmp:
            minimum = tmp
        else:
            break

print(minimum)
