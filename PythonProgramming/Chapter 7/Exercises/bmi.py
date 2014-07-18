# bmi.py
# this will figure out a persons BMI and if it is in a healthy range based on their height and weight.


def bmi(h, w):
    weight = w * 720
    height = h ** 2

    bmi = weight / height

    if bmi <= 19:
        return "BMI is under healthy BMI."
    elif bmi >= 25:
        return "BMI is over healthy BMI."
    else:
        return "BMI is healthy!"


def main():
    height = int(input("Enter height in inches (6 feet = 72 inches): "))
    weight = int(input("Enter weight in pounds: "))

    body = bmi(height, weight)
    print(body)


if __name__ in ['__console__', '__main__']:
    main()