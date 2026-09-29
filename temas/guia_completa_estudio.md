# Guía Completa de Estudio — Análisis de Datos (UTN)

> **Materia**: Análisis de Datos (Universidad Tecnológica Nacional)  
> **Cátedra**: Introducción al Análisis de Datos — Fernández, Luis Nahuel  
> **Documento maestro unificado generado mediante especificación SDD**

---

## 🗺️ Hoja de Ruta Pedagógica de Estudio

La presente guía reúne y unifica el 100% de los contenidos teóricos del libro principal (*Análisis inteligente de datos con lenguaje R*) y los apuntes/presentaciones técnicas de la materia en un orden pedagógico optimizado para la comprensión progresiva:

```
┌────────────────────────────────────────────────────────────────────────┐
│ UNIDAD 1: Fundamentos de la Minería de Datos y el Escenario Actual     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ UNIDAD 2: Programación y Estructuras de Datos con Python               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ UNIDAD 3: Computación Numérica y Vectorial con NumPy                   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ UNIDAD 4: Análisis y Manipulación Tabular con Pandas                   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ UNIDAD 5: Estadística Descriptiva Univariada y Multivariada            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ UNIDAD 6: Limpieza de Datos (Data Cleaning) y Estadística Robusta      │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📑 Tabla de Contenidos General

- [Unidad 1: Fundamentos de la Minería de Datos y el Escenario Actual](#unidad-1-fundamentos-de-la-minería-de-datos-y-el-escenario-actual)
  - [1.1 Orígenes Históricos](#11-orígenes-históricos)
  - [1.2 El Escenario Actual y Big Data](#12-el-escenario-actual-y-big-data)
  - [1.3 Estadística Clásica vs. Data Mining](#13-estadística-clásica-vs-data-mining)
  - [1.4 Ecosistema de Software y Herramientas](#14-ecosistema-de-software-y-herramientas)
  - [1.5 Nueva Terminología (IoT, M2M, WoT, IoE)](#15-nueva-terminología-iot-m2m-wot-ioe)
- [Unidad 2: Programación y Estructuras de Datos con Python](#unidad-2-programación-y-estructuras-de-datos-con-python)
  - [2.1 Entornos de Trabajo (Jupyter, Colab)](#21-entornos-de-trabajo-jupyter-colab)
  - [2.2 Tipos de Datos Primitivos y Variables](#22-tipos-de-datos-primitivos-y-variables)
  - [2.3 Estructuras de Datos Nativas (Listas, Tuplas, Diccionarios, Sets)](#23-estructuras-de-datos-nativas-listas-tuplas-diccionarios-sets)
  - [2.4 Control de Flujo y Comprensión de Listas](#24-control-de-flujo-y-comprensión-de-listas)
  - [2.5 Funciones y Programación Funcional](#25-funciones-y-programación-funcional)
- [Unidad 3: Computación Numérica y Vectorial con NumPy](#unidad-3-computación-numérica-y-vectorial-con-numpy)
  - [3.1 El Objeto `ndarray` y Creación de Arrays](#31-el-objeto-ndarray-y-creación-de-arrays)
  - [3.2 Indexación, Slicing y Máscaras Booleanas](#32-indexación-slicing-y-máscaras-booleanas)
  - [3.3 Operaciones Vectorizadas y Broadcasting](#33-operaciones-vectorizadas-y-broadcasting)
  - [3.4 Estadística Descriptiva y Agregaciones por Eje](#34-estadística-descriptiva-y-agregaciones-por-eje)
  - [3.5 Álgebra Lineal con `np.linalg`](#35-álgebra-lineal-con-nplinalg)
- [Unidad 4: Análisis y Manipulación Tabular con Pandas](#unidad-4-análisis-y-manipulación-tabular-con-pandas)
  - [4.1 Estructuras `Series` y `DataFrame`](#41-estructuras-series-y-dataframe)
  - [4.2 Lectura, Escritura e Inspección de Datos](#42-lectura-escritura-e-inspección-de-datos)
  - [4.3 Indexación y Selección (`loc` e `iloc`)](#43-indexación-y-selección-loc-e-iloc)
  - [4.4 Filtrado Booleano y Consultas `query`](#44-filtrado-booleano-y-consultas-query)
  - [4.5 Transformación con `apply()` y Agrupamiento `groupby()`](#45-transformación-con-apply-y-agrupamiento-groupby)
  - [4.6 Combinación de Datasets (`concat` y `merge`)](#46-combinación-de-datasets-concat-y-merge)
  - [4.7 Procesamiento de Texto (`.str`) y Fechas (`.dt`)](#47-procesamiento-de-texto-str-y-fechas-dt)
- [Unidad 5: Estadística Descriptiva Univariada y Multivariada](#unidad-5-estadística-descriptiva-univariada-y-multivariada)
  - [5.1 Variables y Niveles de Medición](#51-variables-y-niveles-de-medición)
  - [5.2 Tablas de Frecuencias](#52-tablas-de-frecuencias)
  - [5.3 Medidas de Tendencia Central, Posición y Dispersión](#53-medidas-de-tendencia-central-posición-y-dispersión)
  - [5.4 Medidas de Forma: Asimetría y Curtosis](#54-medidas-de-forma-asimetría-y-curtosis)
  - [5.5 Representaciones Gráficas y Boxplots](#55-representaciones-gráficas-y-boxplots)
  - [5.6 Análisis Multivariado: Matriz de Datos y Parámetros](#56-análisis-multivariado-matriz-de-datos-y-parámetros)
  - [5.7 Vector de Medias, Matriz de Covarianzas, Correlación y Traza](#57-vector-de-medias-matriz-de-covarianzas-correlación-y-traza)
  - [5.8 Visualizaciones Multivariadas Avanzadas](#58-visualizaciones-multivariadas-avanzadas)
- [Unidad 6: Limpieza de Datos (Data Cleaning) y Estadística Robusta](#unidad-6-limpieza-de-datos-data-cleaning-y-estadística-robusta)
  - [6.1 Ciclo de Vida del Análisis y Diagnóstico de Datos](#61-ciclo-de-vida-del-análisis-y-diagnóstico-de-datos)
  - [6.2 Valores Inconsistentes vs. Atípicos (*Outliers*)](#62-valores-inconsistentes-vs-atípicos-outliers)
  - [6.3 Tratamiento de Duplicados](#63-tratamiento-de-duplicados)
  - [6.4 Manejo de Valores Faltantes (MCAR, MAR, MNAR) e Imputación](#64-manejo-de-valores-faltantes-mcar-mar-mnar-e-imputación)
  - [6.5 Transformación y Escalado de Variables](#65-transformación-y-escalado-de-variables)
  - [6.6 Detección de Outliers Univariados y Robustez (MAD/MADN)](#66-detección-de-outliers-univariados-y-robustez-madmadn)
  - [6.7 Outliers Multivariados, Mahalanobis, MVE y MCD](#67-outliers-multivariados-mahalanobis-mve-y-mcd)

---

## UNIDAD 1: Fundamentos de la Minería de Datos y el Escenario Actual

### 1.1 Orígenes Históricos
La minería de datos (*data mining*) surge de la necesidad de extraer información valiosa acumulada en grandes bases de datos. Tres figuras marcaron su evolución:
- **Adolphe Quetelet (1796-1874)**: Precursor de la *Física Social*. Demostró que fenómenos sociales como la delincuencia presentan regularidades estadísticamente cuantificables.
- **Francis Galton (1822-1911)**: Desarrolló los conceptos de **correlación y regresión hacia la media**, además del uso de encuestas y estudios antropométricos.
- **Ronald Fisher (1890-1962)**: Formuló el **Análisis de Varianza (ANOVA)** y sentó las bases de la estadística inferencial moderna y el diseño de experimentos.

### 1.2 El Escenario Actual y Big Data
En la actualidad se evidencia un crecimiento masivo de datos colectados, almacenados y distribuidos originados en transacciones bancarias, telefonía celular, e-commerce, registros médicos y sensores remotos. En *Data Mining* convergen la informática, las bases de datos, el aprendizaje automático (*Machine Learning*), la inteligencia artificial, la estadística y la visualización.

### 1.3 Estadística Clásica vs. Data Mining

| Dimensión | Estadística Clásica | Data Mining / Minería de Datos |
| :--- | :--- | :--- |
| **Procedimiento** | **Hipotético-deductivo** (formulación previa de hipótesis) | **Inductivo** (descubrimiento de patrones desde los datos) |
| **Enfoque de Técnicas** | Confirmatorias | Exploratorias y Predictivas |
| **Supuestos Iniciales** | Requiere supuestos rígidos (ej: normalidad) | **Sin supuestos iniciales rígidos** |
| **Escala de Datos** | Muestras pequeñas o moderadas | Grandes volúmenes (*Big Data*) |

### 1.4 Ecosistema de Software y Herramientas
- **Lenguajes Abiertos**: **R** (especializado en análisis estadístico y gráficos) y **Python** (lenguaje multiparadigma dominante en Machine Learning).
- **Entornos y Suites**: WEKA, SAS Enterprise Miner, SPSS Clementine (IBM), SPAD, Statistica, SODAS.

### 1.5 Nueva Terminología (IoT, M2M, WoT, IoE)
- **M2M (*Machine to Machine*)**: Comunicación automatizada entre dispositivos para monitoreo y telemetría en tiempo real (ej: POS, contadores inteligentes).
- **IoT (*Internet of Things*)**: Término introducido por Kevin Ashton (1999). Red de objetos cotidianos interconectados mediante sensores e internet.
- **WoT (*Web of Things*)**: Capa de software sobre IoT que permite acceder a los dispositivos usando estándares web (HTTP, REST, JSON).
- **IoE (*Internet of Everything*)**: Filosofía que conecta **Personas, Procesos, Datos y Cosas** en una red unificada.

---

## UNIDAD 2: Programación y Estructuras de Datos con Python

### 2.1 Entornos de Trabajo (Jupyter, Colab)
El análisis interactivo se ejecuta en **Jupyter Notebooks** o **Google Colab**, entornos basados en bloques (*cells*) ejecutable de código y celdas de documentación Markdown.

### 2.2 Tipos de Datos Primitivos y Variables
Python posee tipado dinámico. Los tipos primitivos son:
- Enteros (`int`), Flotantes (`float`), Cadenas de texto (`str`), Booleanos (`bool`) y Nulos (`NoneType`).

### 2.3 Estructuras de Datos Nativas (Listas, Tuplas, Diccionarios, Sets)
- **Listas (`list`)**: Secuencias ordenadas y **mutables**: `[1, 2, "a"]`.
- **Tuplas (`tuple`)**: Secuencias ordenadas e **inmutables**: `(10, 20)`.
- **Diccionarios (`dict`)**: Colecciones de pares **clave-valor** con búsqueda de complejidad $O(1)$: `{"nombre": "Mariana", "nota": 90}`.
- **Conjuntos (`set`)**: Colecciones desordenadas de elementos **únicos**: `{"A", "B"}`.

### 2.4 Control de Flujo y Comprensión de Listas
- Estruturas `if-elif-else`, bucles `for` con `enumerate()` o `range()`, y bucles `while`.
- **Comprensión de Listas**: Sintaxis concisa para crear listas transformadas/filtradas:
  ```python
  ajustados = [x + 5 for x in puntajes if x >= 70]
  ```

### 2.5 Funciones y Programación Funcional
- Definición de funciones con `def`, parámetros posicionales y nombrados con valores por defecto.
- **Funciones Lambda**: `lambda x: x ** 2`.
- **Funciones de orden superior**: `map()`, `filter()`, `zip()`.

---

## UNIDAD 3: Computación Numérica y Vectorial con NumPy

### 3.1 El Objeto `ndarray` y Creación de Arrays
NumPy proporciona la estructura **`ndarray`**, un contenedor homogéneo de memoria contigua escrito en C.
```python
import numpy as np

