#input matter :
camelCase = input("camelCase: ")
print("snake_case: ", end="")
for text in camelCase:
    if text.isupper():
        print("_" + text.lower(), end="")
    else:
        print(text, end="")