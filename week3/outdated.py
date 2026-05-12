meses = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


dia = '0'
mes = '0'
ano = '0'

while(True):
    try:
        data = input("date: ")

        if "/" in data:
            mes, dia, ano = data.split("/")

            if mes in [str(i) for i in range(1,12)]:
                if dia in [str(j) for j in range(1, 32)]:
                    if int(ano) > 0:
                        mes = int(mes)
                        dia = int(dia)
                        ano = int(ano)

                        print(f"{ano}-{mes:02}-{dia:02}")
                        break
                    else: continue
                else: continue
            else: continue

        else:

            if "," not in data:
                continue
            
            mes, dia, ano = data.replace(",", "").split()

            if mes in meses:
                if dia in [str(j) for j in range(1, 32)]:
                    if int(ano) > 0:
                        dia = int(dia)
                        ano = int(ano)

                        mes = meses.index(mes) + 1
                        print(f"{ano}-{mes:02}-{dia:02}")
                        break
                    else: continue
                else: continue
            else: continue

        

    except ValueError:
        pass
