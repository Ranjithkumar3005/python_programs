def game(num):
    c=0
    if len(num)==1:
        print('Ramos')
        return 0
    for i in range(0,len(num),2):
        if num[i]!=num[i+1]:
            c+=1
    if c%2!=0:
        print('Zlatan')
    else:
        print("Ramos")



T=int(input())
for i in range(T):
    val=input()
    val1=str(input())
    game(val1)