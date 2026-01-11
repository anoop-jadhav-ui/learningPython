exp = input("Expression: ")
[xStr, y, zStr] = exp.split(" ")

x = float(xStr)
z = float(zStr)

match y:
    case "-":
        print(x - z)
    case "+":
        print(x + z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)
