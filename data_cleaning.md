# Guía Completa de Limpieza y Preprocesamiento de Datos (Data Cleaning)

> **Materia**: Análisis de Datos (UTN)  
> **Cátedra**: Introducción al Análisis de Datos — Fernández, Luis Nahuel  
> **Documento generado mediante especificación SDD**

---

## Tabla de Contenidos
1. [Introducción y Etapas del Análisis de Datos](#1-introducción-y-etapas-del-análisis-de-datos)
2. [Valores Inconsistentes vs. Valores Atípicos (Outliers)](#2-valores-inconsistentes-vs-valores-atípicos-outliers)
3. [Tratamiento de Registros Duplicados](#3-tratamiento-de-registros-duplicados)
4. [Manejo de Valores Faltantes (No Respuesta / NaNs)](#4-manejo-de-valores-faltantes-no-respuesta--nans)
   - [4.1 Patrones de la No Respuesta](#41-patrones-de-la-no-respuesta)
   - [4.2 Posibles Soluciones (Eliminación vs Imputación)](#42-posibles-soluciones-eliminación-vs-imputación)
5. [Transformación y Escalado de Datos](#5-transformación-y-escalado-de-datos)
   - [5.1 Estandarización Z-score](#51-estandarización-z-score)
   - [5.2 Escalado Min-Max](#52-escalado-min-max)
   - [5.3 Transformación Logarítmica](#53-transformación-logarítmica)
   - [5.4 Discretización / Binning](#54-discretización--binning)
   - [5.5 Codificación Categórica (One-Hot Encoding)](#55-codificación-categórica-one-hot-encoding)
6. [Detección y Tratamiento de Outliers (Univariado y Multivariado)](#6-detección-y-tratamiento-de-outliers-univariado-y-multivariado)
   - [6.1 Regla de los Tres Desvíos](#61-regla-de-los-tres-desvíos)
   - [6.2 Criterio del Rango Intercuartílico (IQR)](#62-criterio-del-rango-intercuartílico-iqr)
   - [6.3 Medidas Robustas: MAD y MADN](#63-medidas-robustas-mad-y-madn)
   - [6.4 Outliers Multivariados y Distancia de Mahalanobis](#64-outliers-multivariados-y-distancia-de-mahalanobis)

---

## 1. Introducción y Etapas del Análisis de Datos

La limpieza y el preprocesamiento representan la etapa previa fundamental a cualquier modelo descriptivo, predictivo o estadístico.

### Ciclo de Vida del Análisis de Datos:
1. **Recolección de los datos**: Captura desde bases de datos, APIs, archivos CSV/Excel o web scraping.
2. **Almacenamiento**: Persistencia estructurada en data warehouses o sistemas de archivos.
3. **Limpieza y preprocesamiento de datos (*Data Cleaning*)**: Saneamiento de nulos, duplicados, inconsistencias y transformaciones.
4. **Análisis exploratorio y estadístico**: Extracción de patrones y pruebas de hipótesis.
5. **Visualización y/o modelado**: Comunicación gráfica y algoritmos de machine learning.

---

## 2. Valores Inconsistentes vs. Valores Atípicos (Outliers)

Es crucial distinguir entre un dato inconsistente y un dato atípico:

| Característica | Valor Inconsistente | Valor Atípico (*Outlier*) |
| :--- | :--- | :--- |
| **Definición** | Dato que **carece de coherencia lógica** con respecto al dominio de la variable o los conocimientos previos. | Dato real alejado del patrón general de la distribución, pero posible en la realidad. |
| **Ejemplo** | Edad = `250 años`, Estatura = `-1.80m`, Coordenada geográfica fuera de la Tierra. | Edad = `105 años`, Salario de un deportista de élite. |
| **Tratamiento** | **Deben eliminarse o corregirse siempre**. Bajo ningún punto de vista pueden ser tenidos en cuenta. | **Inspección cuidadosa**. No necesariamente deben ser excluidos ni modificados; aportan información sobre casos extremos. |

---

## 3. Tratamiento de Registros Duplicados

Los datos duplicados generan sobrerrepresentación no deseada y conducen a estimaciones sesgadas de los parámetros estadísticos.

```python
import pandas as pd
import numpy as np

# Identificar filas duplicadas en un DataFrame
duplicados_mask = df.duplicated()
total_duplicados = duplicados_mask.sum()

print(f"Total de registros duplicados: {total_duplicados}")

# Eliminar duplicados manteniendo la primera ocurrencia
df_limpio = df.drop_duplicates(keep="first")

# Eliminar duplicados basados en columnas específicas (ej: por ID)
df_unicos = df.drop_duplicates(subset=["ID_Usuario"], keep="last")
```

---

## 4. Manejo de Valores Faltantes (No Respuesta / NaNs)

### 4.1 Patrones de la No Respuesta

El enfoque para resolver la falta de datos depende de la naturaleza probabilística de la ausencia:

1. **Faltantes Completamente al Azar (MCAR - *Missing Completely at Random*)**:
   - La causa de la ausencia no tiene relación con ninguna variable del estudio.
   - **Efecto**: No introduce sesgo en las estimaciones.
   - **Solución típica**: Eliminación de registros (*listwise deletion*).

2. **Faltantes al Azar (MAR - *Missing at Random*)**:
   - La ausencia depende de otras variables observadas en la base, pero no del valor propio de la variable faltante.
   - **Solución típica**: Imputación condicional o modelos de regresión/KNN.

3. **Faltantes No al Azar (MNAR - *Missing Not at Random*)**:
   - La ausencia depende directamente del valor no observado (ej: personas de ingresos muy altos que se niegan a responder su sueldo).
   - **Efecto**: Introduce un sesgo grave si se elimina. Requiere modelos avanzados de imputación o análisis de sensibilidad.

### 4.2 Posibles Soluciones (Eliminación vs Imputación)

```python
# 1. Detección de nulos
nulos_por_columna = df.isna().sum()
porcentaje_nulos = (df.isna().sum() / len(df)) * 100

# 2. Eliminación (dropna)
df_sin_nulos = df.dropna()                        # Elimina filas con al menos 1 nulo
df_col_limpias = df.dropna(axis=1, thresh=0.8*len(df)) # Conserva cols con al menos 80% datos válidos

# 3. Imputación (fillna)
df["Edad_imputada"] = df["Edad"].fillna(df["Edad"].median()) # Imputación por mediana
df["Estado_imputado"] = df["Estado"].fillna("Desconocido")    # Imputación por valor constante

# 4. Imputación avanzada mediante Scikit-Learn (SimpleImputer / KNNImputer)
from sklearn.impute import SimpleImputer, KNNImputer

imputer_knn = KNNImputer(n_neighbors=5)
df_imputado = pd.DataFrame(imputer_knn.fit_transform(df_num), columns=df_num.columns)
```

---

## 5. Transformación y Escalado de Datos

Las transformaciones se aplican para hacer comparables las magnitudes, modificar escalas de medición o cumplir supuestos de modelos estadísticos.

### 5.1 Estandarización Z-score

Transforma la variable para tener **media 0** y **varianza 1**:

$$Z = \frac{X - \mu}{\sigma}$$

```python
df["Z_score"] = (df["Variable"] - df["Variable"].mean()) / df["Variable"].std()
```

### 5.2 Escalado Min-Max

Comprime los valores dentro del rango $[0, 1]$:

$$X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$$

```python
df["MinMax"] = (df["Variable"] - df["Variable"].min()) / (df["Variable"].max() - df["Variable"].min())
```

### 5.3 Transformación Logarítmica

Suaviza distribuciones fuertemente asimétricas a derecha (con *heavy tails*):

$$X' = \log(X + 1)$$

```python
df["Log_Variable"] = np.log1p(df["Variable"])
```

### 5.4 Discretización / Binning

Convierte variables cuantitativas continuas en categorías ordinales:

```python
# pd.cut: Intervalos definidos por cortes explícitos
criterios = [0, 18, 65, 100]
etiquetas = ["Joven", "Adulto", "Adulto Mayor"]
df["Grupo_Etario"] = pd.cut(df["Edad"], bins=criterios, labels=etiquetas)

# pd.qcut: Intervalos basados en cuantiles (cuartiles, deciles)
df["Cuartil_Ingreso"] = pd.qcut(df["Ingreso"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
```

### 5.5 Codificación Categórica (One-Hot Encoding)

Convierte variables categóricas no ordinales en columnas binarias (variables *dummy*):

```python
df_encoded = pd.get_dummies(df, columns=["Nacionalidad"], prefix="Nac", drop_first=True)
```

---

## 6. Detección y Tratamiento de Outliers (Univariado y Multivariado)

### 6.1 Regla de los Tres Desvíos
Para distribuciones aproximadamente normales, el $99.73\%$ de las observaciones cae dentro de $\mu \pm 3\sigma$.

$$\text{Outlier si: } |t_i| = \left| \frac{x_i - \bar{x}}{s} \right| > 3$$

```python
z_scores = np.abs((df["Valor"] - df["Valor"].mean()) / df["Valor"].std())
outliers_3sigma = df[z_scores > 3]
```

### 6.2 Criterio del Rango Intercuartílico (IQR)
Criterio robusto no paramétrico:

$$RI = Q_3 - Q_1$$

- **Outlier Moderado**: Fuera del rango $[Q_1 - 1.5 \cdot RI, \quad Q_3 + 1.5 \cdot RI]$
- **Outlier Severo**: Fuera del rango $[Q_1 - 3 \cdot RI, \quad Q_3 + 3 \cdot RI]$

```python
Q1 = df["Valor"].quantile(0.25)
Q3 = df["Valor"].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers_iqr = df[(df["Valor"] < limite_inferior) | (df["Valor"] > limite_superior)]
```

### 6.3 Medidas Robustas: MAD y MADN

La **MAD** (*Median Absolute Deviation*) es la mediana de los desvíos absolutos respecto de la mediana:

$$MAD(X) = \text{mediana}(|X - \tilde{x}|)$$

Para hacer la MAD comparable con la desviación estándar en distribuciones gaussianas se normaliza por $0.6745$:

$$MADN(X) = \frac{MAD(X)}{0.6745}$$

```python
mediana = df["Valor"].median()
mad = np.median(np.abs(df["Valor"] - mediana))
madn = mad / 0.6745

print(f"MAD: {mad:.4f}, MADN: {madn:.4f}")
```

### 6.4 Outliers Multivariados y Distancia de Mahalanobis

En casos multidimensionales, una observación puede no ser outlier en ninguna variable por separado, pero sí en la relación conjunta entre ellas.

La **Distancia de Mahalanobis** contempla la matriz de covarianzas $\Sigma$:

$$d_m(X, Y) = \sqrt{(X - Y)^t \Sigma^{-1} (X - Y)}$$

Para evitar que los mismos outliers distorsionen la estimación de la matriz de covarianzas, se utilizan estimadores robustos:
- **MVE** (*Minimum Volume Ellipsoid*): Busca el elipsoide de menor volumen que cubra $m$ de las $n$ observaciones.
- **MCD** (*Minimum Covariance Determinant*): Minimiza el determinante de la matriz de covarianzas de un subconjunto $m$ de las $n$ observaciones.

```python
# Ejemplo de detección multivariada con Scikit-Learn (EllipticEnvelope / MinCovDet)
from sklearn.covariance import MinCovDet

# Estimador robusto MCD
mcd = MinCovDet().fit(df_num)
distancias_mahalanobis = mcd.mahalanobis(df_num)

# Identificar outliers multivariados
corte = np.percentile(distancias_mahalanobis, 95)
outliers_multivariados = df[distancias_mahalanobis > corte]
```
