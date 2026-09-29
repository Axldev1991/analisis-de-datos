# Guía Completa de Pandas para el Análisis de Datos

> **Materia**: Análisis de Datos (UTN)  
> **Cátedra**: Introducción al Análisis de Datos — Fernández, Luis Nahuel  
> **Documento generado mediante especificación SDD**

---

## Tabla de Contenidos
1. [Introducción a Pandas](#1-introducción-a-pandas)
2. [Estructuras Principales: Series y DataFrames](#2-estructuras-principales-series-y-dataframes)
3. [Lectura e Inspección de Datos](#3-lectura-e-inspección-de-datos)
4. [Indexación y Selección (`loc` e `iloc`)](#4-indexación-y-selección-loc-e-iloc)
5. [Filtrado Booleano y Consultas](#5-filtrado-booleano-y-consultas)
6. [Transformación y Aplicación de Funciones (`apply`)](#6-transformación-y-aplicación-de-funciones-apply)
7. [Agrupamiento y Agregación (`groupby`)](#7-agrupamiento-y-agregación-groupby)
8. [Combinación de Datasets (`concat` y `merge`)](#8-combinación-de-datasets-concat-y-merge)
9. [Procesamiento de Texto (`.str`) y Fechas (`.dt`)](#9-procesamiento-de-texto-str-y-fechas-dt)

---

## 1. Introducción a Pandas

**Pandas** es la librería de referencia para la manipulación y análisis de datos estructurados (tabulares) en Python. Construida sobre NumPy, proporciona estructuras de datos flexibles con etiquetas en filas y columnas, permitiendo realizar operaciones de limpieza, filtrado, transformación y agregación de forma expresiva y eficiente.

---

## 2. Estructuras Principales: Series y DataFrames

### `Series`
Vector unidimensional etiquetado (homogéneo o heterogéneo en concepto, pero homogéneo en `dtype`).

```python
import pandas as pd
import numpy as np

s = pd.Series([80, 90, 70, 85], index=["Mariana", "Maia", "Sabrina", "Carla"], name="Cordialidad")
print(s)
# Mariana    80
# Maia       90
# Sabrina    70
# Carla      85
# Name: Cordialidad, dtype: int64
```

### `DataFrame`
Estructura bidimensional (tabla de datos) compuesta por una colección ordenada de columnas, donde cada columna es una `Series`.

```python
datos = {
    "Candidata": ["Mariana", "Maia", "Sabrina", "Daniela", "Alejandra", "Carla"],
    "Juez1_Cordialidad": [80, 80, 90, 80, 70, 90],
    "Juez1_Presencia": [90, 90, 60, 50, 60, 85],
    "Juez1_Idioma": [70, 60, 50, 50, 50, 60]
}

df = pd.DataFrame(datos)
print(df)
```

---

## 3. Lectura e Inspección de Datos

### Importación de Archivos
```python
# Carga desde CSV / Excel
df_csv = pd.read_csv("datos.csv", sep=",", encoding="utf-8")
df_excel = pd.read_excel("IMCinfantil.xlsx", sheet_name="Hoja1")

# Exportación
df.to_csv("resultado.csv", index=False)
df.to_excel("resultado.xlsx", index=False)
```

### Inspección Rápida
```python
print("Forma del DataFrame (filas, columnas):", df.shape)
print("\nPrimeras 5 filas:")
print(df.head())

print("\nInformación estructural y nulos:")
df.info()

print("\nEstadística descriptiva de variables numéricas:")
print(df.describe())
```

---

## 4. Indexación y Selección (`loc` e `iloc`)

Pandas provee dos accesores principales para la selección precisa de datos:

| Accesor | Criterio de Selección | Ejemplo |
| :--- | :--- | :--- |
| **`.loc[]`** | Basado en **Etiquetas** (nombres de índice / columna) | `df.loc[0:2, 'Candidata':'Juez1_Presencia']` |
| **`.iloc[]`** | Basado en **Posición Numérica** (entera 0-based) | `df.iloc[0:3, 0:2]` |

```python
# Selección por etiquetas (.loc)
sub_df = df.loc[df["Candidata"] == "Mariana", ["Juez1_Cordialidad", "Juez1_Presencia"]]

# Selección por posiciones numéricas (.iloc)
primeras_dos_filas = df.iloc[:2, :3]
```

---

## 5. Filtrado Booleano y Consultas

Permite seleccionar filas mediante condiciones lógicas:

```python
# Filtrar candidatas con Cordialidad >= 80 e Idioma >= 60
filtro = (df["Juez1_Cordialidad"] >= 80) & (df["Juez1_Idioma"] >= 60)
candidatas_destacadas = df[filtro]

# Método .isin() para consultar listas de valores
seleccionadas = df[df["Candidata"].isin(["Mariana", "Carla"])]

# Método .query() para sintaxis más legible
resultado = df.query("Juez1_Cordialidad >= 80 and Juez1_Idioma >= 60")
```

---

## 6. Transformación y Aplicación de Funciones (`apply`)

### Creación de Columnas Derivadas
```python
# Operaciones vectorizadas directas
df["Promedio_Juez1"] = (df["Juez1_Cordialidad"] + df["Juez1_Presencia"] + df["Juez1_Idioma"]) / 3

# Método .apply() fila por fila (axis=1) o columna por columna (axis=0)
def categorizar_promedio(row):
    prom = row["Promedio_Juez1"]
    if prom >= 80:
        return "Sobresaliente"
    elif prom >= 70:
        return "Satisfactorio"
    else:
        return "Regular"

df["Categoria"] = df.apply(categorizar_promedio, axis=1)
```

---

## 7. Agrupamiento y Agregación (`groupby`)

El patrón **Split-Apply-Combine** permite agrupar datos según categorías y calcular agregaciones:

```python
# Agrupar por Categoría y calcular estadísticas
resumen = df.groupby("Categoria").agg(
    Promedio_Cordialidad=("Juez1_Cordialidad", "mean"),
    Max_Idioma=("Juez1_Idioma", "max"),
    Cantidad=("Candidata", "count")
).reset_index()

print(resumen)
```

---

## 8. Combinación de Datasets (`concat` y `merge`)

### Concatenación (`pd.concat`)
Une DataFrames a lo largo de las filas (`axis=0`) o columnas (`axis=1`).

```python
# Apilar DataFrames verticalmente
df_juez1 = df[["Candidata", "Juez1_Cordialidad"]]
df_juez2 = df[["Candidata", "Juez1_Presencia"]]

df_concatenado = pd.concat([df_juez1, df_juez2], axis=0, ignore_index=True)
```

### Uniones Estilo SQL (`pd.merge`)
Combina DataFrames utilizando claves comunes (*joins*).

```python
df_info = pd.DataFrame({
    "Candidata": ["Mariana", "Maia", "Sabrina"],
    "Edad": [24, 27, 22]
})

# Inner join, Left join, Right join, Outer join
df_merged = pd.merge(df, df_info, on="Candidata", how="inner")
```

---

## 9. Procesamiento de Texto (`.str`) y Fechas (`.dt`)

### Accesor de Cadenas (`.str`)
Permite aplicar funciones de string sobre columnas tipo objeto/texto de forma vectorizada.

```python
df["Candidata_Mayusc"] = df["Candidata"].str.upper()
df["Tiene_A"] = df["Candidata"].str.contains("a", case=False)
df["Candidata_Limpia"] = df["Candidata"].str.strip().str.replace(" ", "_")
```

### Accesor de Fechas (`.dt`) y `pd.to_datetime()`
```python
# Convertir columna a formato datetime
df["Fecha_Entrevista"] = pd.to_datetime(["2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20"])

# Extraer componentes de fecha
df["Anio"] = df["Fecha_Entrevista"].dt.year
df["Mes"] = df["Fecha_Entrevista"].dt.month
df["Dia_Semana"] = df["Fecha_Entrevista"].dt.day_name()
```
