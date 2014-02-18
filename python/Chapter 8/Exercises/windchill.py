# windchill.py
# formula: 35.74 + 0.6215T - 35.75 * (V ** 0.16) + 0.4275T * (V ** 0.16)
# T is temp in fahrenheit V is windspeed in MPH


def windchill():
    # calculate windchill for every 5 mph.
    # show temps from -20 to +60 in 10 degree increments
    print()
    print("Temp     Windspeed      Windchill")
    print("_________________________________")
    for v in range(51):
        if v % 5 == 0 or v % 5:
            for t in range(-20, 61):
                if t % 10 == 0:
                    wc = 35.74 + (0.6215 * t) - 35.75 * (v ** 0.16) + (0.4275 * t) * (v ** 0.16)
                    print("{0:5} {1:10} {2:16.4f}".format(t, v, wc))


if __name__ in ['__console__', '__main__']:
    windchill()