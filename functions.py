
import numpy as np
import sys

#define fct that returns value
def expo(x):
	return np.exp(x) #returns the np e^x fct

#define subroutine that doesnt return value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))

#define main fct
def main():
	n = 10 
	#check if command line argument is provided 
	if(len(sys.argv)>1):
		n = int(sys.argv[1]) #if argument provided use it for n
		
	show_expo(n)
	
if __name__ == "__main__":
	main()
	
