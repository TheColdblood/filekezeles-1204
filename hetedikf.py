def hetedik():
    lista = []
    befile = open("fileok/dal.txt", "r", encoding="utf-8")
    for sor in befile:
        lista.append(sor.strip())
    befile.close()

    kifile = open("fileok/hetedik.txt", "w", encoding="utf-8")
    for index in range(len(lista)-1, -1, -1):
        print(lista[index])
        print(lista[index], file=kifile)
    kifile.close()
