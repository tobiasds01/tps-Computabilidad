# TPs - Teoría de la Computación / Computabilidad y Complejidad
## Alumno: Di Salvo, Tobías

## TP 1: Información de Alan Turing

El primer TP consiste en buscar la información de un científico que haya aportado a el área de la computación. En mi caso, me toco investigar sobre Alan Turing**

![Foto Alan Turing](/Alan_turing_header.jpg)
* **NOMBRE COMPLETO:** Alan Mathison Turing
* **FECHA DE NACIMIENTO:** 23/06/1912
* **FECHA DE FALLECIMIENTO:** 07/06/1954
* **NACIONALIDAD:** Británica
* **APORTE PRINCIPAL:** Máquina de Turing
* **FECHA APORTE PRINCIPAL:** 1936 en "On Computable Numbers".
* **APORTES:** Primer diseño del ACE (computadora digital), descifrar los códigos de la máquina enigma, Tesis Church-Turing, prueba de Turing. Se lo considera el padre de las ciencias de la computación.
* **EDUCACIÓN:** Matemática - Universidad de Cambridge (1931-1934) / Doctorado en Matemática - Universidad de Princeton (1937-1938)
* **OCUPACIÓN:** Informático teórico y criptógrafo
* **RECONOCIMIENTOS:** Premio Smith (1936), Oficial de la Orden del Imperio Británico (1946), Miembro de la Royal Society (1951)
* **CONCEPTO CON SU NOMBRE:** Máquina de Turing, prueba de Turing, tesis Church-Turing, premio Alan Turing
* **ÁREA:** Criptoanálisis, ciencias de la computación, matemáticas, lógica y criptografía
* **APLICACIÓN:** Sus teorías dieron origen a las ciencias de la computación, definió el concepto de Algoritmo y Computabilidad lo que hoy se utiliza para conocer qué problemas pueden resolverse con algoritmos. Todos los microprocesadores tienen una base en el primer diseño del ACE. La evaluación de modelos de LLM y las primeras ideas para sus diseños nacieron de sus pruebas.
* **CURIOSIDAD:** Turing fue procesado por homosexualidad en 1952 luego de todos los aportes que había realizado. En 2009, el primer ministro británico se disculpó públicamente en nombre del gobierno británico por «la forma espantosa en la que Turing había sido tratado». El término «ley Alan Turing» ahora se usa de manera informal para referirse a una ley de 2017 en el Reino Unido que perdona retroactivamente a hombres amonestados o condenados en virtud de la legislación que prohibía los actos homosexuales.

