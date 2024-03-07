# Write your solution here

while True:
    name = input("editor: ")
    name =name.lower()

    if name == "notepad" or name == "word":
        print("awful")
    elif name == "visual studio code":
        print("an excellent choice!")
        break
    else: print("not good")

