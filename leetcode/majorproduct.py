
''' The main function that returns the max possible product '''
def maxProd(n):

    # n equals to 2 or 3 must be handled explicitly 
    if (n == 2 or n == 3):
	    return (n - 1); 

    # Keep removing parts of size 3 while n is greater than 4 
    res = 1;  
    while (n > 4):
	
	    n -= 3; 
	    res *= 3;# Keep multiplying 3 to res 
	
    return (n * res); # The last part multiplied by previous parts 


''' Driver program to test above functions '''
if __name__=='__main__':
	print("Maximum Product is", maxProd(2))
	
	# This code is contributed by rutvik_56.
