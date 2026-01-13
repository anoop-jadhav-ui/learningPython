def main():
    while(True):
        try:
            fraction = input("Fraction:")
            [x,y] = fraction.split("/")
            percent = round(int(x) / int(y) * 100)
            if(percent > 100 or percent < 0):
                continue
            if(percent >= 99):
                print("F")
            elif(percent <= 1):
                print("E")
            else:
                print(f"{percent}%")
            break
        except(ValueError, ZeroDivisionError):
            continue

if(__name__ == "__main__"):
    main()