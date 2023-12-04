def masodik():
    lista = []
    befile = open("fileok/dal.txt", "r", encoding="utf-8")
    for sor in befile:
        lista.append(sor.strip())
    befile.close()

    #lista kiirás
    for index in range(0, len(lista), 1):
        print(lista[index],end="")