# Síntesis Temática — Capítulo 2: Introducción al Análisis de Datos

> **Libro**: *Análisis inteligente de datos con lenguaje R* (Chan, Badano y Rey)  
> **Cátedra**: Introducción al Análisis de Datos — UTN  
> **Documento temático generado mediante especificación SDD**

---

## Tabla de Contenidos
1. [Resumen del Capítulo](#1-resumen-del-capítulo)
2. [Eje 1: Variables y Niveles de Medición](#2-eje-1-variables-y-niveles-de-medición)
3. [Eje 2: Presentación de Datos y Tablas de Frecuencias](#3-eje-2-presentación-de-datos-y-tablas-de-frecuencias)
4. [Eje 3: Medidas Descriptivas Univariadas](#4-eje-3-medidas-descriptivas-univariadas)
   - [4.1 Medidas de Tendencia Central](#41-medidas-de-tendencia-central)
   - [4.2 Estadísticos de Orden y Posición](#42-estadísticos-de-orden-y-posición)
   - [4.3 Medidas de Dispersión Absoluta y Relativa](#43-medidas-de-dispersión-absoluta-y-relativa)
   - [4.4 Medidas de Forma: Asimetría y Curtosis](#44-medidas-de-forma-asimetría-y-curtosis)
5. [Eje 4: Representaciones Gráficas Univariadas y Boxplots](#5-eje-4-representaciones-gráficas-univariadas-y-boxplots)
6. [Eje 5: Análisis Multivariado y Matrices de Datos](#6-eje-5-análisis-multivariado-y-matrices-de-datos)
   - [5.1 Estructura Matriz de Datos y Crecimiento de Parámetros](#51-estructura-matriz-de-datos-y-crecimiento-de-parámetros)
   - [5.2 Vector de Medias, Matriz de Covarianzas y Correlación](#52-vector-de-medias-matriz-de-covarianzas-y-correlación)
   - [5.3 Gráficos Multivariados Avanzados](#53-gráficos-multivariados-avanzados)
7. [Eje 6: Transformaciones de Datos](#7-eje-6-transformaciones-de-datos)
8. [Eje 7: Estadística Robusta y Outliers Multivariados](#8-eje-7-estadística-robusta-y-outliers-multivariados)

---

## 1. Resumen del Capítulo

El **Capítulo 2** aborda la estadística descriptiva univariada y multivariada. Comienza definiendo la clasificación de variables y la construcción de tablas de frecuencias, avanza hacia las medidas de tendencia central, dispersión, asimetría y curtosis, y profundiza en las representaciones gráficas y el análisis multidimensional de datos. Finalmente, introduce las **transformaciones de datos** y la **estadística robusta** (distancia de Mahalanobis, estimadores MVE y MCD) para la detección de *outliers*.

---

## 2. Eje 1: Variables y Niveles de Medición

Las variables se clasifican en función de su escala y nivel de medición:

1. **Categóricas o Cualitativas**: Las modalidades no tienen orden numérico (ej: sexo, color de ojos, tipo de vehículo).
2. **Cuasicuantitativas u Ordinales**: Permiten establecer un orden pero no cuantificar la distancia entre categorías (ej: nivel de satisfacción, estadío de una enfermedad I-IV, calificación A-E).
3. **Cuantitativas Discretas**: Toman valores numéricos aislados o contables (ej: cantidad de hijos, materias aprobadas).
4. **Cuantitativas Continuas**: Toman infinitos valores intermedios dentro de un intervalo (ej: peso, estatura, tiempo de espera).
5. **Escalas Analógicas / Visuales (VAS)**: Escalas subjetivas (ej: nivel de dolor entre 0 y 10) usadas para evaluar evoluciones intra-individuo.

---

## 3. Eje 2: Presentación de Datos y Tablas de Frecuencias

- **Frecuencia Absoluta ($f_i$)**: Cantidad de observaciones que pertenecen a la clase $i$. Se cumple que $\sum_{i=1}^m f_i = n$.
- **Frecuencia Relativa**: Cociente $f_i / n$.
- **Frecuencia Porcentual ($f_{\%i}$)**: $(f_i / n) \times 100$.
- **Frecuencia Acumulada ($F_i$)**: Suma de las frecuencias absolutas hasta la clase $k$: $F_k = \sum_{i=1}^k f_i$.

---

## 4. Eje 3: Medidas Descriptivas Univariadas

### 4.1 Medidas de Tendencia Central
- **Media Aritmética ($\bar{x}$)**: $\bar{x} = \frac{1}{n} \sum x_i$. Sensible a valores extremos (no robusta). Preserva transformaciones lineales ($\bar{y} = a\bar{x} + b$).
- **Mediana ($\tilde{x}$)**: Valor central que divide la muestra ordenada al 50%. Robusta ante *outliers*.
- **Moda ($Mo$)**: Valor de mayor frecuencia observada. Puede ser multimodal.
- **Media $\alpha$-podada ($\bar{x}_\alpha$)**: Promedio recortando el $\alpha\%$ de valores extremos superiores e inferiores (ej: $\alpha = 10\%$).

### 4.2 Estadísticos de Orden y Posición
- **Cuantiles / Cuartiles ($Q_1, Q_2, Q_3$)**: Dividen los datos en 4 partes iguales del $25\%$. $Q_2$ coincide con la mediana.

### 4.3 Medidas de Dispersión Absoluta y Relativa
- **Rango muestral**: $rg(x) = x^{(n)} - x^{(1)}$.
- **Varianza muestral ($s_x^2$)**: $s_x^2 = \frac{1}{n-1} \sum (x_i - \bar{x})^2$.
- **Desviación estándar ($s_x$)**: $s_x = \sqrt{s_x^2}$. Unidades iguales a los datos.
- **Coeficiente de variación ($CV$)**: $CV = \frac{s_x}{\bar{x}} \times 100\%$. Dispersión relativa adimensional para comparar grupos con distintas unidades o medias.
- **Rango Intercuartílico ($RI$)**: $RI = Q_3 - Q_1$. Robusto.
- **MAD / MADN**: Mediana de desvíos absolutos respecto a la mediana. Normalización: $MADN = \frac{MAD}{0.6745}$.

### 4.4 Medidas de Forma: Asimetría y Curtosis
- **Asimetría de Fisher ($sk_F$)**: Describe el sesgo respecto a la media.
- **Asimetría de Pearson ($sk_P$)**: $sk_P = \frac{\bar{x} - Mo}{s_x}$.
- **Asimetría de Bowley ($sk_B$)**: Basada en cuartiles: $sk_B = \frac{Q_3 + Q_1 - 2\tilde{x}}{Q_3 - Q_1}$.
- **Curtosis ($k(x)$)**: Grado de apuntamiento / comportamiento de colas. En la distribución Normal $k \cong 3$.
  - Leptocúrtica: $k > 3$
  - Mesocúrtica: $k = 3$
  - Platicúrtica: $k < 3$

---

## 5. Eje 4: Representaciones Gráficas Univariadas y Boxplots

- **Gráfico circular / 3D / Anidados**: Cualitativas / Ordinales.
- **Gráfico de barras / Bastones**: Cualitativas / Discretas.
- **Histograma y Polígono de frecuencias**: Continuas. Reglas para número de clases $k$:
  - Sturges: $k = \lfloor 1 + \log_2(n) \rfloor$
  - Velleman: $k = \lfloor 2\sqrt{n} \rfloor$
  - Dixon-Kronmal: $k = \lfloor 10\log(n) \rfloor$
- **Boxplot (Diagrama de Caja)**: Muestra $Q_1, \tilde{x}, Q_3$, y define bigotes a $1.5 \times RI$.
  - *Outliers moderados*: entre $1.5 \times RI$ y $3 \times RI$.
  - *Outliers severos*: a distancia mayor a $3 \times RI$.
  - **Regla de 3-Sigma**: Outliers donde $|t_i| = \left| \frac{x_i - \bar{x}}{s} \right| > 3$.

---

## 6. Eje 5: Análisis Multivariado y Matrices de Datos

### 5.1 Estructura Matriz de Datos y Crecimiento de Parámetros
Una matriz de datos $X \in \mathbb{R}^{n \times p}$ contiene $n$ observaciones (filas) y $p$ variables (columnas).

Para analizar $p$ variables se deben estimar $p$ medias, $p$ varianzas y $\frac{p(p-1)}{2}$ covarianzas. El número total de parámetros a estimar crece de forma cuadrática:

$$\text{Total Parámetros} = \frac{p^2 + 3p}{2}$$

### 5.2 Vector de Medias, Matriz de Covarianzas y Correlación
- **Vector de Medias**: $\bar{x} = (\bar{x}_1, \bar{x}_2, \dots, \bar{x}_p) \in \mathbb{R}^p$.
- **Matriz de Covarianzas ($\hat{\Sigma}$)**: Matriz simétrica de tamaño $p \times p$ con varianzas en la diagonal y covarianzas $s_{ik}$ fuera de ella.
- **Matriz de Correlaciones ($R$)**: Matriz simétrica con unos en la diagonal y coeficientes de correlación $r_{ik} \in [-1, 1]$ fuera de ella.
- **Traza ($tr(A)$)**: Suma de la diagonal principal. $tr(R) = p$ (cantidad de variables).

### 5.3 Gráficos Multivariados Avanzados
- **Mosaicos**: Distribución conjunta de variables categóricas.
- **Scatterplots y Dispersogramas**: Matriz de gráficos de dispersión de a pares.
- **Coordenadas Paralelas**: Representación de observaciones $p$-dimensionales en ejes paralelos.
- **Perfiles Multivariados**: Comparación de medias/medianas por subgrupos.
- **Curvas de Nivel**: Identificación de regiones de igual densidad de probabilidad.
- **Gráficos de Estrellas y Caras de Chernoff**: Detección visual de similitudes entre individuos/marcas.

---

## 7. Eje 6: Transformaciones de Datos

- **Transformaciones por variable**:
  - Estandarización $Z$-score: $Z = \frac{X - \bar{x}}{s}$.
  - Min-Max: $X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$.
  - Logarítmica: $X' = \log(X + 1)$.
- **Transformaciones por individuo (por fila)**: Normalizan las respuestas de evaluadores/jueces para eliminar sesgos de severidad o benevolencia.

---

## 8. Eje 7: Estadística Robusta y Outliers Multivariados

En casos multivariados se observan dos efectos característicos:
- **Efecto de Enmascaramiento**: Un grupo de *outliers* oculta la presencia de otros.
- **Efecto de Inundación**: Una observación califica como *outlier* sólo por la presencia de otra.

### Distancia de Mahalanobis
Mide la distancia de un punto al centro considerando la correlación entre variables:

$$d_m(X, Y) = \sqrt{(X - Y)^t \Sigma^{-1} (X - Y)}$$

### Estimadores Robustos
- **MVE (*Minimum Volume Ellipsoid*)**: Busca el elipsoide de menor volumen que cubre $m$ de las $n$ observaciones.
- **MCD (*Minimum Covariance Determinant*)**: Minimiza el determinante de la matriz de covarianzas de un subconjunto $m$ de las $n$ observaciones.
