
def getSpanish(instr):
    global esdic
    outstr = ""
    words = instr.split()
    print(words)
    for w in words:
        if w in esdic:
            outstr += esdic[w.lower()] + " "
        else:
            outstr += "**** "
    return outstr



esdic = {}
l=0
with open("eng-span.txt") as file:
    for line in file:
        parts = line.split()
        esdic[parts[0]] = parts[-2]
        l+=1
        #print(parts)
esdic["is"]="es"
esdic["the"]="el"
print(f"{l} lines read into dictionary")
#print(esdic)

while True:
    instr = input("Enter a sentence.")   
    print(getSpanish(instr))
