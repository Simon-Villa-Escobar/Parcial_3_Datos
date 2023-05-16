import csv

canciones = []
cola_espera = []
artistas_dict = {}
titulos_dict = {}
generos_dict = {}
anos_dict = {}



class Cancion:
    def __init__(self, num, titulo ,artista, genero,ano, bpm, nrgy, dnce, dB, live, val, dur, acous, spch, pop):
        self.num = num
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.ano = ano
        self.bpm = bpm
        self.nrgy = nrgy
        self.dnce = dnce
        self.dB = dB
        self.live = live
        self.val = val
        self.dur = dur
        self.acous = acous
        self.spch = spch
        self.pop = pop

    def __str__(self):
        return "# " + self.num + ", Titulo: " + self.titulo + ", Artista: " + self.artista + ", Genero: " + self.genero + ", Año: " + self.ano + ", bpm: " + self.bpm + ",nrgy: " + self.nrgy + ",dnce " + self.dnce + ", dB: " + self.dB + ", live: " + self.live + ", val: " + self.val + ", dur: " + self.dur + ", acous: " + self.acous + ", spch: " + self.spch + ", pop: " + self.pop




def agregar_cancion():
    num = input("Ingrese el numero de la cancion: ")
    titulo = input("Ingrese el titulo de la cancion: ")
    artista = input("Ingrese el artista de la cancion: ")
    genero = input("Ingrese el genero de la cancion: ")
    ano = input("Ingrese el ano de la cancion: ")
    bpm = input("Ingrese el bpm de la cancion: ")
    nrgy = input("Ingrese el nrgy de la cancion: ")
    dnce = input("Ingrese el dnce de la cancion: ")
    dB = input("Ingrese el dB de la cancion: ")
    live = input("Ingrese el live de la cancion: ")
    val = input("Ingrese el val de la cancion: ")
    dur = input("Ingrese el dur de la cancion: ")
    acous = input("Ingrese el acous de la cancion: ")
    spch = input("Ingrese el spch de la cancion: ")
    pop = input("Ingrese el pop de la cancion: ")
    cancion = Cancion(num, titulo, artista, genero, ano, bpm, nrgy, dnce, dB, live, val, dur, acous, spch, pop)
    canciones.insert(int(num) - 1, cancion)
    for i in range(int(num), len(canciones)):
        canciones[i].num = str(int(canciones[i].num) + 1)

def cargar_canciones():
    canciones = []
    with open('top10s.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)  # Saltar la fila de encabezado
        for fila in lector_csv:
            cancion = Cancion(fila [0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11], fila[12], fila[13], fila[14])
            canciones.append(cancion)
    return canciones


def eliminar_cancion():
    num = int(input("Ingrese el número de la canción que desea eliminar: "))
    canciones.pop(num - 1)
    for i in range(num - 1, len(canciones)):
        canciones[i].num = i + 1



def mostrar_canciones():
    for cancion in canciones:
        print(cancion.__str__())

def lista_espera():
    num = input("Ingrese el número de la canción que quieres escuchar o agregar a la lista de espera: ")
    cancion = canciones[int(num) - 1]

    # Actualizar diccionarios
    artista = cancion.artista
    if artista in artistas_dict:
        artistas_dict[artista] += 1
    else:
        artistas_dict[artista] = 1

    titulo = cancion.titulo
    if titulo in titulos_dict:
        titulos_dict[titulo] += 1
    else:
        titulos_dict[titulo] = 1

    genero = cancion.genero
    if genero in generos_dict:
        generos_dict[genero] += 1
    else:
        generos_dict[genero] = 1

    ano = cancion.ano
    if ano in anos_dict:
        anos_dict[ano] += 1
    else:
        anos_dict[ano] = 1

    # Agregar canción a la cola de espera
    cola_espera.append(cancion)

    print("Canción agregada exitosamente!")


def mostrar_lista_espera():
    for cancion in cola_espera:
       print(cancion.__str__())


def imprimir_top_titulos():
    top_titulos = sorted(titulos_dict.items(), key=lambda x: x[1], reverse=True)
    num_elementos = min(len(top_titulos), 5)
    for i in range(num_elementos):
        titulo, num_reproducciones = top_titulos[i]
        print(f"Has escuchado '{titulo}' {num_reproducciones} veces")

def imprimir_top_artistas():
    top_artistas = sorted(artistas_dict.items(), key=lambda x: x[1], reverse=True)
    num_elementos = min(len(top_artistas), 5)
    for i in range(num_elementos):
        artista, num_reproducciones = top_artistas[i]
        print(f"Has escuchado al artista '{artista}' {num_reproducciones} veces")

def imprimir_top_generos():
    top_generos = sorted(generos_dict.items(), key=lambda x: x[1], reverse=True)
    num_elementos = min(len(top_generos), 5)
    for i in range(num_elementos):
        genero, num_reproducciones = top_generos[i]
        print(f"Has escuchado el género '{genero}' {num_reproducciones} veces")

def imprimir_top_anos():
    top_anos = sorted(anos_dict.items(), key=lambda x: x[1], reverse=True)
    num_elementos = min(len(top_anos), 5)
    for i in range(num_elementos):
        ano, num_reproducciones = top_anos[i]
        print(f"Has escuchado canciones del año {ano} {num_reproducciones} veces")







if __name__ == '__main__':
    canciones = cargar_canciones()

    while True:
        print("\n\nBienvenido al reproductor de canciones:")
        print("1. Agregar canción a la lista general")
        print("2. Eliminar canción de la lista general")
        print("3. Mostrar canciones")
        print("4. Escuchar canción o agregar a la lista de escucha")
        print("5. Mostrar lista de escucha")
        print("6. Mostrar top 5 (Según lo que desee)")
        print("7. Salir")

        opcion = input("\nIngrese una opcion: ")

        if opcion == "1":
            agregar_cancion()
            print("Canción agregada exitosamente!")
        elif opcion == "2":
            eliminar_cancion()
            print("Canción eliminada exitosamente!")
        elif opcion == "3":
            mostrar_canciones()
        elif opcion == "4":
            lista_espera()
        elif opcion == "5":
            mostrar_lista_espera()
        elif opcion == "6":
            d = input("¿Desea ver el top de 1.Canciones, 2.Artistas, 3.Géneros o 4.Años?: ")
            if d == "1":
                imprimir_top_titulos()
            elif d == "2":
                imprimir_top_artistas()
            elif d == "3":
                imprimir_top_generos()
            elif d == "4":
                imprimir_top_anos()
        elif opcion == "7":
            print("¡Gracias por usar el reproductor de canciones!")
            break
        else:
            print("Opción inválida, por favor ingrese una opción válida.")
