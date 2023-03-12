def main():
  text = input("Hello fellas: ")
  
  text = convert(text)
  print(text)



def convert(text):
  text = text.replace(":)", "🙂")
  text = text.replace(":(", "🙁")
  return text

main()