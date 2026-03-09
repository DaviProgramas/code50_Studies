def convert(phrase):
    return phrase.replace(":)", "🙂").replace(":(", "🙁")

def main():
    phrase = input()
    print(convert(phrase))

main()