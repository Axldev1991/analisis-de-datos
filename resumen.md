# Resumen de Análisis de Datos — Conceptos y Temas Clave

> **Materia**: Análisis de Datos (UTN)  
> **Cátedra**: Introducción al Análisis de Datos — Fernández, Luis Nahuel  
> **Acceso a Desarrollo Completo**: Ver archivo ampliado [`temas/resumen_desarrollado.md`](temas/resumen_desarrollado.md)

---

## 1. Conceptos Fundamentales

- **Tipos de datos**:
  - *Estructurados*: Tablas relacionales con esquema fijo ($n$ filas, $p$ columnas).
  - *Semi-estructurados*: JSON, XML, YAML con marcas o metadatos.
  - *No estructurados*: Texto libre, imágenes, audio, video y logs sin esquema predefinido.
- **Big Data y evolución desde 1970**: Crecimiento exponencial impulsado por la Web y la conectividad. Definido por las 5 V: Volumen, Velocidad, Variedad, Veracidad y Valor.
- **Procesamiento de datos vs. Minería de datos**:
  - *Procesamiento*: Gestión, formateo y ETL de datos.
  - *Data Mining*: Descubrimiento inductivo de conocimiento e inferencia de patrones (*KDD*).
- **Ronald Fisher**:
  - *ANOVA* (Análisis de varianza para comparar medias).
  - *Principio de Fisher* (proporción de sexos 1:1 evolutiva).
  - *Hipótesis del Hijo Sexy* (selección sexual evolutiva acelerada).
- **Cambio paradigmático post Segunda Guerra Mundial**: Transición del enfoque deductivo confirmatorio con muestras pequeñas al enfoque inductivo exploratorio masivo.
- **Proceso KDD (Knowledge Discovery in Databases)**:
  1. Selección $\rightarrow$ 2. Limpieza $\rightarrow$ 3. Transformación $\rightarrow$ 4. Data Mining $\rightarrow$ 5. Evaluación.
- **M2M (Machine to Machine)**: Comunicación automatizada entre dispositivos sin intervención humana (telemetría, POS, contadores inteligentes).
- **Evolución del análisis**: Univariado (1 variable) $\rightarrow$ Bivariado (2 variables, covarianza, correlación) $\rightarrow$ Multivariado ($p \ge 3$ variables, matrices $\hat{\Sigma}, R$, Mahalanobis).
- **Niveles de medición de variables**:
  - *Cualitativas/Categóricas*: Categorías nominales sin orden.
  - *Ordinales/Cuasicuantitativas*: Categorías con orden lógico pero sin distancia fija.
  - *Cuantitativas discretas*: Conteo numerable entero.
  - *Cuantitativas continuas*: Medición en escala continua infinita.
- **Reducción de dimensionalidad**:
  - Mitigación de la "maldición de la dimensionalidad".
  - *ACP (Análisis de Componentes Principales)*: Transformación lineal ortogonal hacia ejes de máxima varianza (autovectores/autovalores).
  - *Análisis de correspondencias*: Reducción factorial para tablas de contingencia cualitativas.
- **Análisis de Clusters (Clustering)**: Aprendizaje no supervisado para agrupar $n$ observaciones buscando máxima homogeneidad intra-grupo y máxima heterogeneidad inter-grupo (K-Means, Jerárquico).
- **Procesamiento Inductivo vs. Deductivo**:
  - *Deductivo*: De la hipótesis a la prueba.
  - *Inductivo*: De los datos a las reglas/patrones.
- **Text Mining**: Extracción de información desde lenguaje natural no estructurado (tokenización, TF-IDF, análisis de sentimientos).

---

## 2. NumPy

