# Guía Completa de NumPy para el Análisis de Datos

> **Materia**: Análisis de Datos (UTN)  
> **Cátedra**: Introducción al Análisis de Datos — Fernández, Luis Nahuel  
> **Documento generado mediante especificación SDD**

---

## Tabla de Contenidos
1. [Introducción a NumPy y el `ndarray`](#1-introducción-a-numpy-y-el-ndarray)
2. [Creación de Arrays](#2-creación-de-arrays)
3. [Atributos Fundamentales de un Array](#3-atributos-fundamentales-de-un-array)
4. [Indexación, Slicing y Filtros Booleanos](#4-indexación-slicing-y-filtros-booleanos)
5. [Operaciones Vectorizadas (Element-wise)](#5-operaciones-vectorizadas-element-wise)
6. [Broadcasting (Difusión)](#6-broadcasting-difusión)
7. [Estadística Descriptiva y Agregación](#7-estadística-descriptiva-y-agregación)
8. [Álgebra Lineal con `np.linalg`](#8-álgebra-lineal-con-nplinalg)

---

## 1. Introducción a NumPy y el `ndarray`

**NumPy** (*Numerical Python*) es la librería fundamental sobre la cual se erige todo el ecosistema de computación científica y *Data Science* en Python. 

Su objeto central es el **`ndarray`** (N-dimensional array), un contenedor homogéneo de datos contiguos en memoria, escrito internamente en C para lograr alta eficiencia computacional y evitar los costos de inspección de tipo dinámico de las listas nativas de Python.

### Ventajas clave:
- **Homogeneidad**: Todos los elementos deben ser del mismo tipo de dato (`dtype`).
- **Vectorización**: Ejecuta operaciones numéricas en bloque sin necesidad de bucles explícitos `for`.
- **Eficiencia en memoria**: Ocupa un bloque de memoria contiguo, lo que maximiza el rendimiento del *cache* del procesador.

---

## 2. Creación de Arrays

```python
import numpy as np

# Desde una lista o lista de listas
a1d = np.array([1, 2, 3, 4, 5])
a2d = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Funciones generadoras
zeros = np.zeros((3, 4))             # Matriz de ceros 3x4
ones  = np.ones((2, 3), dtype=int)   # Matriz de unos 2x3 enteros
full  = np.full((2, 2), 7)           # Matriz 2x2 con valor 7
eye   = np.eye(3)                    # Matriz identidad 3x3

# Rangos numéricos
secuencia = np.arange(0, 10, 2)      # [0, 2, 4, 6, 8]
puntos    = np.linspace(0, 1, 5)     # 5 puntos equiespaciados entre 0 y 1

# Números aleatorios
rand_uniform = np.random.rand(3, 3)  # Distribución Uniforme U(0, 1)
rand_normal  = np.random.randn(3, 3) # Distribución Normal N(0, 1)
```

---

## 3. Atributos Fundamentales de un Array

Dado un `ndarray`, se pueden consultar sus propiedades dimensionales y de tipo:

```python
arr = np.array([[10, 20, 30], [40, 50, 60]], dtype=np.float64)

print("Dimensión (ndim):", arr.ndim)   # 2
print("Forma (shape):", arr.shape)     # (2, 3)
print("Total elementos (size):", arr.size) # 6
print("Tipo de dato (dtype):", arr.dtype)  # float64
```

---

## 4. Indexación, Slicing y Filtros Booleanos

### Slicing N-dimensional: `arr[filas, columnas]`

```python
matriz = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print(matriz[0, 1])      # Elemento en fila 0, columna 1 -> 20
print(matriz[:2, 1:3])   # Submatriz filas 0-1, cols 1-2
print(matriz[:, 2])      # Todas las filas, columna 2 -> [30, 70, 110]
```

### Máscaras Booleanas (*Boolean Indexing*)

Permite filtrar arrays según condiciones lógicas sin usar condicionales `if`:

```python
datos = np.array([12, 45, 78, 23, 56, 89, 90, 11])

# Crear máscara booleana
mascara = datos > 50  # [False, False,  True, False,  True,  True,  True, False]

# Filtrar elementos
filtrados = datos[mascara]  # [78, 56, 89, 90]

# Operaciones lógicas combinadas: & (AND), | (OR), ~ (NOT)
filtro_compuesto = datos[(datos >= 20) & (datos <= 80)]
```

---

## 5. Operaciones Vectorizadas (Element-wise)

Las operaciones numéricas se aplican elemento por elemento (*element-wise*):

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)     # [11, 22, 33]
print(a * b)     # [10, 40, 90] (Multiplicación elemento a elemento)
print(a ** 2)    # [1, 4, 9]
print(np.sin(a)) # Seno de cada elemento
```

---

## 6. Broadcasting (Difusión)

El **Broadcasting** describe la capacidad de NumPy para realizar operaciones aritméticas sobre arrays con formas (*shapes*) distintas.

### Reglas de Broadcasting:
1. Si los arrays no tienen el mismo número de dimensiones, se anteponen dimensiones de tamaño 1 a la forma del array más pequeño.
2. Dos dimensiones son compatibles cuando:
   - Son iguales, o
   - Una de ellas es igual a 1.

$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} + \begin{bmatrix} 10 & 20 & 30 \end{bmatrix} = \begin{bmatrix} 11 & 22 & 33 \\ 14 & 25 & 36 \end{bmatrix}$$

```python
# Ejemplo de Broadcasting en código
matriz = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
vector = np.array([10, 20, 30])           # Shape (3,) -> se difunde a (2, 3)

resultado = matriz + vector
print(resultado)
# [[11 22 33]
#  [14 25 36]]
```

---

## 7. Estadística Descriptiva y Agregación

NumPy proporciona funciones vectorizadas para calcular estadísticos descriptivos. El argumento `axis` especifica el eje a lo largo del cual se reduce la matriz:
- `axis=0`: Reduce las **filas** (opera a lo largo de las columnas).
- `axis=1`: Reduce las **columnas** (opera a lo largo de las filas).

```python
X = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Suma total:", np.sum(X))             # 210
print("Suma por columna (axis=0):", np.sum(X, axis=0)) # [50, 70, 90]
print("Suma por fila (axis=1):", np.sum(X, axis=1))    # [60, 150]

# Estadísticos de centralidad y dispersión
media = np.mean(X)
desvio = np.std(X)
varianza = np.var(X)
mediana = np.median(X)
minimo, maximo = np.min(X), np.max(X)
pos_max = np.argmax(X) # Índice del valor máximo plano
```

---

## 8. Álgebra Lineal con `np.linalg`

NumPy soporta operaciones algebraicas matriciales fundamentales:

### Producto Matricial vs Element-wise

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Producto punto / multiplicacion matricial: A @ B o np.dot(A, B)
producto_matricial = A @ B
# [[19 22]
#  [43 50]]

# Transpuesta
A_transpuesta = A.T

# Inversa y Determinante
det_A = np.linalg.det(A)         # -2.0
inv_A = np.linalg.inv(A)         # Inversa de A

# Resolución de sistemas de ecuaciones lineales: A * x = b
b = np.array([5, 11])
x = np.linalg.solve(A, b)
print("Solución x:", x)          # [1., 2.]
```
