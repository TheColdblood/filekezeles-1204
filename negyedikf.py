def negyedik():
    lista = []
    befile = open("fileok/dal.txt", "r", encoding="utf-8")
    for sor in befile:
        lista.append(sor.strip())
    befile.close()

    kifile = open("fileok/negyedik.txt", "w", encoding="utf-8")
    for index in range(0, len(lista), 1):

        daraboltsor = lista[index].split(" ")

        print(daraboltsor[0], file=kifile)
        #kifile.write(lista[index])
    kifile.close()
