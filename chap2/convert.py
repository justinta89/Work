# convert.py
# A program to convert Celsius tempts to Fahrenheit


def main():
    celsius = int(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperatureis {0} degrees fahrenheit.".format(fahrenheit))


if __name__ in ['__console__', '__main__']:
    main()