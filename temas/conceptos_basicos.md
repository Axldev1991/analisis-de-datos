# Conceptos Básicos de Python para el Análisis de Datos

> **Materia**: Análisis de Datos (UTN)  
> **Cátedra**: Introducción al Análisis de Datos — Fernández, Luis Nahuel  
> **Documento generado mediante especificación SDD**

---

## Tabla de Contenidos
1. [Entorno de Trabajo y Filosofía de Python](#1-entorno-de-trabajo-y-filosofía-de-python)
2. [Tipos de Datos Primitivos y Variables](#2-tipos-de-datos-primitivos-y-variables)
3. [Estructuras de Datos Nativas](#3-estructuras-de-datos-nativas)
   - [3.1 Listas](#31-listas)
   - [3.2 Tuplas](#32-tuplas)
   - [3.3 Diccionarios](#33-diccionarios)
   - [3.4 Conjuntos (Sets)](#34-conjuntos-sets)
4. [Estructuras de Control de Flujo](#4-estructuras-de-control-de-flujo)
   - [4.1 Condicionales](#41-condicionales)
   - [4.2 Bucles (for, while)](#42-bucles-for-while)
   - [4.3 Comprensión de Listas (List Comprehensions)](#43-comprensión-de-listas-list-comprehensions)
5. [Funciones y Programación Funcional](#5-funciones-y-programación-funcional)
   - [5.1 Definición de Funciones](#51-definición-de-funciones)
   - [5.2 Funciones Lambda](#52-funciones-lambda)
   - [5.3 Map, Filter y Zip](#53-map-filter-y-zip)
6. [Módulos e Importación de Librerías](#6-módulos-e-importación-de-librerías)

---

## 1. Entorno de Trabajo y Filosofía de Python

Python es un lenguaje de programación interpretado, de alto nivel y multiparadigma, que se ha consolidado como el estándar *de facto* para la ciencia y el análisis de datos debido a su sintaxis clara y a su rico ecosistema de librerías numéricas y estadísticas.

### Entornos Interactivos
- **Jupyter Notebook / JupyterLab**: Entornos basados en web que permiten combinar texto enriquecido (Markdown), código ejecutable en bloques (*cells*) y renderizado gráfico directo.
- **Google Colab**: Plataforma en la nube basada en Jupyter brindada por Google, muy utilizada en la cátedra para la ejecución interactiva de algoritmos de datos sin requerir instalación local previa.

---

## 2. Tipos de Datos Primitivos y Variables

En Python, la asignación de variables es dinámica. No requiere declaración explícita de tipos.

| Tipo de Dato | Clase en Python | Ejemplo | Descripción |
| :--- | :---: | :---: | :--- |
| Entero | `int` | `42`, `-10` | Números enteros de precisión arbitraria |
| Flotante | `float` | `3.14159`, `2.0e-3` | Números de punto flotante de 64 bits |
| Cadena de texto | `str` | `"Análisis"`, `'UTN'` | Secuencia inmutable de caracteres Unicode |
| Booleano | `bool` | `True`, `False` | Valores lógicos |
| Nulo | `NoneType` | `None` | Ausencia explícita de valor |

```python
# Ejemplo de declaración y verificación de tipos
edad = 25
estatura = 1.75
nombre = "Mariana"
es_estudiante = True

print(type(edad))          # <class 'int'>
print(type(estatura))      # <class 'float'>
print(type(nombre))        # <class 'str'>
print(type(es_estudiante)) # <class 'bool'>
```

---

## 3. Estructuras de Datos Nativas

### 3.1 Listas
Las listas son colecciones ordenadas y **mutables** de elementos. Pueden contener tipos heterogéneos.

```python
# Creación e indexación
frutas = ["manzana", "banana", "naranja", "kiwi"]

# Indexación (0-based) y slicing [inicio:fin:paso]
print(frutas[0])       # 'manzana'
print(frutas[-1])      # 'kiwi' (último elemento)
print(frutas[1:3])     # ['banana', 'naranja']

# Métodos principales
frutas.append("pera")   # Agrega al final
frutas.insert(1, "uva") # Inserta en posición específica
frutas.remove("banana")# Elimina por valor
elemento = frutas.pop() # Elimina y retorna el último
```

### 3.2 Tuplas
Las tuplas son colecciones ordenadas e **inmutables**. Se definen mediante paréntesis `()`.

```python
dimensiones = (1920, 1080)
coordenadas = (-34.6037, -58.3816)

# Desempaquetado de tuplas (Tuple Unpacking)
latitud, longitud = coordenadas
print(f"Lat: {latitud}, Lon: {longitud}")
```

### 3.3 Diccionarios
Los diccionarios son estructuras de pares **clave-valor** (*key-value*), optimizadas para búsquedas rápidas mediante tablas hash.

```python
candidata = {
    "nombre": "Mariana",
    "cordialidad": 80,
    "presencia": 90,
    "idioma": 70
}

# Acceso y modificación
print(candidata["nombre"])          # 'Mariana'
print(candidata.get("edad", 0))      # Retorna valor por defecto (0) si no existe la clave

candidata["evaluada"] = True        # Agregar nueva clave
candidata["cordialidad"] = 85       # Modificar clave existente

# Iteración en diccionarios
for clave, valor in candidata.items():
    print(f"{clave}: {valor}")
```

### 3.4 Conjuntos (Sets)
Colecciones desordenadas de elementos **únicos** (sin duplicados). Útiles para operaciones algebraicas de conjuntos (unión, intersección, diferencia).

```python
juez1_aprobados = {"Mariana", "Maia", "Carla"}
juez2_aprobados = {"Maia", "Sabrina", "Carla"}

# Operaciones de conjuntos
ambos_jueces = juez1_aprobados.intersection(juez2_aprobados) # {'Maia', 'Carla'}
al menos_uno = juez1_aprobados.union(juez2_aprobados)        # {'Mariana', 'Maia', 'Carla', 'Sabrina'}
solo_juez1   = juez1_aprobados.difference(juez2_aprobados)   # {'Mariana'}
```

---

## 4. Estructuras de Control de Flujo

### 4.1 Condicionales

```python
puntaje = 85

if puntaje >= 90:
    calificacion = "Excelente"
elif puntaje >= 70:
    calificacion = "Aprobado"
else:
    calificacion = "Reprobado"
```

### 4.2 Bucles (for, while)

```python
# Bucle for con range() y enumerate()
candidatas = ["Mariana", "Maia", "Sabrina", "Daniela"]

for i, nombre in enumerate(candidatas, start=1):
    print(f"Candidata N°{i}: {nombre}")

# Bucle while
contador = 5
while contador > 0:
    contador -= 1
```

### 4.3 Comprensión de Listas (List Comprehensions)
Sintaxis concisa para construir listas a partir de iterables aplicando transformaciones y filtros.

$$\text{Sintaxis: } [\text{expresion} \text{ for } \text{item} \text{ in } \text{iterable} \text{ if } \text{condicion}]$$

```python
puntajes_originales = [80, 90, 60, 50, 70]

# Filtrar y transformar: aumentar 5 puntos a puntajes >= 70
puntajes_ajustados = [p + 5 for p in puntajes_originales if p >= 70]
# Resultado: [85, 95, 75]
```

---

## 5. Funciones y Programación Funcional

### 5.1 Definición de Funciones

```python
def calcular_promedio(puntajes, ponderacion=None):
    \"\"\"Calcula el promedio ponderado o simple de una lista de puntajes.\"\"\"
    if not puntajes:
        return 0.0
    if ponderacion is None:
        return sum(puntajes) / len(puntajes)
    return sum(p * w for p, w in zip(puntajes, ponderacion)) / sum(ponderacion)

# Llamada a la función
print(calcular_promedio([80, 90, 70])) # 80.0
```

### 5.2 Funciones Lambda
Funciones anónimas e inline de una sola línea.

```python
normalizar_z = lambda x, mu, sigma: (x - mu) / sigma if sigma != 0 else 0

print(normalizar_z(80, mu=70, sigma=10)) # 1.0
```

### 5.3 Map, Filter y Zip

```python
valores = [10, 20, 30, 40, 50]

# map(): Aplica una función a cada elemento
duplicados = list(map(lambda x: x * 2, valores)) # [20, 40, 60, 80, 100]

# filter(): Filtra elementos según una condición booleana
mayores_25 = list(filter(lambda x: x > 25, valores)) # [30, 40, 50]

# zip(): Empareja elementos de múltiples iterables
nombres = ["Mariana", "Maia"]
notas = [85, 92]
parejas = list(zip(nombres, notas)) # [('Mariana', 85), ('Maia', 92)]
```

---

## 6. Módulos e Importación de Librerías

Para la manipulación eficiente de datos, Python cuenta con módulos estándar (`math`, `os`, `sys`, `json`) y un ecosistema de librerías externas que se instalan vía `pip` o `conda`.

```python
# Importaciones estándar y convención del ecosistema de Data Science
import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(f"Versión de NumPy: {np.__version__}")
print(f"Versión de Pandas: {pd.__version__}")
```
