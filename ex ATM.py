from time import sleep

print("*"*50)
print("\U0001F4B3 ATM \U0001F4B3")
print("*"*50)

while True:
    try:
        cash=int(input("\U0001F4B5 What amount would you like to withdraw? The ATM has bills of 50, 20, 10, and 1 dollars: "))
        break
    except ValueError:
        print("\033[31mPlease enter a numeric value\033[m")

cont_50 = cash // 50
cash = cash % 50

cont_20 = cash // 20
cash = cash % 20

cont_10 = cash // 10
cash = cash % 10

cont_1 = cash

print("*"*50)

print("\U0001F4B3 PROCESSING \U0001F4B3")
print(".")
sleep(0.5)
print(".")
sleep(0.5)
print(".")

print(f"\033[32m$50 bills:\033[m {cont_50}")
print(f"\033[34m$20 bills:\033[m {cont_20}")
print(f"\033[32m$10 bills:\033[m {cont_10}")
print(f"\033[34m$1 bills:\033[m {cont_1}")

