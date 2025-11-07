import random
from time import sleep

print("*" * 20)
print("Play EVEN or ODD against the computer \U0001F3C6")
print("The game only ends when you lose!")
print("*" * 20)

total = 0
win = 0

while True:
    num_player=int(input("\033[34mChoose a number: \033[m"))
    choice_player= str(input("\033[33mDo you choose EVEN or ODD? [E/O]: \033[m")).strip().upper()

    print("The computer is choosing its number...")
    print("Please wait..")
    sleep(1)

    num_computer=random.randint(1,10)

    total = num_player + choice_player

    if (total % 2 == 0 and choice_player == "E") or (total % 2 == 1 and choice_player == "O"):
        print(f"\033[32mCongratulations! The computer chose {num_computer} and the total was {total}! You won! Keep playing!\033[m")
        win=win + 1

    elif (total % 2 == 0 and choice_player == "O") or (total % 2 == 1 and choice_player == "E"):
        break

print(f"\033[31mThe computer chose {num_computer} and the total was {total}. You lost!!\033[m")
print(f"\033[31mYou won {win} time(s) this round!\033[m")