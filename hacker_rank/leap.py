def is_leap(year):
    leap = False
    print(2100%4)
    if (year%4==0) or (year//400==0):
        leap=True
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))