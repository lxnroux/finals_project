def Hello(name):
    print(f"Hello {name}")

while True:
    ask = input("Please provide a name: ").strip()
    if ask.upper() == "STOP":
        print("Goodbye!")
        break
    Hello(ask)
    