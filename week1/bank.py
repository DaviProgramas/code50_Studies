input = input("Greetings: ").lower().strip()

if input.startswith("hello"):
    print("$0")
elif input.startswith("h"):
    print("$20")
else:  
    print("$100")