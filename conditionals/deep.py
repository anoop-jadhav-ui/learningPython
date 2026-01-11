valid_answers = ["42", "forty-two", "forty two"]
x = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if x.lower().strip() in valid_answers:
    print("Yes")
else:
    print("No")
