import os
path="D:\\python_programs\\hello.txt"

if os.path.exists(path):
    print("The location is identified")
else:
    print("The location doesn't found")
    
#Same for the file and directory


#With open function , it automatically closed
try:
    with open("hello.txt") as file:
        print(file.read()) 
except Exception as e:
    print(e)
    
text="Hello\n\nRanjithikumar"
with open("hello.txt",'a') as file:
    file.write(text)
    
#see more ablut files in a video