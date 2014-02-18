# prime.py
# Determines if the given number is prime or not. A prime number is a number where no number between 2 and sqrt(n)(inclusive) evenly divides n.
# This program accepts a givne number, n, and determines if it is prime. if n is not prime the program will quit once it finds a number that can evenly divide n.
import math


def prime(num):

    #iterate through the range of numbers to see
    # check for any numbers that divide evenly.
    # if any numbers divide into given number evenly, break
    # if no number divide evenly, the number is prime
    for i in range(2, num):
        mod = num % i
        while mod == 0:
            return "{0} is not a prime number".format(num)
            break
    return "{0} is prime".format(num)


def main():
    while True:
        try:
            n = int(input("Enter a number >> "))
        except ValueError:
            print("Not valid input!")
            continue
        p = prime(n)
        print(p)
        break



if __name__ in ['__console__', '__main__']:
    main()