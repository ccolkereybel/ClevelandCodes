import csv

with open("test-write.txt", "w") as fpout: #when done with commands, close file
    for i in range(0,100,2):
        fpout.write(f"{i}\n")
    
lines = 0
sum = 0 
with open ("emails-spring-2024.csv", "r") as fpin:
    reader = csv.reader(fpin) #method to read CSV files
    for line in reader:
        name = line[0]
        email = line[1]
        num = int(line[2])
        numx2 = num * 2
        sum += numx2 #used to find total for payroll
        print(f"Name: {name}\tEmail: {email}\tNumber: {numx2}")
        lines += 1
print (f"{lines} lines read")
print ("done")
            
