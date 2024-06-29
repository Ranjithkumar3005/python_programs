num1=[1,6]
num2=[7]
num1.extend(num2)
num1=sorted(num1)
sum=0.0000
len=len(num1)
len1=int(len/2)
if int(len%2)!=0:
    print(float(num1[len1]))
else:
    for i in range(len1-1,len1+1):
         sum+=num1[i]
    
    print(sum/2)
    