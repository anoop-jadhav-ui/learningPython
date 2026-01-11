def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    return


def is_valid(s):
    if not s[:2].isalpha():
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    if not s.isalnum():
        return False

    numStarts = False
    for c in s:
        if c.isnumeric():
            if numStarts == False and c == "0":
                return False
            numStarts = True
        elif numStarts and c.isalpha():
            return False

    return True


if (__name__ == "__main__"):
    main()
