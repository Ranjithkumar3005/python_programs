import textwrap

def wrap(string, max_width):
    s=""
    d=0
    for i in range(0,len(string)):
        s+=string[i]
        d+=1
        if d==max_width:
            s+="\n"
            d=0
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)