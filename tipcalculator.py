def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar_change = d.replace("$", "")
    return float(dollar_change)


def percent_to_float(p):
    percent_change = p.replace("%", "")
    p_converted = float(percent_change) / 100
    return p_converted