words = ["blue","green","bu"]

for i in range(0,len(words)):
    for j in range(0,len(words)):
        if i==j:
             continue
        else:
            u=0
            p=0
            for k in range(0,len(words[i])):
                 for f in range(p,len(words[j])):
                      if words[i][k]==words[j][f]: 
                       u+=1
                       p=f+1
                       break
            if u==len(words[i]):
              print(words[i])