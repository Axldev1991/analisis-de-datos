# Guía Completa de NumPy para el Análisis de Datos

> **Materia**: Análisis de Datos (UTN)  
> **Cátedra**: Introducción al Análisis de Datos — Fernández, Luis Nahuel  
> **Documento generado mediante especificación SDD**

---

## Tabla de Contenidos
1. [Introducción a NumPy y el `ndarray`](#1-introducción-a-numpy-y-el-ndarray)
2. [Funciones Generadoras de Arrays](#2-funciones-generadoras-de-arrays)
3. [Atributos de la Clase `numpy.ndarray`](#3-atributos-de-la-clase-numpyndarray)
4. [Métodos Principales de la Clase `numpy.ndarray`](#4-métodos-principales-de-la-clase-numpyndarray)
5. [Indexación, Slicing y Filtros Booleanos](#5-indexación-slicing-y-filtros-booleanos)
6. [Operaciones Vectorizadas y SIMD](#6-operaciones-vectorizadas-y-simd)
7. [Broadcasting (Difusión)](#7-broadcasting-difusión)
8. [Estadística Descriptiva y Agregación por Eje](#8-estadística-descriptiva-y-agregación-por-eje)
9. [Álgebra Lineal con `np.linalg`](#9-álgebra-lineal-con-nplinalg)
10. [Casos de Uso de NumPy](#10-casos-de-uso-de-numpy)

---

## 1. Introducción a NumPy y el `ndarray`

**NumPy** (*Numerical Python*) es la librería fundamental de código abierto para la computación científica, matricial y numérica en Python. 

Su objeto central es la clase **`numpy.ndarray`** (N-dimensional array), un contenedor homogéneo de datos almacenados en un bloque de memoria contiguo escrito en C para lograr alta eficiencia computacional y evitar los costos de la comprobación dinámica de tipos de las listas de Python.

### Características Generales (según material de cátedra):
- Desarrollada en lenguaje C para el trabajo con arrays multidimensionales y gran cantidad de información.
- Ofrece recursos para matemática, álgebra lineal y disciplinas científicas.
- Código abierto y multiplataforma.
- Sintaxis de alto nivel optimizada bajo altos estándares de calidad.

---

## 2. Funciones Generadoras de Arrays

NumPy proporciona funciones clave para la creación e inicialización de arrays:

| Función | Descripción | Ejemplo de Sintaxis |
| :--- | :--- | :--- |
| **`np.zeros()`** | Crea un array lleno de ceros según la cantidad de elementos o forma (*shape*). | `np.zeros(5)` o `np.zeros((3, 3))` |
| **`np.ones()`** | Crea un array lleno de unos. | `np.ones((2, 4), dtype=int)` |
| **`np.empty()`** | Crea un array sin inicializar (con valores aleatorios en el buffer de memoria). | `np.empty((2, 2))` |
| **`np.arange()`** | Adaptación de `range()` a NumPy. Permite dar pasos con decimales. | `np.arange(0, 10, 0.5)` |
| **`np.linspace()`** | Crea un array con un número exacto de elementos en un intervalo equiespaciado. | `np.linspace(0, 1, 5)` |
| **`np.sort()`** | Ordena los elementos de un array (por defecto en orden ascendente). | `np.sort(arr)` |
| **`np.concatenate()`** | Concatena dos o más arrays a lo largo de un eje especificado. | `np.concatenate((a, b), axis=0)` |
| **`np.expand_dims()`** | Agrega dimensiones adicionales al array (*expand dimensions*). | `np.expand_dims(arr, axis=0)` |

```python
import numpy as np

# Ejemplos de uso
cero_matriz = np.zeros((2, 3))
rango_decimal = np.arange(0, 5, 0.5)      # [0. , 0.5, 1. , 1.5, ... 4.5]
puntos = np.linspace(0, 100, 5)           # [0., 25., 50., 75., 100.]

# Ordenamiento y concatenación
desorden = np.array([4, 1, 7, 2])
ordenado = np.sort(desorden)              # [1, 2, 4, 7]

a = np.array([1, 2])
b = np.array([3, 4])
union = np.concatenate((a, b))            # [1, 2, 3, 4]
expansion = np.expand_dims(a, axis=0)     # Shape (1, 2)
```

---

## 3. Atributos de la Clase `numpy.ndarray`

A diferencia de las listas nativas de Python, un objeto `ndarray` tiene **tamaño fijo** y **elementos homogéneos del mismo tipo de dato**. Sus atributos principales son:

| Atributo | Descripción | Ejemplo / Retorno |
| :--- | :--- | :--- |
| **`ndim`** | Retorna el número de dimensiones del array. | `2` para matriz bidimensional |
| **`shape`** | Tupla con la cantidad de elementos en cada dimensión. | `(3, 4)` |
| **`dtype`** | Tipo de datos numéricos que contiene el array. | `int32`, `float64`, `bool` |
| **`size`** | Cantidad total de elementos contenidos en la matriz. | `12` para matriz (3, 4) |
| **`itemsize`** | Tamaño en bytes de cada elemento del array. | `8` bytes para `float64` |
| **`data`** | Buffer que contiene los elementos del array en memoria física. | `<memory at 0x...>` |
| **`T`** | Transpuesta del array (intercambia filas por columnas). | `arr.T` |

```python
matriz = np.array([[10, 20, 30], [40, 50, 60]], dtype=np.float64)

print("ndim:", matriz.ndim)       # 2
print("shape:", matriz.shape)     # (2, 3)
print("dtype:", matriz.dtype)     # float64
print("size:", matriz.size)       # 6
print("itemsize:", matriz.itemsize)# 8 bytes
print("data:", matriz.data)       # Buffer contiguo
print("Transpuesta:\n", matriz.T) # Shape (3, 2)
```

---

## 4. Métodos Principales de la Clase `numpy.ndarray`

| Método | Descripción | Ejemplo |
| :--- | :--- | :--- |
| **`flatten()`** | Convierte el array a una sola dimensión (1D) retornando una **copia en memoria**. | `arr.flatten()` |
| **`reshape()`** | Cambia la forma (*shape*) del array sin modificar sus datos (genera una **vista** si es contiguo). | `arr.reshape((3, 2))` |
| **`sum()`** | Devuelve la suma de los elementos (o a lo largo de un eje `axis`). | `arr.sum()` |
| **`mean()`** | Estima la media aritmética de los datos. | `arr.mean()` |
| **`std()`** | Estima la desviación estándar de los datos. | `arr.std()` |

---

## 5. Indexación, Slicing y Filtros Booleanos

### Slicing N-dimensional: `arr[filas, columnas]`
```python
matriz = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print(matriz[0, 1])      # Elemento fila 0, col 1 -> 20
print(matriz[:2, 1:3])   # Submatriz filas 0-1, cols 1-2
```

### Máscaras Booleanas (*Boolean Indexing*)
```python
datos = np.array([12, 45, 78, 23, 56, 89])
filtrados = datos[datos > 50] # [78, 56, 89]
```

---

## 6. Operaciones Vectorizadas y SIMD

Las operaciones numéricas se aplican elemento a elemento (*element-wise*):

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)     # [11, 22, 33]
print(a * b)     # [10, 40, 90]
print(a ** 2)    # [1, 4, 9]
```

A nivel de procesador (CPU), los registros de hardware ejecutados por NumPy ejecutan instrucciones **SIMD (*Single Instruction, Multiple Data*)**, aplicando la misma operación aritmética sobre múltiples valores en un solo ciclo de reloj.

---

## 7. Broadcasting (Difusión)

Permite realizar operaciones aritméticas entre arrays de formas distintas.

$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} + \begin{bmatrix} 10 & 20 & 30 \end{bmatrix} = \begin{bmatrix} 11 & 22 & 33 \\ 14 & 25 & 36 \end{bmatrix}$$

---

## 8. Estadística Descriptiva y Agregación por Eje

El parámetro `axis` permite especificar la dirección de agregación:
- `axis=0`: Reduce las **filas** (opera verticalmente por columnas).
- `axis=1`: Reduce las **columnas** (opera horizontalmente por filas).

```python
X = np.array([[10, 20, 30], [40, 50, 60]])

print("Suma por columna (axis=0):", X.sum(axis=0)) # [50, 70, 90]
print("Media por fila (axis=1):", X.mean(axis=1))   # [20., 50.]
```

---

## 9. Álgebra Lineal con `np.linalg`

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Producto matricial (@ o np.dot)
C = A @ B

# Operaciones matriciales avanzadas
det_A = np.linalg.det(A)         # Determinante
inv_A = np.linalg.inv(A)         # Inversa
sol_x = np.linalg.solve(A, [5, 11]) # Sistema A * x = b
```

---

## 10. Casos de Uso de NumPy

De acuerdo al material teórico de la cátedra, los principales casos de aplicación son:

1. **Big Data**: Procesamiento masivo de torrentes de datos numéricos en memoria contigua.
2. **Estadística Avanzada**: Cómputo de matrices de covarianza, varianzas y correlaciones.
3. **Álgebra Lineal**: Transformaciones de coordenadas, resolución de sistemas y descomposición matricial.
4. **Modelos de Procesamiento del Lenguaje Natural (NLP)**: Representación de vectores de palabras (*word embeddings*) y matrices TF-IDF.
5. **Procesamiento de Imágenes**: Manipulación de imágenes como tensores 3D de píxeles (alto, ancho, canales RGB).
