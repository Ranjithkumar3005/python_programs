I    =         1
V     =        5
X      =       10
L       =      50
C        =     100
D         =    500
M          =   1000
A=" "

s = "MCMXCIV"
s=s+A
print(s)
s1="IVXLCDM"
total=0
for i in range(0,len(s)-1):
    if s[i]=='I' and (s[i+1] not in s1[1:len(s1)]):
        total+=1
    elif s[i]=='I' and (s[i+1] in s1[1:len(s1)]):
        total-=1 
    elif s[i]=='V' and (s[i+1] not in s1[2:len(s1)]):
        total+=5
    elif s[i]=='V' :
        total-=5
    elif s[i]=='X' and (s[i+1]  not in s1[3:len(s1)]):
        total+=10
    elif s[i]=='X':
        total-=10
    elif s[i]=='L' and (s[i+1]  not in s1[4:len(s1)]):
        total+=50
    elif s[i]=='L':
        total-=50
    elif s[i]=='C' and (s[i+1]  not in s1[5:len(s1)]):
        total+=100
    elif s[i]=='C':
        total-=100
    elif s[i]=='D' and (s[i+1]  not in s1[6:len(s1)]):
        total+=500
    elif s[i]=='D':
        total-=500
    elif s[i]=='M':
        total+=1000
        
print(total)
    