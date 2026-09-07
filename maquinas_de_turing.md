# Diseño de Máquinas de Turing

Este documento detalla el diseño de Máquinas de Turing para dos tipos de lenguajes formales: un lenguaje regular y un lenguaje independiente del contexto. Ambos diseños asumen una cinta infinita, el uso del símbolo $\Delta$ (o espacio en blanco) para delimitar las cadenas, y la finalización en un estado de aceptación ($q_{acc}$).

---

## 1. Lenguaje Regular: $L = a^+b^+$

El lenguaje regular $L = a^+b^+$ acepta cadenas compuestas por **al menos una letra 'a' seguida de al menos una letra 'b'** (por ejemplo: `ab`, `aabb`, `abbb`).

Dado que es un lenguaje regular, la Máquina de Turing actúa de forma similar a un Autómata Finito Determinista (AFD): realiza una lectura secuencial de izquierda a derecha, transita entre estados, y no tiene necesidad de reescribir la cinta ni retroceder el cabezal.

### Tabla de Transiciones

| Estado Actual | Símbolo Leído | Símbolo Escrito | Movimiento | Nuevo Estado | Descripción del Paso |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **$q_0$** (Inicio) | $a$ | $a$ | $R$ (Derecha) | **$q_1$** | Lee la primera 'a' (obligatoria). |
| **$q_1$** | $a$ | $a$ | $R$ (Derecha) | **$q_1$** | Ciclo: Permite múltiples 'a' adicionales. |
| **$q_1$** | $b$ | $b$ | $R$ (Derecha) | **$q_2$** | Lee la primera 'b' (obligatoria). |
| **$q_2$** | $b$ | $b$ | $R$ (Derecha) | **$q_2$** | Ciclo: Permite múltiples 'b' adicionales. |
| **$q_2$** | $\Delta$ (Blanco)| $\Delta$ | $R$ (Derecha) | **$q_{acc}$** (Aceptación)| Fin de cadena, acepta el formato correcto. |

> *Nota:* Cualquier transición no definida explícitamente en la tabla (por ejemplo, leer una 'b' estando en el estado inicial $q_0$) conduce a la finalización de la máquina y al rechazo automático de la cadena.

### Representación Gráfica (Espacios para Imágenes)

<!-- REEMPLAZAR ESTAS RUTAS CON LAS RUTAS REALES DE TUS IMÁGENES -->

> **[Espacio para Imagen 1]**
> ![Diagrama de Transiciones del Lenguaje Regular](ruta_a_imagen_1.jpg)
> *Descripción sugerida: Diagrama de estados (grafos) para el lenguaje regular.*

> **[Espacio para Imagen 2]**
> ![Ejemplo de Cinta o Traza de Ejecución](ruta_a_imagen_2.jpg)
> *Descripción sugerida: Traza en cinta de una cadena válida como 'aabb'.*

---

## 2. Lenguaje Independiente del Contexto: $L = \{a^n b^n \mid n \ge 1\}$

El lenguaje $L = \{a^n b^n \mid n \ge 1\}$ requiere que exista **exactamente la misma cantidad de letras 'a' que de letras 'b'**, y que todas las 'a' precedan al bloque de 'b' (por ejemplo: `ab`, `aabb`, `aaabbb`).

A diferencia de un autómata finito, una Máquina de Turing puede "contar" utilizando la cinta como memoria. El algoritmo clásico consiste en:
1. Marcar una 'a' con una $X$.
2. Mover el cabezal hacia la derecha buscando su 'b' correspondiente y marcarla con una $Y$.
3. Regresar el cabezal a la izquierda hasta encontrar la última marca $X$.
4. Repetir el ciclo hasta que no queden letras sin emparejar y verificar que la cinta quede limpia.

### Tabla de Transiciones

| Estado Actual | Símbolo Leído | Símbolo Escrito | Movimiento | Nuevo Estado | Propósito de la Transición |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **$q_0$** | $a$ | $X$ | $R$ (Derecha) | **$q_1$** | Marca la 'a' actual y comienza la búsqueda de su 'b'. |
| **$q_0$** | $Y$ | $Y$ | $R$ (Derecha) | **$q_3$** | Si encuentra 'Y', ya no hay 'a'. Inicia fase de verificación final. |
| **$q_1$** | $a$ | $a$ | $R$ (Derecha) | **$q_1$** | Avanza a la derecha ignorando las 'a' restantes. |
| **$q_1$** | $Y$ | $Y$ | $R$ (Derecha) | **$q_1$** | Avanza a la derecha ignorando las 'b' ya procesadas ($Y$). |
| **$q_1$** | $b$ | $Y$ | $L$ (Izquierda)| **$q_2$** | Encuentra y marca la 'b'. Cambia de dirección para regresar. |
| **$q_2$** | $a$ | $a$ | $L$ (Izquierda)| **$q_2$** | Regresa a la izquierda ignorando las 'a'. |
| **$q_2$** | $Y$ | $Y$ | $L$ (Izquierda)| **$q_2$** | Regresa a la izquierda ignorando las 'b' ya marcadas. |
| **$q_2$** | $X$ | $X$ | $R$ (Derecha) | **$q_0$** | Al encontrar la marca inicial, se mueve un paso a la derecha para reiniciar. |
| **$q_3$** | $Y$ | $Y$ | $R$ (Derecha) | **$q_3$** | Lee la cola de la cinta verificando que solo queden 'Y' (ninguna 'b' extra). |
| **$q_3$** | $\Delta$ | $\Delta$ | $R$ (Derecha) | **$q_{acc}$** | Llega al blanco al final de la cinta: ¡Cadena aceptada! |

### Representación Gráfica (Espacios para Imágenes)

<!-- REEMPLAZAR ESTAS RUTAS CON LAS RUTAS REALES DE TUS IMÁGENES -->

> **[Espacio para Imagen 3]**
> ![Diagrama de Transiciones del Lenguaje Indep. del Contexto](ruta_a_imagen_3.jpg)
> *Descripción sugerida: Diagrama completo de los 5 estados iterativos de la Máquina de Turing.*

> **[Espacio para Imagen 4]**
> ![Traza de Ejecución paso a paso](ruta_a_imagen_4.jpg)
> *Descripción sugerida: Cinta mostrando la sobrescritura paso a paso (ej. XaYb -> XXYY).*
