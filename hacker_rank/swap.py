def swap_case(s):
    d=[]
    new=""
    for i in range(0,len(s)):
        if ord(s[i])>=65 and ord(s[i])<=90:
            d.append(chr(ord(s[i])+32))
            
        elif ord(s[i])>=97 and ord(s[i])<=122:
            d.append(chr(ord(s[i])-32))
        else:
            d.append(s[i])
            
    for x in d:
        new += x
    return new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)