arr = np.array([1, 2, 3])
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
secuencia = np.arange(0, 10, 2)
puntos = np.linspace(0, 1, 5)
```
Atributos clave: `ndim`, `shape`, `size`, `dtype`.

### 3.2 Indexación, Slicing y Máscaras Booleanas
- **Slicing**: `matriz[filas, columnas]` -> `matriz[:2, 1:3]`.
- **Indexación Booleana**: `filtrados = datos[datos > 50]`.

### 3.3 Operaciones Vectorizadas y Broadcasting
- Las operaciones aritméticas (`+`, `-`, `*`, `/`) se ejecutan elemento por elemento (*element-wise*).
- **Broadcasting (Difusión)**: Permite operar arrays de formas distintas adaptando dimensiones de tamaño 1.

$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} + \begin{bmatrix} 10 & 20 & 30 \end{bmatrix} = \begin{bmatrix} 11 & 22 & 33 \\ 14 & 25 & 36 \end{bmatrix}$$

### 3.4 Estadística Descriptiva y Agregaciones por Eje
Funciones `np.sum()`, `np.mean()`, `np.std()`, `np.var()`, `np.median()`, `np.min()`, `np.max()`.
- `axis=0`: Opera verticalmente a lo largo de las filas (reduce a nivel columna).
- `axis=1`: Opera horizontalmente a lo largo de las columnas (reduce a nivel fila).

### 3.5 Álgebra Lineal con `np.linalg`
- Producto matricial: `A @ B` o `np.dot(A, B)`.
- Transpuesta: `A.T`.
- Inversa y Determinante: `np.linalg.inv(A)`, `np.linalg.det(A)`.
- Resolución de sistemas de ecuaciones: `np.linalg.solve(A, b)`.

---

## UNIDAD 4: Análisis y Manipulación Tabular con Pandas

### 4.1 Estructuras `Series` y `DataFrame`
- **`Series`**: Array unidimensional etiquetado.
- **`DataFrame`**: Tabla bidimensional de columnas estructuradas (`Series`).

### 4.2 Lectura, Escritura e Inspección de Datos
```python
import pandas as pd

