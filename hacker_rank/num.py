def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        print("{} {:o} {:x} {:b}".format(i,i,i,i))
   

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)