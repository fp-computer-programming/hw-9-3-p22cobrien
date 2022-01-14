# Author: CMOB 1/13/2022


while True:
    temp = float(input("What is the temperature?"))
    conver = str.capitalize(input("Is it Celsius(C) or Fahrenheit(F)?"))
    try:
        if conver == "C":
            if temp == 0:
                new_temp = 32
            else:
                new_temp = temp / 5
        elif conver == "F":
            new_temp = temp - 32 / 9

    except ValueError:
        print("Please input an appropriate number.")
    except NameError:
        print("Please input either C or F for temperature type.")

    finally:
        try:
            print(new_temp)
        finally:
            again = str.capitalize(input("Would you like to try again? Y or N"))
            if again == "N":
                break