**Link a la hoja de cálculo:**
[Científicos](https://docs.google.com/spreadsheets/d/19Bz7HpqyY465uTSSMZl_xUvJH9eviDKqdAx2mwPVTQA/edit?gid=0#gid=0)

## TP 2: Prueba de la máquina de ejemplo

En el TP 2 debíamos probar la máquina de turing de ejemplo que funcionaba para duplicar 1s. Consiste en pasarle como entrada una cantidad de 1s y, luego del cómputo, en la cinta nos quedarían el doble de 1s de esa cantidad.

### Entradas:
### 1
![Prueba de cinta con un solo 1](/TP2-Maq_turing/Captura%20de%20pantalla%202026-08-30%20195653.png)

### 11
![Prueba de cinta con dos 1](/TP2-Maq_turing/Captura%20de%20pantalla%202026-08-30%20195741.png)

### 111
![Prueba de cinta con tres 1](/TP2-Maq_turing/Captura%20de%20pantalla%202026-08-30%20195815.png)

### 1111
![Prueba de cinta con cuatro 1](/TP2-Maq_turing/Captura%20de%20pantalla%202026-08-30%20195848.png)

### 11111
![Prueba de cinta con cinco 1](/TP2-Maq_turing/Captura%20de%20pantalla%202026-08-30%20195946.png)

Como vemos, la máquina funcionó perfecto. Para cada entrada, al finalizar, en la cinta podemos ver el doble de 1s.

## TP 3: Máquina de Turing para LR y LIC

### 1. Lenguaje Regular: $L = a^+b^+$

El lenguaje regular $L = a^+b^+$ acepta cadenas compuestas por **al menos una letra 'a' seguida de al menos una letra 'b'** (por ejemplo: `ab`, `aabb`, `abbb`).

### Tabla de Transiciones

| $\delta$ | $a$ | $b$ | $\square$ |
| --- | --- | --- | --- |
| **$>q0$** | $(q1, a, R)$ | - | - |
| **$q1$** | $(q1, a, R)$ | $(q2, b, R)$ | - |
| **$q2$** | - | $(q2, b, R)$ | $(q3, \square, S)$ |
| **$*q3$** | - | - | - |

### Representación Gráfica (Grafos)


![Diagrama de Transiciones del Lenguaje Regular](/TP3-Turing_para_Regular_e_Indep/Maq_lenguaje_regular.png)

![Resultados](/TP3-Turing_para_Regular_e_Indep/Maq_lenguaje_regular-Resultados.png)

---

### 2. Lenguaje Independiente del Contexto: $L = \{a^n b^{2n} \mid n \ge 1\}$

El lenguaje $L = \{a^n b^{2n} \mid n \ge 1\}$ exige que por cada letra 'a', existan **exactamente dos** letras 'b' (por ejemplo: `abb`, `aabbbb`, `aaabbbbbb`).

### Tabla de Transiciones

| $\delta$ | $a$ | $b$ | $X$ | $Y$ | $\square$ |
| --- | --- | --- | --- | --- | --- |
| **$>q0$** | $(q1, X, R)$ | - | - | $(q4, Y, R)$ | - |
| **$q1$** | $(q1, a, R)$ | $(q2, Y, R)$ | - | $(q1, Y, R)$ | - |
| **$q2$** | - | $(q3, Y, L)$ | - | $(q2, Y, R)$ | - |
| **$q3$** | $(q3, a, L)$ | - | $(q0, X, R)$ | $(q3, Y, L)$ | - |
| **$q4$** | - | - | - | $(q4, Y, R)$ | $(q5, \square, S)$ |
| **$*q5$** | - | - | - | - | - |

### Representación Gráfica (Espacios para Imágenes)

<!-- REEMPLAZAR ESTAS RUTAS CON LAS RUTAS REALES DE TUS IMÁGENES -->

> ![Diagrama de Transiciones del Lenguaje Indep. del Contexto](/TP3-Turing_para_Regular_e_Indep/Maq_lenguaje_indep.png)

> ![Resultados](/TP3-Turing_para_Regular_e_Indep/Maq_lenguaje_indep-Resultados.png)

### Diferencias entre máquinas de aceptación y de cálculo

La diferencia fundamental entre una Máquina de Turing de aceptación y una de cálculo radica en el objetivo de su ejecución. Por un lado, la primera funciona como un **validador** que **indica si una cadena pertenece a un lenguaje determinado**, llegando a un estado de aceptación o rechazo sin importar demasiado lo que quede escrito en la cinta. Por otro lado, la segunda actúa como una **calculadora** o procesador de datos, y su finalidad es **transformar una entrada** inicial para dejar guardado en la cinta el resultado final de una función.







## TP5: Máquina de Turing Universal

**Ej. 1: ¿Por qué se dice que una MTU es capaz de simular cualquier Máquina de Turing?**
> Se dice que una MTU es capaz de simular cualquier máquina de turing ya que lo que hace es replicar el funcionamiento de la máquina que nosotros le pasemos por parámetro. Al aplicar ciertas transformaciones, lo que hará siempre es recorrer la cinta, pero nosotros somos quienes le indican de qué manera hacerlo con nuestro diseño pasado como parámetro junto con la entrada que vamos a computar. Entonces, siguiendo los mismos pasos siempre podemos representar todos los estados y transiciones iguales que cualquier otra máquina.

---

**Ej. 2: Suponer que se tiene una MT _M_ que acepta todas las cadenas que terminan en 01. Indicar qué debería hacer una MTU con las siguientes entradas. Explicar en cada caso si la MTU acepta o rechaza y por qué**

**U(⟨M⟩,1101)**  
**U(⟨M⟩,100)**  
**U(⟨M⟩,01)**  
**U(⟨M⟩,111)**

> Lo que va a hacer es transformar las transiciones descritas en _M_ y hacer el proceso desde su propia cinta, emulando el comportamiento de _M_. Irá recorriendo las entradas y siguiendo las transiciones hasta llegar a un estado de aceptación o no. En caso de llegar, la entrada será aceptada. En caso contrario, será rechazada o no se llegará a un resultado definido (si no para nunca).
>
> 1. **U(⟨M⟩,1101)** - La MTU va a aceptar la entrada, recorrerá las transiciones hasta observar que el final de la cadena contiene el 01.
> 2. **U(⟨M⟩,100)** - La MTU va a rechazar la entrada, porque al llegar al final de la cadena no tendrá una transición de 00 a un estado final.
> 3. **U(⟨M⟩,01)** - La MTU va a aceptar la entrada, recorrerá las transiciones hasta observar que el final de la cadena contiene el 01.
> 4. **U(⟨M⟩,111)** - La MTU va a rechazar la entrada, porque al llegar al final de la cadena no tendrá una transición de 11 a un estado final.

---

**Ej. 3: Dada la siguiente MT _M_:**

<div align="center">

| Q  |     0    |     1    |
|:--:|:--------:|:--------:|
| q0 | (q1,1,R) | (q1,0,R) |
| q1 | (qf,0,R) | (qf,1,R) |
| qf |     -    |     -    |

</div>

1. Explicar que hace _M_
2. Explicar qué información debería recibir una MTU para poder simular M
3. Codificar la cintar de MTU sabiendo que configuración de la cinta de MT M es 1 q0 0 1 1

> 1. La máquina _M_ intercambia el primer bit de la palabra. Si hay un 0, escribe un 1. Si hay un 1, escribe un 0. Además, la palabra debe tener al menos 2 símbolos.
> 2. La MTU debería recibir la información de la máquina _M_ con sus transiciones y una palabra que computar. Por ejemplo, U(⟨M⟩, 001).
> 3. Símbolos: `0 = 0`, `1 = 1`  
>  Estados: `q0 = 00`, `q1 = 01`, `q2 = 10`  
>  Movimientos: `R = 0`, `L = 1` 

---
**Ej. 4: Realizar una máquina de Turing Universal**

1. **Codificación de una máquina simple**
    * **Definir una máquina que ...**
    * **Codificar sus estados, símbolos y transiciones en forma numérica**

> Se realizará una máquina de Turing que invierta todos los bits de la cadena  
> _M_ = {  
>> $\Gamma$ = {0, 1, &EmptySmallSquare;},  
> $\Sigma$ = {0, 1},  
> _b_ = &EmptySmallSquare;,  
> _Q_ = {q0, q1},  
> _q0_ = q0,  
> _F_ = {q1},  
> $\delta$  
>
>}
>
> <div align="center">
>
> | Q  |     0    |     1    |    &EmptySmallSquare;     |
> |:--:|:--------:|:--------:|:-------------------------:|
> | q0 | (q0,1,R) | (q0,0,R) | (q1,&EmptySmallSquare;,L) |
> | q1 |     -    |     -    |             -             |
> </div>

>  Símbolos: `0 = 00`, `1 = 01`, `▢ = 10`  
>  Estados: `q0 = 0`, `q1 = 1`  
>  Movimientos: `R = 0`, `L = 1` 
> <div align="center">
>
> | Q  |     0    |     1    |    &EmptySmallSquare;     |
> |:--:|:--------:|:--------:|:-------------------------:|
> | 0 | 0010 | 0000 | 1101 |
> | 1 |   -  |   -  |   -  |
> </div>
>
> Entonces, la cinta quedaría algo así (siendo los ... la entrada a procesar)
> `...0000010#0010000#0101101`
>
> Para la entrada `10011b` la cinta quedaría así:
> `*0011b$001#0000010#0010000#0101101`

2. **Simulación básica**
    * **Implementar en Python un programa que reciba:**
        * **La codificación de una máquina _M_**
        * **Una cadena de entrada _w_**
    * **El programa debe simular paso a paso la ejecución de _M_ sobre _w_**

> El programa puede verse en el siguiente link: [mtu.py](TP5-MTU/mtu.py)

Explicando un poco el código, este es el formato de máquina que vamos a utilizar:

Importamos la librería **_bidict_** para agilizar algunas acciones. Esa estructura de datos no es más que un diccionario que funciona en ambas direcciones (ya que tanto la codificación como los elemenos son únicos, no habrá margen de error). Deberemos construír la máquina con las siguiente estructura:  
* **Símbolos:** las claves deben ser los símbolos de la cinta y los valores sus codificaciones.
* **Estados:** tanto las claves como los valores deberán ser los estados YA CODIFICADOS.
* **Movimientos:** las claves serán las letras (R, L y S, a medida que sea necesario) y los valores sus codificaciones.

De esta manera garantizamos que las transformaciones funcionen correctamente.

```python
from bidict import bidict

simbolos = bidict({"0": "00", "1": "01", "b": "10"})
estados = bidict({"0": "0", "1": "1"})
movimientos = bidict({"R": "0", "L": "1"})
transiciones = ['0000010', '0010000', '0101101']

w = '10011b'
estadoActual = '0'
posicionDelCabezal = 0
```
<br>
Funciones auxiliares para hacer los prints en pantalla, procesar correctamente la transición identificando correctamente sus elementos y mover el cabezal.

```python
def escribirCinta(entrada, estadoActual, caracterCodificado)

def procesarTransicion(transicion, diccionario)

def realizarMovimientoDelCabezal(direccion)
```
<br>
Realizamos el algoritmo para la MTU. Primero obtendremos la información necesaria para el procesamiento (el símbolo codificado y el estado codificado). Luego buscamos la transición correspondiente.

```python
while hayTransicion:
    caracterActual = w[posicionDelCabezal]
    caracterCodificado = simbolos[caracterActual]
    estadoCodificado = estados[estadoActual]

    transicionEncontrada = next((t for t in transiciones if t.startswith(estadoCodificado + caracterCodificado)), None)
    hayTransicion = transicionEncontrada is not None
```
<br>
Escribimos cómo está la cinta en este momento. Si hay transición, obtenemos el próximo estado, el símbolo que se va a escribir en la palabra y la dirección a la que debe moverse el cabezal. Luego actualizamos la palabra y el cabezal. Repetiremos el proceso (`while hayTransicion:`) hasta no encontrar una transición disponible.

```python
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
```

3. **Pruebas de funcionamiento**
    * **Probar la simulación con diferentes entradas**
    * **Documentar los resultados**

Para probar la simulación, utilizaremos las entradas `01b`, `111b`, `10011b`, `000111b`, `01010101b`

4. **Informe final**
    * **Explicar la codificación utilizada**
    * **Mostrar ejemplos de ejecución**
    * **Reflexionar sobre la relación entre la MTU y las computadoras modernas**

Se utilizó la codificación de esta manera:
* Símbolos: ``0 = 00``, ``1 = 01``, ``▢ = 10``
* Estados: ``q0 = 0``, ``q1 = 1``
* Movimientos: ``R = 0``, ``L = 1``

En este caso, los símbolos se codificaron con 2 bits ya que había tres para leer y con un solo bit solo podemos representar dos valores. Luego, como tanto los estados como los movimientos solo queremos representar dos, sí se utilizó un único bit. Entonces, al codificar las transiciones se conformaron de esta manera (para el ejemplo `0010000`):
* Estado: primer bit (`0`).
* Símbolo leído: segundo y tercer bit (`01`).
* Estado al que nos movemos: cuarto bit (`0`).
* Símbolo que escribimos: quinto y sexto bit (`00`).
* Dirección del cabezal: séptimo bit (`0`).

Entonces estamos en el estado _q0_ (`0`), leímos un _1_ (`01`), nos movemos al estado _q0_ (`0`), escribimos el símbolo 0 (`00`) y nos movemos a la derecha (`0`).  
`0` `01` `0` `00` `0`


Para `01b`

```
Palabra inicial: 01b

*1b$000#0000010#0010000#0101101
1*b$001#0000010#0010000#0101101
10*$010#0000010#0010000#0101101
1*b$100#0000010#0010000#0101101

Palabra final: 10b
```

Para `111b`
```
Palabra inicial: 111b

*11b$001#0000010#0010000#0101101
0*1b$001#0000010#0010000#0101101
00*b$001#0000010#0010000#0101101
000*$010#0000010#0010000#0101101
00*b$100#0000010#0010000#0101101

Palabra final: 000b
```

Para `10011b`

```
Palabra inicial: 10011b

*0011b$001#0000010#0010000#0101101
0*011b$000#0000010#0010000#0101101
01*11b$000#0000010#0010000#0101101
011*1b$001#0000010#0010000#0101101
0110*b$001#0000010#0010000#0101101
01100*$010#0000010#0010000#0101101
0110*b$100#0000010#0010000#0101101

Palabra final: 01100b
```

Para `000111b`

```
Palabra inicial: 000111b

*00111b$000#0000010#0010000#0101101
1*0111b$000#0000010#0010000#0101101
11*111b$000#0000010#0010000#0101101
111*11b$001#0000010#0010000#0101101
1110*1b$001#0000010#0010000#0101101
11100*b$001#0000010#0010000#0101101
111000*$010#0000010#0010000#0101101
11100*b$100#0000010#0010000#0101101

Palabra final: 111000b
```

Para `01010101b`

```
Palabra inicial: 01010101b

*1010101b$000#0000010#0010000#0101101
1*010101b$001#0000010#0010000#0101101
10*10101b$000#0000010#0010000#0101101
101*0101b$001#0000010#0010000#0101101
1010*101b$000#0000010#0010000#0101101
10101*01b$001#0000010#0010000#0101101
101010*1b$000#0000010#0010000#0101101
1010101*b$001#0000010#0010000#0101101
10101010*$010#0000010#0010000#0101101
1010101*b$100#0000010#0010000#0101101

Palabra final: 10101010b
```