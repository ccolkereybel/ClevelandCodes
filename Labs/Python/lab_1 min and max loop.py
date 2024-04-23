counter = 0

while True:
    userInput = input("Enter a number from 1 to 100")
    if userInput.lower() == "q":
        break
    userInput = int(userInput)
    if userInput >=1 and userInput <= 100:
        counter += 1
        if counter == 1:
            max = userInput
            min = userInput
        elif userInput < min:
            min = userInput
        elif userInput > max:
            max = userInput


print(f"Minimum = {min} \n"
      f"Maximum = {max} \n"
      f"You entered {counter} numbers")
        
    
