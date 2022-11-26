# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: November 2022
# ICS3U-Unit5-01.py File, learning functions in python.


def fahrenheit():

    celsius = input("Enter a temperature (°C): ")

    try:
        print("")
        celsius_asfloat = float(celsius)
        fahrenheit = 9 / 5 * celsius_asfloat + 32
        print("{0}°C is equal to {1:.2f}°F.".format(celsius, fahrenheit))

    except ValueError:
        print("Invalid input, please try again.")

    print("\n\nDone.")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
