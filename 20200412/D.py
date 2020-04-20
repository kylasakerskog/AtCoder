d = input()
s = input()

r = s.count('R')
g = s.count('G')
b = s.count('B')

res = r*g*b
for i in range(len(s)-2):
    for j in range(i,len(s)-1):
        k = 2 * j - i
        if k < len(s) and s[i] != s[k] and s[i] != s[j] and s[j] != s[k]:
            res -= 1
print(res)
