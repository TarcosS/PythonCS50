name = input("What is your name? ")

match name:
    case "Harry" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
        
