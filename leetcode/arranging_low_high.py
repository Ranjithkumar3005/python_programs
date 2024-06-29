def arrange(dum):
    d=[0]*len(dum)
    dum=sorted(dum,reverse=True)
    e=0
    f=0
    check=False
    for i in range(0,len(dum)):
        if check:
          d[f]=dum[i]
          check=False
          f+=1
        else:
          c=len(dum)-e-1
          d[c]=dum[i]
          check=True  
          e+=1
    print(d) 

arrange([10,20,30,40,50,60,70,80,90,100])