def elso():
    befile = open("fileok/dal.txt", "r", encoding="utf-8")
    for sor in befile:
        print(sor.strip(), end="")
    befile.close()
