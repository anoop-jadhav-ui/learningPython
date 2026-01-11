def main():
    time = input("What time is it?")
    timeInDecimals = convert(time)

    if (timeInDecimals >= 7 and timeInDecimals <= 8):
        print("breakfast time")
    elif (timeInDecimals >= 12 and timeInDecimals <= 13):
        print("lunch time")
    elif (timeInDecimals >= 18 and timeInDecimals <= 19):
        print("dinner time")


def convert(time):
    [hhStr, mmStr] = time.split(":")

    hh = float(hhStr)
    mm = float(mmStr) / 60

    return hh + mm


if __name__ == "__main__":
    main()
