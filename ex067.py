print("-" * 10, "Multiplication Table Program\U0001F92F", "-" * 10)

num=int(input("\033[34mWhich multiplication table would you like to see? Enter a number [a negative number will stop the program]: \033[m"))
div=1
vz=0
while True:
    if num <=0:
        print("\033[31mNegative number, end of program.\033[m")
        break
    elif num >0:
        vz= num * div
        print(f"{num} x {div} = {vz}")
        div+=1
    if div == 11:
        print(f"\033[mThis is the multiplication table of {num}.\033[m")
        num = int(input("\033[34mWhich multiplication table would you like to see? Enter a number [a negative number will stop the program]: \033[m"))
        div=1