df = pd.read_csv("datos.csv")
df_excel = pd.read_excel("archivo.xlsx")

df.head()       # Primeras filas
df.info()       # Estructura y nulos
df.describe()   # Estadísticos descriptivos
```

### 4.3 Indexación y Selección (`loc` e `iloc`)
- **`.loc[]`**: Selección basada en **etiquetas/nombres**: `df.loc[:, 'ColA':'ColC']`.
- **`.iloc[]`**: Selección basada en **posiciones enteras**: `df.iloc[:5, 0:2]`.

### 4.4 Filtrado Booleano y Consultas `query`
```python
filtrado = df[(df["Edad"] >= 18) & (df["Ingreso"] > 50000)]
consulta = df.query("Edad >= 18 and Ingreso > 50000")
```

### 4.5 Transformación con `apply()` y Agrupamiento `groupby()`
- **`apply()`**: Aplica funciones personalizadas por fila o columna.
- **`groupby()` + `agg()`**: Patrón **Split-Apply-Combine**:
  ```python
  resumen = df.groupby("Categoria").agg(
      Promedio=("Valor", "mean"),
      Total=("Cantidad", "sum")
  ).reset_index()
  ```

### 4.6 Combinación de Datasets (`concat` y `merge`)
- **`pd.concat([df1, df2], axis=0)`**: Apilado vertical u horizontal.
- **`pd.merge(df1, df2, on="clave", how="inner")`**: Uniones tipo SQL (`inner`, `left`, `right`, `outer`).

### 4.7 Procesamiento de Texto (`.str`) y Fechas (`.dt`)
- Accesor `.str`: `df["Nombre"].str.upper()`, `.str.contains()`, `.str.replace()`.
- Accesor `.dt`: `pd.to_datetime(df["Fecha"])`, `.dt.year`, `.dt.month`, `.dt.day_name()`.

---

## UNIDAD 5: Estadística Descriptiva Univariada y Multivariada

### 5.1 Variables y Niveles de Medición
1. **Cualitativas**: Categorías sin orden (ej: sexo, marca).
2. **Ordinales**: Categorías con orden jerárquico (ej: nivel de estudio, gravedad I-IV).
3. **Discretas**: Conteo numérico aislado (ej: número de autos).
4. **Continuas**: Medición continua (ej: peso, estatura).
5. **Escalas Analógicas (VAS)**: Evaluación subjetiva en rango (ej: dolor 0 a 10).

### 5.2 Tablas de Frecuencias
- Frecuencia absoluta $f_i$, relativa $f_i/n$, porcentual $f_{\%i}$ y acumulada $F_k = \sum_{i=1}^k f_i$.

### 5.3 Medidas de Tendencia Central, Posición y Dispersión
- **Media ($\bar{x}$)**: $\bar{x} = \frac{1}{n}\sum x_i$. Sensible a outliers. Preserva la transformación $y = ax+b$.
- **Mediana ($\tilde{x}$)**: Valor central del 50%. Robusta.
- **Moda ($Mo$)**: Valor más frecuente.
- **Media $\alpha$-podada ($\bar{x}_\alpha$)**: Promedio descartando el $\alpha\%$ de extremos.
- **Cuartiles ($Q_1, Q_2, Q_3$)**: Dividen la muestra ordenada en 4 partes del 25%.
- **Varianza ($s_x^2$)**: $s_x^2 = \frac{1}{n-1}\sum (x_i - \bar{x})^2$.
- **Desviación Estándar ($s_x$)**: $s_x = \sqrt{s_x^2}$.
- **Coeficiente de Variación ($CV$)**: $CV = \frac{s_x}{\bar{x}} \times 100\%$. Dispersión relativa sin dimensión.
- **Rango Intercuartílico ($RI$)**: $RI = Q_3 - Q_1$.
- **MAD y MADN**: Mediana de desvíos absolutos respecto a la mediana. Normalización gaussiana: $MADN = \frac{MAD}{0.6745}$.

### 5.4 Medidas de Forma: Asimetría y Curtosis
- Asimetría de Fisher ($sk_F$), Pearson ($sk_P = \frac{\bar{x} - Mo}{s_x}$), Bowley ($sk_B = \frac{Q_3 + Q_1 - 2\tilde{x}}{Q_3 - Q_1}$).
- Curtosis $k(x)$: Leptocúrtica ($k > 3$), Mesocúrtica ($k = 3$), Platicúrtica ($k < 3$).

### 5.5 Representaciones Gráficas y Boxplots
- Gráficos circulares, barras, bastones, histogramas (reglas de Sturges, Velleman, Dixon-Kronmal).
- **Boxplot**: Muestra $Q_1, \tilde{x}, Q_3$ y bigotes a $1.5 \times RI$.
  - Outliers moderados: entre $1.5 \times RI$ y $3 \times RI$.
  - Outliers severos: mayores a $3 \times RI$.
  - Regla 3-Sigma: $|t_i| = \left|\frac{x_i - \bar{x}}{s}\right| > 3$.

### 5.6 Análisis Multivariado: Matriz de Datos y Parámetros
En una matriz $X \in \mathbb{R}^{n \times p}$, se deben estimar $p$ medias, $p$ varianzas y $\frac{p(p-1)}{2}$ covarianzas. El total de parámetros a estimar es:

$$\text{Parámetros} = \frac{p^2 + 3p}{2}$$

### 5.7 Vector de Medias, Matriz de Covarianzas, Correlación y Traza
- **Vector de Medias**: $\bar{x} = (\bar{x}_1, \dots, \bar{x}_p)$.
- **Matriz de Covarianzas ($\hat{\Sigma}$)**: Simétrica $p \times p$, varianzas en la diagonal y covarianzas fuera.
- **Matriz de Correlación ($R$)**: Simétrica $p \times p$, unos en la diagonal y coeficientes $r_{ik} \in [-1, 1]$ fuera.
- **Traza ($tr(A)$)**: Suma de elementos diagonales. $tr(R) = p$.

### 5.8 Visualizaciones Multivariadas Avanzadas
Mosaicos, Scatterplots, Dispersogramas, Coordenadas Paralelas, Perfiles Multivariados, Curvas de Nivel, Estrellas y Caras de Chernoff.

---

## UNIDAD 6: Limpieza de Datos (Data Cleaning) y Estadística Robusta

### 6.1 Ciclo de Vida del Análisis y Diagnóstico de Datos
1. Recolección -> 2. Almacenamiento -> 3. Limpieza (*Data Cleaning*) -> 4. Análisis -> 5. Visualización/Modelado.

### 6.2 Valores Inconsistentes vs. Atípicos (*Outliers*)
- **Valor Inconsistente**: Sin coherencia lógica (ej: Edad = 250). **Debe eliminarse o corregirse siempre**.
- **Valor Atípico (*Outlier*)**: Valor real alejado del patrón pero posible (ej: Edad = 105). Requiere inspección cuidadosa.

### 6.3 Tratamiento de Duplicados
`df.duplicated()` identifica filas repetidas. `df.drop_duplicates()` elimina la duplicación para evitar sobrerrepresentación.

### 6.4 Manejo de Valores Faltantes (MCAR, MAR, MNAR) e Imputación
- **MCAR (Completamente al Azar)**: Sin patrón ni sesgo. Se puede aplicar eliminación (`dropna()`).
- **MAR (al Azar)**: Condicionado por otras variables. Requiere imputación (`fillna()`, media/mediana/KNN).
- **MNAR (No al Azar)**: La falta depende de la propia variable. Requiere modelos especiales.

### 6.5 Transformación y Escalado de Variables
- **Estandarización $Z$-score**: $Z = \frac{X - \mu}{\sigma}$ (media 0, varianza 1).
- **Escalado Min-Max**: $X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$ (rango $[0, 1]$).
- **Transformación Logarítmica**: $X' = \log(X + 1)$ (suaviza asimetría positiva).
- **Discretización (*Binning*)**: `pd.cut()` (cortes fijos), `pd.qcut()` (por cuantiles).
- **One-Hot Encoding**: `pd.get_dummies()` para variables categóricas.

### 6.6 Detección de Outliers Univariados y Robustez (MAD/MADN)
- Criterio $3\sigma$, Rango Intercuartílico ($Q_1 - 1.5RI, Q_3 + 1.5RI$), y desviaciones robustas con MADN.

### 6.7 Outliers Multivariados, Mahalanobis, MVE y MCD
- **Efectos de interacción**: Enmascaramiento (un outlier oculta a otro) e Inundación (un dato es outlier solo por la presencia de otro).
- **Distancia de Mahalanobis**: Considera la correlación entre variables:
  $$d_m(X, Y) = \sqrt{(X - Y)^t \Sigma^{-1} (X - Y)}$$
- **Estimadores Robustos**:
  - **MVE (*Minimum Volume Ellipsoid*)**: Elipsoide de menor volumen que cubre $m$ de $n$ datos.
  - **MCD (*Minimum Covariance Determinant*)**: Minimiza el determinante de la matriz de covarianzas de $m$ observaciones de las $n$ disponibles.
