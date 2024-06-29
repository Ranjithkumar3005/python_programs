try:
    a=int(input("Enter the a value:"))
    b=int(input("Enter the b value:"))
    c=a/b
except Exception as e:
    print(e)
    
else:
    print(c)

finally:
    print("This always execute")