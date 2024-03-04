import random as rdm

# All the possible options
options = ["Rock", "Paper", "Scissors"];

# Values
usrScore = 0
botScore = 0;
round = 1;

# Game start
print("Welcome to Handbattles");
print("A.K.A Rock Paper Scissors!");

# Suspense
def suspense():
    suspense = ["Cling...!", "Clashhh!!!...", "Clang!!!", "CrlCrl...."];
    for time in range(3):
        print(rdm.choice(suspense));

while (True):
    try:
        bestOf = int(input("Best of ?: "));
        break;
    except:
        print("Please type a valid numeric value");


while(bestOf):
    print(f"\nRound {round}");
    print("Scores: ");
    print(f"Player 1: {usrScore} | Player 2: {botScore}");

    # Player 1 (Human)
    print("What do you want to throw? ");
    while (True):
        try:
            usrInput = int(input("1. Rock \n2. Paper \n3. Scissors\n"));
            if (usrInput == 1 or usrInput == 2 or usrInput == 3):
                break;
            else:
                print("Please choice from the above options");
        except:
            print("Please type a valid numeric value");
    
    usrInput = options[usrInput-1];

    # Player 2 (Computer)
    botInput = rdm.choice(options);

    # Different conditions
    if (botInput == usrInput):
        print("");
        
        suspense();
        print("Round's Result:");
        print(f"Seems like you both choose {usrInput}");
    elif ((usrInput == "Rock" and botInput == "Scissors") or (usrInput == "Paper" and botInput == "Rock") or (usrInput == "Scissors" and botInput == "Paper")):
        print("");

        suspense();
        print("Round's Result:");
        print("You won!");
        print(f"You choose {usrInput}, while the bot choose {botInput}");
        usrScore += 1;
    else:
        print("");
        
        suspense();
        print("Round's Result:");
        print("You lost!");
        print(f"You choose {usrInput}, while the bot choose {botInput}");
        botScore += 1;
    round += 1;

    bestOf -= 1;


print("\nFinal Scores: ");
print(f"Player 1: {usrScore} | Player 2: {botScore}")
    
if (usrScore > botScore):
    print("\You have won this battle!");
    print("Congrats");
elif (usrScore < botScore):
    print("You have lost this battle!");
    print("Better luck next time.");
else:
    print("Unbelieve it's a tie!!");