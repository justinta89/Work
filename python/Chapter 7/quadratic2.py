# quadratic2.py
import math


def main():
    print("This program finds the real solutions to a quadratic\n")

    try:
        a, b, c = map(int, input("Enter the coefficients a, b, c: ").split(','))
        discrim = b * b - 4 * a * c
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are: {0} {1}".format(root1, root2))

    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No real roots")
        else:
            print("You don't have the right number of coefficients")
    except NameError:
        print("\nYou didn't enter three numbers")
    except TypeError:
        print("\nYour inputs were not all numbers")
    except SyntaxError:
        print("\nYour input was not in the correct form. Missing comma?")
    except:
        print("\nSomething went wrong, sorry!")


if __name__ in ['__console__', '__main__']:
    main()