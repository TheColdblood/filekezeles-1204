def harmadik():
    lista = []
    befile = open("fileok/dal.txt", "r", encoding="utf-8")
    for sor in befile:
        lista.append(sor.strip())
    befile.close()

    kifile = open("fileok/harmadik.txt", "w", encoding="utf-8")
    for index in range(0, len(lista), 1):
        print(lista[index], file=kifile, end="")
        #kifile.write(lista[index])
    kifile.close()
