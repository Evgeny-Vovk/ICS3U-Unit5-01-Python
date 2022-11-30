# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: November 2022
# ICS3U-Unit5-01.py File, learning functions in python.


def fahrenheit():

    celsius = input("Enter a temperature (°C): ")

    try:
        print("")
        celsius_as_float = float(celsius)
        fahrenheit = 9 / 5 * celsius_as_float + 32
        print("{0}°C is equal to {1:.2f}°F.".format(celsius_as_float, fahrenheit))

    except ValueError:
        print("Invalid input, please try again.")


def main():
    fahrenheit()

    print("\n\nDone.")


if __name__ == "__main__":
    main()
