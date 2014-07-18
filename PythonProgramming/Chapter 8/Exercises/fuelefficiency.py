# fuelefficiency.py


def getInputs():
    # prompt user for starting odometer reading
    # get number of legs in journey
    # return data
    odometer = float(input("Enter current odometer reading: "))
    legs = int(input("Enter number of legs in journey: "))
    return odometer, legs


def fuelEfficiency(curr_odo, legs):
    new_odo, gas = map(int, input(
            "Enter odometer reading and gas used: ").split(" "))
    while new_odo != "" and gas != "":
        distance = new_odo - curr_odo
        efficiency = distance / gas
        new_odo, gas = map(int, input(
            "Enter odometer reading and gas used: ").split(" "))

    return efficiency


def main():
    odometer, legs = getInputs()
    efficiency = fuelEfficiency(odometer, legs)

    print(odometer, efficiency)


if __name__ in ['__console__', '__main__']:
    main()