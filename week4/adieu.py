
import inflect

nomes = []
i = inflect.engine()

try:
    while(True):
        nome = input("nome: ")
        nomes += [nome]

except (EOFError, KeyboardInterrupt):
    print()
    print("adieu, adieu, to", i.join(nomes))
