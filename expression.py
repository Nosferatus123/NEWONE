expression = input("expression: ").split(" ")
x = float(expression[0])
y = expression[1]
z = float(expression[2])

if y == "+":
    result = x + z
if y == "-":
    result = x - z
if y == "*":
    result = x * z
if y == "/":
    result = x / z
print(result)