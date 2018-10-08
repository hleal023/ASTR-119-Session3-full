import numpy as np

i = 10 #integer
print(type(i)) 

a_i = np.zeros(i,dtype=int) #declare array of integers
print(type(a_i))			#returns ndarray
print(type(a_i[0]))			#returns int64 bits

#floats

x = 119.0					#floating pt number 
print(type(x)) 				#print out the data type of x

y = 1.19e2					#float 119 in sci notation
print(type(y))				#print out the data type of y

z = np.zeros(i,dtype=float)	#declare array of floats 
print(type(z))				#returns nd array
print(type(z[0]))			#returns float64
