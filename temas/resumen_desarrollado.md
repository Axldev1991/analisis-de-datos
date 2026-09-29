# Desarrollo Exhaustivo de Conceptos de Análisis de Datos

> **Materia**: Análisis de Datos (UTN)  
> **Cátedra**: Introducción al Análisis de Datos — Fernández, Luis Nahuel  
> **Documento de desarrollo conceptual generado a partir de `resumen.md`**

---

## 📑 Tabla de Contenidos
1. [Sección 1: Conceptos Fundamentales](#sección-1-conceptos-fundamentales)
   - [1.1 Tipos de Datos: Estructurados, Semi-estructurados y No Estructurados](#11-tipos-de-datos-estructurados-semi-estructurados-y-no-estructurados)
   - [1.2 Big Data y la Evolución Histórica desde 1970](#12-big-data-y-la-evolución-histórica-desde-1970)
   - [1.3 Procesamiento de Datos vs. Minería de Datos (Data Mining)](#13-procesamiento-de-datos-vs-minería-de-datos-data-mining)
   - [1.4 Ronald Fisher: ANOVA, Principio de Fisher e Hipótesis del Hijo Sexy](#14-ronald-fisher-anova-principio-de-fisher-e-hipótesis-del-hijo-sexy)
   - [1.5 Evolución Post Segunda Guerra Mundial: De la Estadística Clásica al Data Mining](#15-evolución-post-segunda-guerra-mundial-de-la-estadística-clásica-al-data-mining)
   - [1.6 El Proceso KDD (Knowledge Discovery in Databases)](#16-el-proceso-kdd-knowledge-discovery-in-databases)
   - [1.7 Tecnología M2M (Machine to Machine)](#17-tecnología-m2m-machine-to-machine)
   - [1.8 Niveles de Análisis: Univariado, Bivariado y Multivariado](#18-niveles-de-análisis-univariado-bivariado-y-multivariado)
   - [1.9 Clasificación y Niveles de Medición de Variables](#19-clasificación-y-niveles-de-medición-de-variables)
   - [1.10 Reducción de Dimensionalidad y Métodos Factoriales](#110-reducción-de-dimensionalidad-y-métodos-factoriales)
     - [Análisis de Componentes Principales (ACP)](#análisis-de-componentes-principales-acp)
     - [Análisis de Correspondencias](#análisis-de-correspondencias)
   - [1.11 Análisis de Clusters (Clustering No Supervisado)](#111-análisis-de-clusters-clustering-no-supervisado)
   - [1.12 Procesamiento Inductivo vs. Deductivo](#112-procesamiento-inductivo-vs-deductivo)
   - [1.13 Minería de Texto (Text Mining)](#113-minería-de-texto-text-mining)
2. [Sección 2: NumPy (Numerical Python)](#sección-2-numpy-numerical-python)
   - [2.1 ¿Qué es NumPy y para qué sirve?](#21-qué-es-numpy-y-para-qué-sirve)
   - [2.2 IoT (Internet of Things) y el Flujo de Datos Numéricos](#22-iot-internet-of-things-y-el-flujo-de-datos-numéricos)
   - [2.3 El Objeto `ndarray`: Estructura, Atributos y Métodos](#23-el-objeto-ndarray-estructura-atributos-y-métodos)
   - [2.4 Vectorización e Instrucciones SIMD del Hardware](#24-vectorización-e-instrucciones-simd-del-hardware)
   - [2.5 Ensamblaje de Matrices y Funciones Generadoras](#25-ensamblaje-de-matrices-y-funciones-generadoras)
   - [2.6 Pipelines de Computación Numérica](#26-pipelines-de-computación-numérica)
3. [Sección 3: Pandas](#sección-3-pandas)
   - [3.1 ¿Qué es Pandas y para qué sirve?](#31-qué-es-pandas-y-para-qué-sirve)
   - [3.2 El Enfoque en Pandas y Manejo de Estructuras Tabulares](#32-el-enfoque-en-pandas-y-manejo-de-estructuras-tabulares)
   - [3.3 Las Estructuras Clave: `Series` y `DataFrame`](#33-las-estructuras-clave-series-y-dataframe)
   - [3.4 Vectorización y Alineación por Índices](#34-vectorización-y-alineación-por-índices)
   - [3.5 Selección con `loc` e `iloc`](#35-selección-con-loc-e-iloc)
4. [Sección 4: Limpieza y Preprocesamiento de Datos (Data Cleaning)](#sección-4-limpieza-y-preprocesamiento-de-datos-data-cleaning)
   - [4.1 Las 5 Etapas del Ciclo de Datos](#41-las-5-etapas-del-ciclo-de-datos)
   - [4.2 Sobre-representación y Duplicación de Datos](#42-sobre-representación-y-duplicación-de-datos)
   - [4.3 Valores Perdidos / No Respuesta (MCAR, MAR, MNAR)](#43-valores-perdidos--no-respuesta-mcar-mar-mnar)
   - [4.4 Valores Inconsistentes vs. Valores Atípicos (Outliers)](#44-valores-inconsistentes-vs-valores-atípicos-outliers)
   - [4.5 Efecto de Enmascaramiento (Masking Effect)](#45-efecto-de-enmascaramiento-masking-effect)

---

## Sección 1: Conceptos Fundamentales

### 1.1 Tipos de Datos: Estructurados, Semi-estructurados y No Estructurados

La información en sistemas informáticos se clasifica en tres grandes formas según su grado de organización interna:

- **Datos Estructurados**: Datos que se ajustan estrictamente a un esquema rígido y relacional prefijado, organizados en tablas con filas (registros/individuos $n$) y columnas (atributos/variables $p$).
  - *Ejemplos*: Tablas SQL, matrices numéricas, archivos CSV alineados.
- **Datos Semi-estructurados**: Datos que no poseen un esquema relacional fijo pero incorporan marcas, etiquetas o metadatos jerárquicos que separan los campos.
  - *Ejemplos*: Archivos JSON, XML, YAML, documentos NoSQL (MongoDB).
- **Datos No Estructurados**: Información amorfa que no posee una estructura interna predefinida y requiere algoritmos avanzados de extracción (NLP, visión por computadora) para ser analizada.
  - *Ejemplos*: Documentos de texto libre, correos electrónicos, imágenes, archivos de audio, video y registros (*logs*) crudos.

---

### 1.2 Big Data y la Evolución Histórica desde 1970

A partir de la década de 1970 y acelerándose exponencialmente con la llegada de la **World Wide Web (1990)** y los dispositivos móviles, la capacidad de generar y almacenar datos superó la capacidad de procesamiento de la estadística tradicional.

El paradigma de **Big Data** se define clásicamente por las **V**:
1. **Volumen**: Escala masiva de datos (terabytes, petabytes).
2. **Velocidad**: Frecuencia de generación e ingesta en tiempo real (ej: *streaming* de transacciones, sensores).
3. **Variedad**: Convivencia de datos estructurados, semi-estructurados y no estructurados.
4. **Veracidad**: Incertidumbre y sesgos que deben ser corregidos mediante *Data Cleaning*.
5. **Valor**: Capacidad de convertir los datos en conocimiento accionable para la toma de decisiones.

---

### 1.3 Procesamiento de Datos vs. Minería de Datos (Data Mining)

- **Procesamiento de Datos (ETL - Extract, Transform, Load)**: Operaciones de manipulación computacional enfocadas en la recolección, formateo, almacenamiento y consulta eficiente de información. No busca descubrir nuevas relaciones; su objetivo es la gestión y sanidad del dato.
- **Minería de Datos (*Data Mining*)**: Subcampo interdisciplinario que aplica algoritmos matemáticos, computacionales y estadísticos sobre bases de datos masivas para **descubrir patrones, tendencias, anomalías y relaciones no evidentes**.

---

### 1.4 Ronald Fisher: ANOVA, Principio de Fisher e Hipótesis del Hijo Sexy

Sir **Ronald A. Fisher (1890-1962)** es considerado el padre de la estadística moderna. Sus aportes clave incluyen:

1. **Análisis de Varianza (ANOVA)**: Técnica estadística que permite comparar las medias de tres o más grupos evaluando si las diferencias observadas entre las medias son estadísticamente significativas con respecto a la variabilidad interna de cada grupo.
2. **Principio de Fisher**: Explicación evolutiva de por qué la proporción de sexos (macho/hembra) se mantiene aproximadamente 1:1 en la mayoría de las especies que se reproducen sexualmente, basada en la selección dependiente de la frecuencia.
3. **Hipótesis del *Hijo Sexy* (*Runaway Selection*)**: Modelo de selección sexual evolutiva donde las hembras eligen machos con ciertos rasgos ornamentales exagerados. Las hijas heredan la preferencia por dicho rasgo y los hijos heredan el rasgo atractivo ("sexy"), acelerando la evolución del adorno.

---

### 1.5 Evolución Post Segunda Guerra Mundial: De la Estadística Clásica al Data Mining

- **Estadística Clásica (Pre-computacional / Siglo XIX y principios del XX)**: Diseñada para situaciones donde la recolección de datos era costosa y difícil. Se basaba en el enfoque **hipotético-deductivo**: formular una hipótesis antes de mirar los datos, tomar una muestra pequeña y aplicar inferencia confirmatoria asumiendo distribuciones teóricas (ej. Normalidad).
- **Transición Post Segunda Guerra Mundial**: La invención de la computadora digital permitió acumular datos de forma automática. Surgió la necesidad de explorar datos sin hipótesis previas.
- **Minería de Datos (Años 1990+)**: Adopta el enfoque **inductivo**: partir de grandes volúmenes de datos empíricos para que los propios algoritmos descubran los patrones subyacentes sin imponer supuestos iniciales rígidos.

---

### 1.6 El Proceso KDD (Knowledge Discovery in Databases)

El descubrimiento de conocimiento en bases de datos es un proceso iterativo de 5 etapas:

```
[Datos Crudos] ──► 1. Selección ──► 2. Limpieza/Preprocesamiento ──► 3. Transformación ──► 4. Data Mining ──► 5. Evaluación/Interpretación ──► [Conocimiento]
```

1. **Selección**: Filtrar el conjunto de datos de interés a partir de la fuente general.
2. **Limpieza y Preprocesamiento**: Eliminar ruido, corregir inconsistencias y tratar datos nulos/duplicados.
3. **Transformación**: Reducir dimensionalidad, escalar atributos ($Z$-score, Min-Max) o codificar variables.
4. **Data Mining**: Aplicación de algoritmos (clasificación, regresión, *clustering*, reglas de asociación).
5. **Evaluación e Interpretación**: Validar los patrones descubiertos y traducirlos a conocimiento accionable.

---

### 1.7 Tecnología M2M (Machine to Machine)

Refiere a las tecnologías que permiten a dispositivos y máquinas remotas comunicarse entre sí e intercambiar datos de forma autónoma sin intervención humana.

- *Aplicaciones*: Monitoreo de peajes automáticos (Telepase), telemantenimiento de ascensores, terminales punto de venta (POS), contadores inteligentes de electricidad/agua y gestión de flotas por GPS.

---

### 1.8 Niveles de Análisis: Univariado, Bivariado y Multivariado

- **Análisis Univariado**: Estudio de una sola variable de forma aislada.
  - *Objetivo*: Describir centralidad ($\bar{x}, \tilde{x}$), dispersión ($s_x, RI$) y distribución (histograma, boxplot).
- **Análisis Bivariado**: Estudio simultáneo de dos variables.
  - *Objetivo*: Determinar el grado y sentido de la asociación entre ambas (covarianza $s_{xy}$, correlación de Pearson $r_{xy}$, *scatterplots*, tablas de contingencia).
- **Análisis Multivariado**: Estudio conjunto de $p \ge 3$ variables evaluadas sobre $n$ individuos.
  - *Objetivo*: Captar la estructura global de relaciones inter-variables y detectar patologías complejas que no son visibles en 1 o 2 dimensiones.

---

### 1.9 Clasificación y Niveles de Medición de Variables

1. **Cualitativas o Categóricas**: Modalidades no numéricas sin orden inherente.
   - *Ejemplo*: Color de vehículo, Estado civil, Nacionalidad.
2. **Cuasicuantitativas u Ordinales**: Modalidades categóricas que poseen un orden lógico, aunque la distancia entre categorías no se puede medir.
   - *Ejemplo*: Nivel de instrucción (Primario, Secundario, Universitario), Calificación (A, B, C, D), Gravedad médica (Estadío I, II, III, IV).
3. **Cuantitativas Discretas**: Variables numéricas cuyos valores provienen generalmente de un conteo numerable (pasos enteros).
   - *Ejemplo*: Cantidad de hijos, número de materias aprobadas.
4. **Cuantitativas Continuas**: Variables numéricas que pueden tomar infinitos valores intermedios dentro de un intervalo continuo, asociadas al proceso de medición.
   - *Ejemplo*: Peso, estatura, tiempo de respuesta, temperatura.

---

### 1.10 Reducción de Dimensionalidad y Métodos Factoriales

Cuando el número de atributos $p$ es muy elevado, surge la **maldición de la dimensionalidad** (*curse of dimensionality*): los datos se vuelven dispersos y el volumen del espacio crece exponencialmente. La reducción de dimensionalidad busca proyectar los datos a un subespacio de menor dimensión $k \ll p$ preservando la mayor cantidad de información/varianza.

#### Análisis de Componentes Principales (ACP)
- **Técnica cuantitativa no supervisada**.
- Transforma un conjunto de $p$ variables correlacionadas en un nuevo conjunto de variables incorrelacionadas linealmente llamadas **Componentes Principales** ($PC_1, PC_2, \dots$).
- La primera componente $PC_1$ se construye en la dirección de máxima varianza de los datos. La segunda $PC_2$ es ortogonal a la primera y captura la mayor varianza remanente.
- Matemáticamente se obtiene resolviendo la descomposición en autovalores y autovectores de la matriz de covarianzas $\Sigma$ o de correlaciones $R$.

#### Análisis de Correspondencias
- **Técnica factorial para variables cualitativas/categóricas**.
- Se aplica sobre tablas de contingencia (clasificación cruzada) para representar gráficamente las asociaciones entre las categorías de filas y columnas en un plano de pocas dimensiones.

---

### 1.11 Análisis de Clusters (Clustering No Supervisado)

El **Clustering** agrupa $n$ individuos en $K$ conjuntos (*clusters*) de modo que:
- La **homogeneidad intra-grupo** sea máxima (los elementos de un mismo cluster son muy parecidos entre sí).
- La **heterogeneidad inter-grupo** sea máxima (los clusters son claramente distintos entre sí).

No requiere etiquetas previas (*aprendizaje no supervisado*).  
*Métodos comunes*: **K-Means** (basado en centroides y distancia euclídea) y **Clustering Jerárquico** (dendrogramas aglomerativos o divisivos).

---

### 1.12 Procesamiento Inductivo vs. Deductivo

- **Método Deductivo (Estadística Clásica)**:
  $$\text{Teoría / Hipótesis general} \longrightarrow \text{Recolección de datos} \longrightarrow \text{Confirmación / Rechazo}$$
- **Método Inductivo (Minería de Datos)**:
  $$\text{Observación de datos masivos} \longrightarrow \text{Algoritmo / Minería} \longrightarrow \text{Descubrimiento de Patrones / Reglas}$$

---

### 1.13 Minería de Texto (Text Mining)

Consiste en la extracción automatizada de conocimiento útil a partir de grandes colecciones de documentos de texto en lenguaje natural no estructurado.

- *Técnicas clave*:
  - **Tokenización y Lematización/Stemming**: Reducción de palabras a su raíz o forma canónica.
  - **Bolsa de Palabras (Bag of Words) y TF-IDF**: Vectorización de texto según la frecuencia de términos y frecuencia inversa de documentos.
  - **Análisis de Sentimiento**: Clasificación de opiniones en positivo, negativo o neutro.

---

## Sección 2: NumPy (Numerical Python)

### 2.1 ¿Qué es NumPy y para qué sirve?

**NumPy** (*Numerical Python*) es la librería fundamental de código abierto para la **computación científica, matricial y numérica en Python**. Proporciona un objeto de arreglo $N$-dimensional de alto rendimiento denominado **`ndarray`**, así como rutinas optimizadas para operar sobre él.

#### ¿Para qué sirve NumPy?
1. **Procesamiento de Grandes Volúmenes de Datos Numéricos**: Permite almacenar y operar sobre vectores, matrices y tensores homogéneos en un bloque contiguo de memoria optimizado en C.
2. **Cómputo Vectorial de Alta Velocidad**: Elimina los bucles explícitos `for` de Python (que son lentos por la inspección de tipo dinámico) reemplazándolos por operaciones vectorizadas masivas.
3. **Álgebra Lineal y Estadística Avanzada**: Incluye el submódulo `np.linalg` para calcular productos de matrices, transposiciones, inversas, determinantes, sistemas de ecuaciones lineales, autovalores/autovectores y transformadas de Fourier.
4. **Base del Ecosistema de Data Science**: Constituye la infraestructura sobre la cual se apoyan **Pandas** (DataFrames), **SciPy** (cómputo científico), **Scikit-Learn** (Machine Learning) y motores de Deep Learning (**TensorFlow**, **PyTorch**).

---

### 2.2 IoT (Internet of Things) y el Flujo de Datos Numéricos

Los dispositivos **IoT** generan flujos masivos de lecturas numéricas continuas (temperatura, aceleración, presión). Para procesar estos torrentes de datos a alta velocidad en Python se requiere **NumPy**, ya que la estructura nativa `list` de Python resulta ineficiente en memoria y velocidad.

---

### 2.3 El Objeto `ndarray`: Estructura, Atributos y Métodos

El **`ndarray`** es un arreglo multidimensional homogéneo escrito en C.

#### Atributos Clave:
- **`shape`**: Tupla con las dimensiones de la matriz (ej. `(100, 5)` indica 100 filas y 5 columnas).
- **`dtype`**: Tipo de dato único de todos los elementos (ej. `float64`, `int32`).
- **`itemsize`**: Tamaño en bytes de cada elemento individual (ej. 8 bytes para `float64`).
- **`strides`**: Tupla que indica el número de bytes que se deben saltar en memoria para avanzar un elemento a lo largo de cada dimensión.
- **Metadatos**: Puntero a la dirección de memoria física donde inicia el bloque contiguo.

#### Métodos de Modificación de Forma:
- **`reshape(new_shape)`**: Cambia las dimensiones del array sin modificar los datos. Si el array es contiguo en memoria, genera una **vista** (*view*) sin copiar datos.
- **`flatten()`**: Convierte el array a 1D retornando siempre una **copia independiente** de los datos en memoria.
- **`ravel()`**: Aplana el array a 1D retornando una **vista** siempre que sea posible (más rápido y eficiente en memoria).

---

### 2.4 Vectorización e Instrucciones SIMD del Hardware

La **Vectorización** permite realizar operaciones matemáticas sobre arrays enteros sin escribir bucles `for` en Python.

- **Instrucciones SIMD (*Single Instruction, Multiple Data*)**: A nivel del procesador (CPU), los registros de hardware ejecutados por NumPy aplican una misma instrucción aritmética sobre múltiples datos numéricos simultáneamente en un único ciclo de reloj. Esto acelera la ejecución entre **10x y 100x** respecto a listas nativas.

---

### 2.5 Ensamblaje de Matrices y Funciones Generadoras

```python
import numpy as np

# Funciones de Creación
zeros = np.zeros((3, 3))        # Matriz 3x3 de ceros
ones = np.ones((2, 4))          # Matriz 2x4 de unos
arange = np.arange(0, 10, 2)    # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5) # 5 puntos equiespaciados entre 0 y 1

# Ensamblaje / Apilado de Matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

v_stacked = np.vstack((A, B)) # Apilado vertical (4x2)
h_stacked = np.hstack((A, B)) # Apilado horizontal (2x4)
concat = np.concatenate((A, B), axis=0) # Concatenación por eje
```

---

### 2.5 Pipelines de Computación Numérica

Un **Pipeline** en NumPy encadena transformaciones vectorizadas continuas sobre matrices de datos sin crear variables intermedias redundantes, optimizando la memoria caché del sistema.

```python
# Ejemplo de pipeline vectorial: Normalizar min-max y calcular media por columna
datos = np.random.rand(100, 5)
norm_pipeline = (datos - datos.min(axis=0)) / (datos.max(axis=0) - datos.min(axis=0))
resultado = norm_pipeline.mean(axis=0)
```

---

## Sección 3: Pandas

### 3.1 ¿Qué es Pandas y para qué sirve?

**Pandas** es la librería estándar de código abierto y de alto nivel en Python para la **manipulación, limpieza, transformación y análisis de datos estructurados y tabulares**. Construida sobre la infraestructura de cálculo numérico de NumPy, proporciona estructuras flexibles enriquecidas con etiquetas explícitas en filas (índices) y columnas.

#### ¿Para qué sirve Pandas?
1. **Ingesta y Carga Multiformato de Datos**: Importa y exporta datos fácilmente desde/hacia archivos CSV, Excel (`.xlsx`), JSON, bases de datos SQL, Parquet y HTML (`pd.read_csv()`, `pd.read_excel()`).
2. **Limpieza y Preparación Tabular (*Data Wrangling*)**: Facilita el tratamiento de valores faltantes (`dropna`, `fillna`), eliminación de duplicados (`drop_duplicates`), transformaciones de tipo de dato y filtrado de datos inconsistentes.
3. **Agrupamiento y Agregaciones Complejas (*Split-Apply-Combine*)**: Permite agrupar registros por categorías (`groupby()`) y aplicar agregaciones estadísticas como promedios, sumas, desviaciones y recuentos sobre subconjuntos.
4. **Unión y Combinación de Datasets**: Combina tablas a través de uniones relacionales tipo SQL (`pd.merge`) o apilados vectoriales (`pd.concat`) mediante claves comunes.
5. **Enriquecimiento y Extracción de Atributos (*Feature Engineering*)**: Procesa cadenas de texto (`.str`) y fechas (`.dt`) de forma vectorizada para alimentar modelos analíticos y de Machine Learning en Scikit-Learn.

---

### 3.2 El Enfoque en Pandas y Manejo de Estructuras Tabulares

Mientras NumPy opera sobre bloques numéricos puros homogéneos, Pandas está orientada a manejar **estructuras tabulares heterogéneas** (columnas con distintos tipos de datos: números, texto, fechas, booleanos) con etiquetas explícitas en filas (índices) y columnas.

---

### 3.3 Las Estructuras Clave: `Series` y `DataFrame`

1. **`Series`**: Estructura unidimensional etiquetada capaz de contener cualquier tipo de dato (`int`, `float`, `str`, `object`). Consta de dos componentes: un array de **datos** y un array de **etiquetas de índice** (`index`).
2. **`DataFrame`**: Estructura bidimensional (tabla) compuesta por una colección ordenada de columnas `Series` que comparten un mismo índice de filas.

```python
import pandas as pd

# Creación de DataFrame
df = pd.DataFrame({
    "Candidata": ["Mariana", "Maia", "Carla"],
    "Puntaje": [85, 90, 88]
})
```

---

### 3.4 Vectorización y Alineación por Índices

A diferencia de NumPy (que alinea por posición fija), Pandas realiza **alineación automática basada en etiquetas de índice**. Si dos `Series` tienen índices en distinto orden, Pandas empareja las etiquetas antes de realizar la operación matemática.

---

### 3.5 Selección con `loc` e `iloc`

| Método | Tipo de Selección | Ejemplo de Sintaxis |
| :--- | :--- | :--- |
| **`.loc[]`** | Basada estrictamente en **etiquetas / nombres** de filas y columnas | `df.loc[0:2, ['Candidata', 'Puntaje']]` |
| **`.iloc[]`** | Basada estrictamente en **posiciones enteras** (0-based) | `df.iloc[0:2, 0:2]` |

```python
# Filtrado booleano combinado
destacadas = df.loc[df["Puntaje"] >= 88, ["Candidata", "Puntaje"]]
```

---

## Sección 4: Limpieza y Preprocesamiento de Datos (Data Cleaning)

### 4.1 Las 5 Etapas del Ciclo de Datos

```
1. Recolección  ──►  2. Almacenamiento  ──►  3. Limpieza y Preprocesamiento  ──►  4. Análisis  ──►  5. Modelado / Visualización
```

La **limpieza de datos (Data Cleaning)** se ubica como la etapa previa indispensable para garantizar la sanidad y confiabilidad de los resultados analíticos.

---

### 4.2 Sobre-representación y Duplicación de Datos

Los registros duplicados o clonados generan **sobrerrepresentación** no deseada en el conjunto de observaciones, distorsionando promedios, desviaciones y modelos predictivos.

- *Solución en Pandas*:
  ```python
  # Detectar y eliminar filas duplicadas
  df_sin_duplicados = df.drop_duplicates(keep="first")
  ```

---

### 4.3 Valores Perdidos / No Respuesta (MCAR, MAR, MNAR)

Los valores faltantes (fantasmas o no respuesta) se clasifican según el mecanismo generador:

1. **Faltantes Soslayables / MCAR (*Missing Completely at Random*)**:
   - La no respuesta es absolutamente aleatoria y no depende de ninguna variable.
   - *Solución*: Eliminación directa de las filas (`df.dropna()`). No introduce sesgo.
2. **Faltantes No Soslayables**:
   - **MAR (*Missing at Random*)**: La falta depende de otras variables observadas.
   - **MNAR (*Missing Not at Random*)**: La falta depende del propio valor omitido.
   - *Solución*: **Imputación** de la media, mediana, reponderación muestral o modelos probabilísticos KNN/Regresión.

---

### 4.4 Valores Inconsistentes vs. Valores Atípicos (Outliers)

```
┌────────────────────────────────────────────────────────────────────────┐
│                        DIAGNÓSTICO DE DATOS                            │
├───────────────────────────────────┬────────────────────────────────────┤
│      VALORES INCONSISTENTES       │      VALORES ATÍPICOS (OUTLIERS)   │
├───────────────────────────────────┼────────────────────────────────────┤
│ Datos SIN coherencia lógica con   │ Datos REALES lejanos al patrón     │
│ respecto al tema o dominio.       │ general de la distribución.        │
│ Ejemplo: Edad = 250 años.         │ Ejemplo: Edad = 105 años.          │
│ ACCIÓN: Eliminar o corregir       │ ACCIÓN: Inspeccionar cuidadosamente│
│ obligatoriamente.                 │ antes de decidir excluir.          │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

### 4.5 Efecto de Enmascaramiento (Masking Effect)

En análisis multivariado, el **efecto de enmascaramiento** ocurre cuando un grupo de *outliers* altera fuertemente las estimaciones clásicas de la media y la matriz de covarianzas, haciendo que **otros outliers queden ocultos e invisibles** ante los métodos convencionales.

- *Solución*: Utilizar técnicas de **Estadística Robusta** como la **Distancia de Mahalanobis** basada en estimadores de alta ruptura como **MVE** (*Minimum Volume Ellipsoid*) o **MCD** (*Minimum Covariance Determinant*).

---

### 4.6 Transformación de Datos (Por Variables y por Individuos)

> *"En algunas ocasiones, para optimizar el análisis de la información disponible, es conveniente realizar transformaciones a los datos. Las transformaciones pueden ser por filas o por columnas, o sea por individuos o por variables, dependiendo de los objetivos de las mismas."*  
> — **Chan, Badano y Rey (2019)**

#### Objetivos más Usuales de la Transformación:
1. **Hacer comparables las magnitudes**: Eliminar distorsiones causadas por distintas unidades de medida (ej: comparar peso en kg con altura en cm).
2. **Modificar la escala de medición**: Convertir escalas continuas a categorías ordinales (*discretización/binning*) o viceversa.
3. **Satisfacer propiedades estadísticas**: Normalizar distribuciones asimétricas (mediante logaritmo) o estabilizar la varianza.

#### Clasificación de las Transformaciones:
- **Transformaciones por Variables (Columnas)**:
  - **Estandarización $Z$-score**: $Z = \frac{X - \mu}{\sigma}$ (media 0, desvío 1).
  - **Normalización Min-Max**: $X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$ (comprime al rango $[0, 1]$).
  - **Transformación Logarítmica**: $X' = \log(X + 1)$ (suaviza asimetría positiva a derecha).
  - **Cuantitativas a Ordinales (*Discretización*)**: Convertir edad continua en rangos categóricos ("Joven", "Adulto", "Adulto Mayor") mediante `pd.cut()` o `pd.qcut()`.
  - **Ordinales/Categóricas a Cuantitativas**: Asignar valores numéricos o codificar en dummies (`pd.get_dummies()`).
  - **String a Datetime**: Convertir cadenas de texto a objetos temporales (`pd.to_datetime()`) para habilitar el accesor `.dt`.
- **Transformaciones por Individuos (Filas)**:
  - Operaciones centradas en cada registro individual (ej: porcentajes por fila, centrados respecto a la media del sujeto).

