import itertools
import string

def main():
    length = int(input())
    seq = (chr(i) for i in range(97, 97+length))
    
    l = list(itertools.product(seq, repeat=length))
    s = ""
    
    for i, val in enumerate(l):
        minchar = 'a'
        fl = True
        if val[0] != 'a':
            continue
        for j in range(len(val)-1):
            if val[j] > val[j+1]:
                if ord(val[j+1]) - ord(minchar) > 0:                
                    fl = False
                    break
            if ord(val[j+1]) - ord(minchar) > 0:
                if ord(val[j+1]) - ord(minchar) > 1:
                    fl = False
                    break
                else:
                    minchar = val[j+1]
        if fl:
            s += ("".join(val) + "\n")
            
    print(s)

if __name__ == '__main__':
    main()
