# speeding.py
# determines the cost of a speeding ticket based on speed of car.


def ticket(speed, limit):
    over_ninty_fee = 200
    ninty = 90
    initial_fee = 50
    per_mph = 5
    ticket_fee = 0
    # speeding tickets are $50 + $5 for ever mph over the limit.
    if speed > limit:
        excess = speed - limit
        ticket_fee = initial_fee + (excess * per_mph)
        # if the speed is over 90 mph, there is an additional $200 fine.
        if speed > ninty:
            ticket_fee = ticket_fee + over_ninty_fee

    legal = "The speed, {0}, is a legal speed.".format(speed)
    illegal = "The speed, {0}, is illegal. Your fine is: ${1:0.2f}".format(speed, ticket_fee)

    if speed > limit:
        return illegal
    else:
        return legal


def main():
    speed = int(input("How fast was the car going? "))
    limit = int(input("What is the posted speed? "))

    verdict = ticket(speed, limit)

    print(verdict)


if __name__ in ['__console__', '__main__']:
    main()