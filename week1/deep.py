def main():
    answer = input("what is the answer to the Great Question of Life, the Universe and Everything: ").lower().strip()
    match answer:
        case "42":
            print("yes")
        case "forty-two":
            print("yes")
        case "forty two":
            print("yes")
        case _:
            print("no")

main()