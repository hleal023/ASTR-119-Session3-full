
x = [0.0, 3.0, 5.0, 2.5, 3.7]           #define array
print(type(x))

x.pop(2)                                #remove third element
print(x)

x.remove(2.5)                           #remove element equal to 2.5
print(x)

x.append(1.2)                           #add an element at the end
print(x)

y = x.copy()                            #get a copy
print(y)

print(y.count(0.0))                     #how many elements are 0.0?

print(y.index(3.7))                     #print index w value 3.7

y.sort()                                #sort list
print(y)

y.reverse()                             #reverse sort
print(y)

y.clear()                               #remove all elements
print(y)
      
