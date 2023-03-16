def main():
    convert()
def convert():
  time = input("What time is it ?: ")
  hours, minutes = time.split(":")
  hours = float(hours)
  minutes = (float(minutes) * 100 / 60) / 100
  sec = hours + minutes
  if 0 <= hours < 24 and 0 <= minutes < 60:
    if 7 <= sec <= 8:
        print("breakfast time")
    elif 12 <= sec <= 13:
        print("sec time")
    elif 18 <= sec <= 19:
        print("dinner time")
    else:
       print("wrong time")
if __name__ == "__main__":
  main()