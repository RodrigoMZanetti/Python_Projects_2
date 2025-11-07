response ="Y"
men = 0
age = 0
over18 = 0
young_women = 0

print("\033[1;33m**********REGISTRATION**********\033[m")

while True:
    print("-"*25)

    while True:
        gender=str(input("\U0001F31E\033[1mGender [M/F]:\033[m").upper().strip())
        if gender =="":
            print("\U0001F622\033[1;31mERROR, you must type something!\033[m")
            continue
        gender = gender[0]
        if gender in ["M", "F"]:
            break
        else:
            print("\U0001F622\033[1;31mERROR, please type only M or F!!\033[m")
    if (gender == "M") or (gender == "m"):
        men += + 1

    while True:
        try:
            age=int(input("\U0001F331\033[1mAge:\033[m"))
            break
        except:
            print("\U0001F622\033[1;31mERROR, please type only whole numbers.\033[m")
            continue
    if (age > 18):
        over18 += 1
    elif (age < 20 and gender == "F") or (age < 20 and gender == "f"):
        young_women += 1

    print("-" * 25)

    while True:
        response=str(input("\U0001F5A5\033[1;34mDo you want to continue registering people? [Y/N]: \033[m").strip().upper())
        if response == "":
            print("\U0001F622\033[1;31mERROR, you must type something!\033[m")
            continue
        response = response[0]
        if response in ["Y", "N"]:
            break
        else:
            print("\U0001F622\033[1;31mERROR, please type only Y or N!\033[m")
    if (response == "N") or (response == "n"):
        break

print("\033[1;33m-\033[m"*25)
print(f"\U0001F60E\033[1;31mNumber of people over 18 years old: {over18}.\033[m")
print(f"\U0001F4AA\033[1;32mNumber of men registered: {men}.\033[m")
print(f"\U0001F60D\033[1;35mNumber of women under 20 years old: {young_women}.\033[m")

