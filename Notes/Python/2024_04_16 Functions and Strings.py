def addNumbers (x,y=0):
    z=x+y
    return x,y, z
# x = int (input("X: "))
# y = int (input("Y: "))

# x2, y2, z2 = addNumbers (x,y)
# print (x2, y2, z2)

str1 = input("Enter String: ")

#for c in str1:
#   print(c)

print("Length = " + str(len(str1)))

for n in range (len(str1)):
    print (str1[n])

print(str1.upper())

print(str1.lower())

str2 = str1[2:7]

print(str2)

str3 = str1[:6] #start at beginning

str4 = str1[2:] #start at 2, go to end

print (str1 [-5:-2])

#reverse a string

revstr = ""

for c in range(-1, -(len(str1)+1), -1):
    print (str1[c])
    revstr += str1[c] #concatenate string

    print(revstr)

revstr2= ""
for c in str1:
    revstr2 = c + revstr2 #put character in front
print(revstr2)
