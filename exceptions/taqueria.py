def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    totalAmount = 0
    while True:
        try: 
            order = input("Item: ").title()
            if menu[order]:
                totalAmount += menu[order]

                # precision to 2 decimal places
                print(f"Total: ${totalAmount:.2f}")
        except EOFError:
            break
        except KeyError:
            continue

if(__name__  == "__main__"):
    main()