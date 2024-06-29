def grades(value):
    if value>=90:
        return ("Grade: S")
    else:
        q=value//10 
        if q<4:
            return ("Grade: F")
        return ("Grade: "+str(chr(73-q)))
    
grade=grades(int(input("Enter Mark:")))
print(grade)