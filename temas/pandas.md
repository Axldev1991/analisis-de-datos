# Guía Completa de Pandas para el Análisis de Datos

> **Materia**: Análisis de Datos (UTN)  
> **Cátedra**: Introducción al Análisis de Datos — Fernández, Luis Nahuel  
> **Documento generado mediante especificación SDD**

---

## Tabla de Contenidos
1. [Introducción a Pandas](#1-introducción-a-pandas)
2. [Funciones de Carga e Ingesta de Datos](#2-funciones-de-carga-e-ingesta-de-datos)
3. [Estructuras de Datos Básicas: `Series` y `DataFrame`](#3-estructuras-de-datos-básicas-series-y-dataframe)
4. [Atributos y Métodos de la Clase `Series`](#4-atributos-y-métodos-de-la-clase-series)
5. [Atributos y Métodos de la Clase `DataFrame`](#5-atributos-y-métodos-de-la-clase-dataframe)
6. [Selección de Columnas y Filtrado de Filas](#6-selección-de-columnas-y-filtrado-de-filas)
7. [Manejo de Índices (`loc` e `iloc`)](#7-manejo-de-índices-loc-e-iloc)
8. [Procesamiento de Fechas (`to_datetime` y `.dt`)](#8-procesamiento-de-fechas-to_datetime-y-dt)
9. [Procesamiento de Cadenas de Texto (`.str`)](#9-procesamiento-de-cadenas-de-texto-str)
10. [Agrupamiento y Uniones (`groupby` y `merge`)](#10-agrupamiento-y-uniones-groupby-y-merge)

---

## 1. Introducción a Pandas

**Pandas** es una librería de código abierto y de alto nivel en Python orientada al trabajo con **DataFrames** (estructuras tabulares). Fue desarrollada inicialmente en **2008 por Wes McKinney**.

### Características Generales (según material de cátedra):
- Orientada al trabajo con DataFrames (estructuras bidimensionales y relacionales).
- Código abierto y multiplataforma.
- Optimizada bajo altos estándares de calidad sobre la base computacional de NumPy.
- Sintaxis de alto nivel altamente expresiva.

---

## 2. Funciones de Carga e Ingesta de Datos

Pandas ofrece funciones para la lectura y exportación multiformato:

| Función | Descripción | Ejemplo de Sintaxis |
| :--- | :--- | :--- |
| **`pd.read_csv()`** | Abre e importa archivos CSV. | `df = pd.read_csv("datos.csv")` |
| **`pd.read_excel()`** | Abre e importa archivos Excel (`.xlsx`). | `df = pd.read_excel("datos.xlsx")` |
| **`pd.read_json()`** | Carga archivos en formato JSON. | `df = pd.read_json("datos.json")` |
| **`pd.DataFrame()`** | Crea manualmente una instancia de DataFrame. | `df = pd.DataFrame(diccionario)` |
| **`pd.to_datetime()`** | Convierte una columna o vector a formato fecha/tiempo. | `df["fecha"] = pd.to_datetime(df["fecha"])` |
| **`pd.merge()`** | Une dos tablas/DataFrames estilo SQL. | `pd.merge(df1, df2, on="id")` |

---

## 3. Estructuras de Datos Básicas: `Series` y `DataFrame`

- **`Series`**: Vectores unidimensionales etiquetados que contienen datos de cualquier tipo. Están construidos internamente sobre la base de `numpy.ndarray`.
- **`DataFrame`**: Estructura de datos bidimensional (tabla) capaz de contener arrays de dos dimensiones o tablas con filas y columnas heterogéneas.

---

## 4. Atributos y Métodos de la Clase `Series`

### Atributos Clave:
- **`index`**: Retorna las etiquetas del índice de la serie.
- **`values`**: Retorna los valores subyacentes como un `ndarray`.
- **`name`**: Atributo opcional que almacena el nombre de la serie.
- **`is_unique`**: Retorna `True` o `False` según si todos los valores son únicos o existen duplicados.
- *Nota de cátedra*: Posee la mayoría de los atributos de `ndarray` (excepto `data`, `itemsize` y `strides`).

### Métodos Principales:
- **`head(n)`**: Muestra los primeros $n$ elementos.
- **`describe()`**: Retorna medidas de tendencia central y otras estadísticas descriptivas.
- **`dropna()`**: Elimina valores nulos de la serie.
- **`apply(func)`**: Aplica una función a cada elemento de la serie.
- *Nota de cátedra*: Posee la mayoría de los métodos de `ndarray` (excepto `flatten()` y `reshape()`).

---

## 5. Atributos y Métodos de la Clase `DataFrame`

### Atributos Principales:
- **`shape`**: Devuelve una tupla con la cantidad de filas y columnas.
- **`columns`**: Devuelve los nombres de las columnas.
- **`dtypes`**: Retorna los tipos de datos de cada columna.
- **`index`**: Atributo de índice de filas que se puede acceder o setear.

### Métodos Principales:
- **`to_csv()`**: Guarda un DataFrame como archivo CSV.
- **`to_excel()`**: Guarda un DataFrame como archivo Excel.
- **`head(n)`**: Muestra las primeras $n$ filas.
- **`info()`**: Retorna un resumen estructural del DataFrame (filas, columnas, nulos, dtypes).
- **`groupby()`**: Agrupa filas según una columna especificada por parámetro.

---

## 6. Selección de Columnas y Filtrado de Filas

### Selección de Columnas:
- **Por Nombre**:
  - Una columna: `df.id` o `df["id"]`
  - Subconjunto de columnas: `df[["id", "damage"]]`
- **Por Posición**:
  - Una columna por posición: `df.iloc[:, 1]` (selecciona la primera columna tras el índice)
  - Varias columnas por posición: `df.iloc[:, 1:4]` (selecciona las columnas en posiciones 1 a 3)

### Filtrado de Filas:
- **Por Posición**:
  - `df.iloc[2, :]`: Retorna todas las columnas de la fila en posición 2.
- **Según Condiciones Logicas**:
  - `df.loc[df.damage == 3, ["id", "damage"]]`: Retorna las columnas `"id"` y `"damage"` de todas las filas cuyo valor en `"damage"` sea igual a 3.
- **Consulta con `.query()`**:
  - `df.query("damage > 2")`: Retorna las filas cuyo valor en `"damage"` sea mayor a 2 con sintaxis limpia.

---

## 7. Manejo de Índices (`loc` e `iloc`)

Los índices simplifican el acceso a los datos. El atributo `df.index` permite consultar o definir el índice de filas.

```python
# loc utiliza nombres de filas y columnas
df_filtrado = df.loc[df["damage"] == 3, ["id", "damage"]]

# iloc utiliza posiciones numéricas enteras
sub_matriz = df.iloc[:5, 0:3]
```

---

## 8. Procesamiento de Fechas (`to_datetime` y `.dt`)

Con la función `pd.to_datetime()` se transforma una columna en formato fecha (`datetime64`). Luego, mediante el accesor **`.dt`**, se accede a los componentes individuales:

```python
import pandas as pd

# Convertir columna a fecha
df["fecha"] = pd.to_datetime(df["fecha_string"])

# Accesores del atributo .dt
df["anio"] = df["fecha"].dt.year
df["mes"]  = df["fecha"].dt.month
df["dia"]  = df["fecha"].dt.day
```

---

## 9. Procesamiento de Cadenas de Texto (`.str`)

Pandas simplifica el trabajo con texto vectorizado mediante el accesor **`.str`**:

| Función de `.str` | Descripción | Ejemplo de Sintaxis |
| :--- | :--- | :--- |
| **`str.lower()`** | Convierte el texto a minúsculas. | `df["texto"].str.lower()` |
| **`str.upper()`** | Convierte el texto a mayúsculas. | `df["texto"].str.upper()` |
| **`str.slice()`** | Corta una subcadena por posiciones. | `df["texto"].str.slice(0, 3)` |
| **`str.split()`** | Divide la cadena por un delimitador. | `df["texto"].str.split(" ")` |
| **`str.replace()`** | Reemplaza subcadenas. | `df["texto"].str.replace("a", "b")` |

---

## 10. Agrupamiento y Uniones (`groupby` y `merge`)

```python
# Agrupamiento por columna
resumen = df.groupby("categoria")["damage"].mean()

# Uniones de tablas
df_unido = pd.merge(df1, df2, on="id", how="inner")
```
