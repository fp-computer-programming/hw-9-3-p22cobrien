# Author: CMOB 1/13/2022

from hashlib import new


temp = float(input("What is the temperature?"))
conver = str.capitalize(input("Is it Celsius(C) or Fahrenheit(F)?"))
try:
    if conver == "F":
        new_temp = temp / 5
    elif conver == "C":
        new_temp = temp - 32 / 9
    print(new_temp)
except ZeroDivisionError:
    print(-17.18)
except:
    print("P")
