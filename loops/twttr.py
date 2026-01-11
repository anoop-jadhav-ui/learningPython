def main():
    str = input("Input: ")
    result = ""
    for c in str:
        if (not c.lower() in ["a", "e", "i", "o", "u"]):
            result += c

    print(f"Output: {result}")
    return


if (__name__ == "__main__"):
    main()
