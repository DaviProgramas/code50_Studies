import sys
from random import choice
from pyfiglet import Figlet

fontes = Figlet().getFonts()

if len(sys.argv) == 1:
    fonte = choice(fontes)

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f","--font"]:
       sys.exit("wrong argv input")
    
    if sys.argv[2] in fontes:
        fonte = sys.argv[2]
    else:
        sys.exit("unavaible font")
else:
    sys.exit("wrong argv input")


figlet = Figlet(font = fonte)

text = input("Input: ")
print("Output\n", figlet.renderText(text))

