from happy_birthday import happy_birthday

print("Welcome :)")

# Daryafte moshakhasat

esm = input("What is your name?")
sen = input("How old are you?")
happy_birthday(age=sen, name=esm)
sen = int(sen)

while True:
    vazn = input("How much do you weigh?")
    vazn = int(float(vazn))
    ghad = input("How tall are you?")
    ghad = int(float(ghad))

    # Namayeshe moshakhasat jahate taeid

    print(
        "Salam",
        esm,
        "Senne shoma",
        sen,
        "Vazne shoma",
        vazn,
        "Ghade shoma",
        ghad,
        "mibashad",
    )
    taeid = input("Aya taeid mikonid? Y/N. Enter Q to exit.")
    print("Javabe shoma: " + taeid)

    if taeid == "Y":
        print("dar hale mohasebe...")
        javab = vazn / ghad
        javab = float(javab)
        print(javab)
        if javab > 0.6:
            print("Ezafe vazn darid :(")
        else:
            print("Normal Hastid :)")
        break
    elif taeid == "N":
        continue
    else:
        break
