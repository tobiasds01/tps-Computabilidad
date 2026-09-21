from bidict import bidict

simbolos = bidict({"0": "00", "1": "01", "b": "10"})
estados = bidict({"0": "0", "1": "1"})
movimientos = bidict({"R": "0", "L": "1"})
transiciones = ['0000010', '0010000', '0101101']

w = '01010101b'
estadoActual = '0'
posicionDelCabezal = 0

hayTransicion = True

def escribirCinta(entrada, estadoActual, caracterCodificado):
    print(f"{entrada}${estadoActual}{caracterCodificado}#{'#'.join(transiciones)}")

def procesarTransicion(transicion, diccionario):
    caracter = transicion[0]
    elemento = None
    while elemento is None and len(transicion) > 0:
        transicion = transicion[1:]
        if caracter in diccionario.inverse:
            elemento = diccionario.inverse[caracter]
        else:
            caracter += transicion[0]
    return elemento, transicion

def realizarMovimientoDelCabezal(direccion):
    global posicionDelCabezal
    if direccion == "R":
        posicionDelCabezal += 1
    elif direccion == "L":
        posicionDelCabezal -= 1
    else:
        posicionDelCabezal = posicionDelCabezal

print(f"Palabra inicial: {w}")
print("")

while hayTransicion:
    caracterActual = w[posicionDelCabezal]
    caracterCodificado = simbolos[caracterActual]
    estadoCodificado = estados[estadoActual]

    transicionEncontrada = next((t for t in transiciones if t.startswith(estadoCodificado + caracterCodificado)), None)
    hayTransicion = transicionEncontrada is not None

    if hayTransicion:
        w = w[:posicionDelCabezal] + "*" + w[posicionDelCabezal + 1:]
        escribirCinta(w, estadoCodificado, caracterCodificado)

        transicionEncontrada = transicionEncontrada[len(estadoCodificado + caracterCodificado):]

        estadoActual, transicionEncontrada = procesarTransicion(transicionEncontrada, estados)
        simboloAEscribir, transicionEncontrada = procesarTransicion(transicionEncontrada, simbolos)
        direccionMovimiento, transicionEncontrada = procesarTransicion(transicionEncontrada, movimientos)

        w = w[:posicionDelCabezal] + simboloAEscribir + w[posicionDelCabezal + 1:]
        realizarMovimientoDelCabezal(direccionMovimiento)
    else:
        wFinal = w[:posicionDelCabezal] + "*" + w[posicionDelCabezal + 1:]
        escribirCinta(wFinal, estadoCodificado, caracterCodificado)

print("")
print(f"Palabra final: {w}")


"""
leer el primer caracter
lo codifico -> 01
escribo la codificacion en la cinta

w sin caracterActual $ estadoActual caracterCodificado # transiciones 

*0011b$001#0000010#0010000#0101101

busco una transicion que empiece como mi estadoActual + caracterCodificado
lo quito de mi cadena

si hay transición

    agarro el primer caracter = estado siguiente.
    Busco si lo encuentro como key en estados, si lo encuentro, actualizo mi estadoActual, sino agarro dos caracteres.

    Agarro el primer caracter = símbolo a escribir.
    Busco si lo encuentro como key en simbolos, si lo encuentro, escribo el valor en la cinta, sino agarro dos caracteres.

    Agarro el primer caracter = dirección del movimiento.
    Busco si lo encuentro como key en movimientos, si lo encuentro, actualizo la posición del cabezal, sino agarro dos caracteres.



"""