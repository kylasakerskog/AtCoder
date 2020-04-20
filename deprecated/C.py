N, K = map(int,input().split())

ans1 = N%K
ans2 = -1 * (N % (-1 * K))


if ans1 < ans2:
    print(ans1)
else:
    print(ans2)
