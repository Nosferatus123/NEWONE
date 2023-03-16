#input
filename = input("File name: ")
filename = filename.lower()

#  document identification
if ".gif" in filename:
    print("image/gif")
elif ".jpg" in filename:
    print("image/jpeg")
elif ".png" in filename:
    print("image/png")
elif ".pdf" in filename:
    print("application/pdf")
elif ".txt" in filename:
    print("text/plain")
elif ".zip" in filename"
    print("application/x-7z-compressed")