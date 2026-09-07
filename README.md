# TPs - Teoría de la Computación / Computabilidad y Complejidad
## Alumno: Di Salvo, Tobías

## TP 1: Información de Alan Turing

El primer TP consiste en buscar la información de un científico que haya aportado a el área de la computación. En mi caso, me toco investigar sobre **Alan Turing**

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