
def lecturaArchivo(nombre):
    listaLIneas = []
    with open(nombre) as archivo:
        listaLIneas = archivo.readlines()

    