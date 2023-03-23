# creating symbol vowels
# symbols = a,e,i,o,u


text = input("input: ")

print("output: ", end="")

for symbols in text:
    if not symbols in ["a","i","e","o","u"]:
        print(symbols, end="")