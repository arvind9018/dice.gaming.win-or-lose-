import random
human_point=0
computer_point=0
print("\t\t\t\t HELLO\t\t\t\t")
print("\t\t\tWelcome to this wonderful Game\t\t")
print("(NOTE: Whenever you whant to exist the game please press 0[ZERO].) \n\n")
i=0
while (True):
    a=int(input("Enter a number from 1 to 6: \n",))
    b=int(random.randint(1,6))
    if a==b:
        human_point=human_point+1
        print(f"You enter {a} and computer give {b}")
        print("You WIN")
        print(f"Computer point is {computer_point} and your point is {human_point}")
    elif a!=b and a>=1 and a<=6:
        computer_point=computer_point+1
        print(f"You enter {a} and computer give {b}")
        print("You LOOSE")
        print(f"Computer point is {computer_point} and your point is {human_point}")
    elif a==0:
        break
    else:
        print("Please enter a vlid input")
print("\t \t \tGave over\t\t\t")
print(f"Your point is '{human_point}' and Computer point is '{computer_point}'.")
print("\t\tThank you for your valuable time.\t\t\t")
print("\t\t\tSee you soon.\t\t\t")