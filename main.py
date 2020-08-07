import random as rand

scorew = 0
scorel = 0

def repeat():
    pag = input("Do you want to play again? ").casefold()
    if pag == "yes":
        main()
    elif pag == "no":
        print("Okay! Hope to see you soon!")
    else:
        print("Please answer with yes or no.")
        repeat()

def main():
    rand.seed(None, 2)
    main = rand.randint(1, 3)
    global scorew
    global scorel
    print("Welcome to Rock, Paper, Scissors!")
    usr = input("Choose! Rock, Paper or Scissors? ").casefold()
    if usr == "rock":
        if main == 1: #rock
            print("Your opponent chose rock!")
            print("You tied!")
        elif main == 2: #paper
            scorel += 1
            print("Your opponent chose paper!")
            print("You lost :(")
        elif main == 3: #scissors
            scorew += 1
            print("Your opponent chose scissors!")
            print("You won!")
    elif usr == "paper":
        if main == 1: #rock
            scorew += 1
            print("Your opponent chose rock!")
            print("You won!")
        elif main == 2: #paper
            print("Your opponent chose paper!")
            print("You tied!")
        elif main == 3: #scissors
            scorel += 1
            print("Your opponent chose Scissors!")
            print("You lost :(")
    elif usr == "scissors":
        if main == 1: #rock
            scorel += 1
            print("Your opponent chose rock!")
            print("You lost :(")
        elif main == 2: #paper
            scorew += 1  
            print("Your opponent chose paper!")
            print("You win!")
        elif main == 3: #scissors
            print("Your opponent chose scissors!")
            print("You tied!")
    else:
        print("Incorrect answer, please answer with Rock, Paper, or Scissors.")
        print("Exiting.")
        exit()
    print("You won ", scorew, "times")
    print("And lost ", scorel, "times")
    repeat()
 
main()
    
    
    
