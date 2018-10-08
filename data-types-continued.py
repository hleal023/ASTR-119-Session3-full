								#string

s = "I am a string"
print(type(s))					#says string

								#Boolean

yes = True
print(type(yes))

no = False
print(type(no))

								#list -- ordered and changeable

alpha_list = ["a", "b", "c"]  	#list initialization
print(type(alpha_list))			#says tuple
print(type(alpha_list[0]))		#says string
alpha_list.append("d")			#adds "d" to the list end
print(alpha_list)				#print list

								#Tuple -- ordered and unchangeable
									
alpha_tuple = ("a", "b", "c")	#Tuple initialization
print(type(alpha_tuple))		#says tuple

try:							#attempt following line
	alpha_tuple[2] = "d"		#wont work comes back with TypeError
except TypeError:				#when we get a type error, print "We cant add..."
	print("We can't add elements to tuples!") 
print(alpha_tuple)