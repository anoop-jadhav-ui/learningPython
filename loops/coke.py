def main():

    TOTAL_AMOUNT = 50
    due = TOTAL_AMOUNT
    print(f"Amount Due: {due}")
    while (True):
        money = int(input("Insert Coin: "))
        if (money in [5, 10, 25]):
            due = due - money
            if (due <= 0):
                print(f"Change Owed: {abs(due)}")
                break
        print(f"Amount Due: {due}")
    return


if (__name__ == "__main__"):
    main()
