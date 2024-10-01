import csv
from datetime import date,time,datetime

lines = 0
payroll = 0
outlist = []

starttime = datetime.now()

with open("timesheet.csv", "r") as fpin:
    reader = csv.reader(fpin)
    for line in reader:
        if lines > 0:
          id = line[0]
          fname = line[1]
          lname = line[2]
          pay = int(float(line[3])) * int(float(line[4]))
          payroll += pay
          print(f"{id} {fname} {lname} {pay:,.2f}")
        lines += 1
        
today = date.today()
print(f"Payroll Date: {today:%x}")

print(f"Start Time: {starttime:%X}")

endtime = datetime.now()
print(f"End Time: {endtime:%X}")

print (f"Records processed: {lines}")

print (f"Total Payroll Amount: {payroll:,.2f}")


          
