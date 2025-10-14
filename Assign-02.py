# Created by Christopher El-Murr
# Created on Oct 14 2025
# This Program calculates the Volume and surface area in Python
import math


def main():
    # Ask the user to enter the Radius of the Sphere
    Radius = int(input("Enter the Radius of Sphere:"))
    # Calculate the Volume
    Volume = (4 / 3) * math.pi * (Radius ** 3)
    # Calculate the Sufrace Area
    Surface_Area = 4 * math.pi * (Radius ** 2)

    print("")
    # Display the Surface area and volume of the sphere
    print("The Surface Area is {:,.2f}".format(Surface_Area))
    print("The Volume is = {:,.2f}".format(Volume))


if __name__ == "__main__":
    main()
