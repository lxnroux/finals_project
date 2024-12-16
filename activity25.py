def list():

    fruits = ["orange", "lime", "lemon", "grapefruit", "tangerine", "strawberry", "delete one", "delete two"]

    fruits.remove("delete one")
    fruits.pop()
    fruits.append("blueberry")
    fruits.insert(0, "banana")

    print(fruits)

list()