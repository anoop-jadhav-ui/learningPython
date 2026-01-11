greeting = input("Greeting: ")
greeting_l = greeting.lower().strip()
if (greeting_l.startswith("hello")):
    print("$0", end=""),
elif (greeting_l.startswith("h")):
    print("$20", end="")
else:
    print("$100", end="")
