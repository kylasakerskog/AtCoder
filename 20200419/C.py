a=int(input())
li = list(map(int,input().split()))
ans = [0] * (a)

for i in li:
    ans[i-1] += 1

for j in ans:
    print(j)
    
