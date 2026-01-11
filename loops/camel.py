
def main():
    txt = input("camelCase: ")
    print(camelCaseToSnakeCase(txt))
    return


def camelCaseToSnakeCase(str):
    res = ""
    for c in str:
        if (c.isupper()):
            res = res + ("_" + c.lower())
        else:
            res = res + c
    return res


if (__name__ == "__main__"):
    main()
