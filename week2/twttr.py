word = input("input: ")

for vowel in word:
    if vowel in "aeiouAEIOU":
        word = word.replace(vowel, "")

print("output: " + word)