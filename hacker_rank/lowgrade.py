name1=[]
score1=[]
n=int(input())
for i in range(n):
        name = input()
        score = float(input())
        name1.append(name)
        score1.append(score)
    
total=[[name1[i], score1[i]] for i in range(len(name1))]

tota1=sorted(total,key=lambda x:x[0] and x[1])
print(total)
for i in range(1,n):
    if total[i][1]==total[i+1][1]:
        for j in range(0,1):
            print(total[i][j])
            
    
    else:
        print(total[i][0])
        break