- **¿Qué es y para qué sirve?**: Librería fundamental de código abierto para computación científica y matricial en Python. Sirve para manipular arreglos multidimensionales (`ndarray`), ejecutar cómputo vectorial de alta velocidad en C, resolver álgebra lineal y estadística (`np.linalg`), y constituye la base de todo el ecosistema (Pandas, SciPy, Scikit-Learn).
- **IoT (Internet of Things)**: Flujos numéricos continuos de sensores que exigen procesamiento vectorial eficiente.
- **`ndarray`**: Arreglo multidimensional homogéneo en memoria contigua en C.
  - *Atributos principales*: `shape` (dimensiones), `dtype` (tipo único), `itemsize` (bytes por elemento), `strides` (pasos de memoria).
  - *Métodos*: `reshape()` (cambio de forma con vista), `flatten()` (aplanan a 1D con copia) y `ravel()` (aplanan a 1D con vista).
- **Vectorización e instrucciones SIMD**:
  - *SIMD (Single Instruction, Multiple Data)*: Nivel de hardware que ejecuta operaciones sobre vectores en 1 ciclo de reloj, evitando bucles `for` interpretados.
- **Ensamblaje y funciones de creación**: `zeros`, `ones`, `arange`, `linspace`, `vstack`, `hstack`, `concatenate`.
- **Pipelines**: Cadena de transformaciones numéricas vectorizadas contiguas.

---

## 3. Pandas

- **¿Qué es y para qué sirve?**: Librería estándar de código abierto y de alto nivel construida sobre NumPy para la manipulación, limpieza, preparación (*data wrangling*) y análisis de datos tabulares. Sirve para cargar datos multiformato (`read_csv`, `read_excel`), realizar uniones tipo SQL (`merge`), agrupamientos (`groupby`), filtrados complejos y preparar datasets para Machine Learning.
- **Enfoque de Análisis**: Orientada al manejo de estructuras tabulares heterogéneas de alto nivel con etiquetas explícitas en filas y columnas.
- **Estructuras Clave**:
  - `Series`: Vector 1D etiquetado.
  - `DataFrame`: Tabla 2D de columnas `Series` compartiendo índice.
- **Vectorización y Alineación**: Operaciones alineadas automáticamente por etiquetas de índice.
- **`loc` e `iloc`**:
  - `.loc[]`: Selección por **etiquetas/nombres** de filas y columnas.
  - `.iloc[]`: Selección por **posiciones numéricas enteras** (0-based).

---

## 4. Data Cleaning

- **Ciclo de vida de los datos (5 etapas)**:
  1. Recolección $\rightarrow$ 2. Almacenamiento $\rightarrow$ 3. Limpieza y Preprocesamiento $\rightarrow$ 4. Análisis $\rightarrow$ 5. Visualización/Modelado.
- **Sobre-representación y Duplicados**:
  - Registros clonados que sesgan estimaciones. Tratamiento: `drop_duplicates()`.
- **Valores perdidos / No respuesta**:
  - *MCAR (Missing Completely at Random)*: No soslayada / aleatoria pura. Eliminación con `dropna()`.
  - *MAR / MNAR*: Soslayable o sesgada. Imputación por mediana, media, KNN o modelos de reponderación.
- **Valores Inconsistentes vs. Atípicos (Outliers)**:
  - *Inconsistentes*: Sin coherencia lógica (ej. Edad = 250). Deben corregirse/eliminarse obligatoriamente.
  - *Outliers*: Valores reales lejanos que rompen la escala. Se deben inspeccionar antes de decidir si excluir.
- **Efecto de enmascaramiento (*Masking Effect*)**:
  - Ocurre cuando un grupo de outliers distorsiona la media y covarianza ocultando a otros outliers. Solución: Distancia de Mahalanobis con estimadores robustos MVE y MCD.
- **Transformación de datos (Chan, Badano y Rey, 2019)**:
  - *Objetivos*: Hacer comparables magnitudes, modificar escala de medición y satisfacer propiedades estadísticas (normalidad).
  - *Métodos por variables*: $Z$-score, Min-Max, logarítmica $\log(X+1)$, discretización (`cut`, `qcut`), dummies (`get_dummies`) y fechas (`to_datetime`).
  - *Métodos por individuo*: Centrado y porcentajes por fila.