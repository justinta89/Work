# senator.py
# this program takes age and years of citizenship and determins if user is eligible for senate and house


def gov(age, citizenship):
    if age >= 25 and citizenship >= 7:
        if age < 30:
            return "House"
        if age >= 30:
            return "Senate"
    else:
         return "Not Eligible"


def main():
    age = int(input("Enter age:"))
    citizen = int(input("Enter years a citizen: "))

    eligible = gov(age, citizen)

    print("You are eligible for: {0}".format(eligible))


if __name__ in ['__console__', '__main__']:
    main()