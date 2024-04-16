import random 
rnum = random.randrange(1,100)
counter = 0
print(rnum)

while True:
    userInput = input("Guess a whole number between 1 and 100")
    userInput = int(userInput)
    if(userInput>=1 and userInput<=100):
        counter += 1
        if userInput<rnum:
            print("Guess a higher number")
            
        elif userInput>rnum:
            print("Guess a lower number")
            
        elif userInput == rnum:
            print(f"You guessed the number in {counter} guesses")
            break
              
    

