# convert.py
# A program to convert Celsius tempts to Fahrenheit


def main():
    celsius = int(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperatureis {0} degrees fahrenheit.".format(fahrenheit))

    # print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("Brrrrr. Be sure to dress warmly!")


if __name__ in ['__main__', '__console__']:
    main()
