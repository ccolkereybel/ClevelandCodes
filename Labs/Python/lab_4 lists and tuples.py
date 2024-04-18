#list intersection
L1 = [1,2,3,4]
L2 = [3,4,5,6]
L3 = []
for item in L1:
    if item in L2:
        L3.append(item)
        
print("List intersection:", L3)


#factorial
L1 = [1,2,3,4]
total = 1
for item in L1:
    int(item)
    total *= item
    
print("Factorial total:", total)


#even/odd list
L1 = [22,54,76,87,47,77,98,30,76,90,21,22,45,76,81]
even = []
odd = []
for item in L1:
    if item%2 == 0:
        even.append(item)  
    else:
        odd.append(item)
        
odd.sort()
even.sort()
    
print("Even numbers list:", even)
print("Odd numbers list:", odd)

#string to tuple
cc_string = "ClevelandCodes"
cc_tuple = tuple(cc_string)
print(cc_tuple)

#convert a tuple
stooges = ("Larry", "Curly", "Moe")
print(stooges)

stooges = list(stooges)
stooges[1] = "Shemp"
stooges = tuple(stooges)
print(stooges)
