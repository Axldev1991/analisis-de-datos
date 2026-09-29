# Análisis de Datos — UTN

Repositorio oficial de la materia **Análisis de Datos** (Universidad Tecnológica Nacional).

---

## 📁 Estructura del Repositorio

```
.
├── README.md                                # Índice principal del repositorio
├── capitulos/                               # Transcripción íntegra de capítulos del libro
│   ├── capitulo_1.md                        # Capítulo 1: Introducción a la Minería de Datos
│   └── capitulo_2.md                        # Capítulo 2: Introducción al Análisis de Datos
├── temas/                                   # Guías y módulos temáticos de estudio
│   ├── conceptos_basicos.md                 # Sintaxis de Python, estructuras de datos y funciones
│   ├── numpy.md                             # Arrays ndarray, vectorización, broadcasting y álgebra lineal
│   ├── pandas.md                            # Series, DataFrames, loc/iloc, groupby, merge y .str/.dt
│   ├── data_cleaning.md                     # Limpieza de datos, imputación de nulos, outliers y escalado
│   ├── temas_capitulo_1.md                  # Síntesis temática del Capítulo 1 (Minería de Datos, IoT, etc.)
│   └── temas_capitulo_2.md                  # Síntesis temática del Capítulo 2 (Descriptiva, Covarianzas, etc.)
├── material_pdf/                            # Material bibliográfico y presentaciones en PDF
│   ├── libros/                              # Libros principales de la materia
│   ├── clases/                              # Diapositivas y apuntes de clases teóricas
│   └── ejercicios/                          # Guías de trabajos prácticos y ejercicios
├── recursos/                                # Enlaces a Google Colab e imágenes
│   ├── googleCollab.mc                      # Enlaces a cuadernos interactivos de Google Colab
│   └── imagenes/                            # Gráficos e ilustraciones extraídas de los capítulos
└── openspec/                                # Especificaciones del flujo SDD (Spec-Driven Development)
```

---

## 📘 Contenido de la Materia

### 1. Transcripción de Capítulos (`/capitulos`)
- **[Capítulo 1: Introducción a la Minería de Datos](capitulos/capitulo_1.md)**: Transcripción completa del primer capítulo.
- **[Capítulo 2: Introducción al Análisis de Datos](capitulos/capitulo_2.md)**: Transcripción completa del segundo capítulo.

### 2. Módulos y Síntesis Temáticas (`/temas`)
- **[Síntesis Temática — Capítulo 1](temas/temas_capitulo_1.md)**: Historia (Quetelet, Galton, Fisher), Big Data, Estadística vs. Data Mining, herramientas y terminología moderna (IoT, M2M, WoT, IoE).
- **[Síntesis Temática — Capítulo 2](temas/temas_capitulo_2.md)**: Clasificación de variables, tablas de frecuencias, medidas de tendencia central, dispersión, asimetría, curtosis, gráficos, matriz de covarianzas/correlación, transformaciones y estadística robusta.
- **[Conceptos Básicos de Python](temas/conceptos_basicos.md)**: Variables, tipos primitivos (`int`, `float`, `str`, `bool`), estructuras nativas (`list`, `tuple`, `dict`, `set`), control de flujo, *list comprehensions*, funciones `lambda`, `map`, `filter` y módulos.
- **[Guía Completa de NumPy](temas/numpy.md)**: Manejo de `ndarray`, creación de matrices, indexación y *slicing*, máscaras booleanas, operaciones vectorizadas, *Broadcasting*, agregaciones estadísticas por ejes (`axis=0`, `axis=1`) y álgebra lineal con `np.linalg`.
- **[Guía Completa de Pandas](temas/pandas.md)**: `Series` y `DataFrame`, lectura/escritura (CSV, Excel), selección con `.loc` e `.iloc`, filtrado booleano, transformaciones con `apply()`, patrones `groupby()`, uniones `concat`/`merge`, y accesores `.str` y `.dt`.
- **[Limpieza y Preprocesamiento de Datos (Data Cleaning)](temas/data_cleaning.md)**: Ciclo de vida del análisis, valores inconsistentes vs. atípicos (*outliers*), manejo de duplicados, patrones de no respuesta (MCAR, MAR, MNAR), técnicas de imputación, estandarización ($Z$-score, Min-Max, logarítmica, binning, one-hot encoding), y detección de outliers univariados y multivariados (Mahalanobis, MVE, MCD).

### 3. Enlaces Interactivos (`/recursos`)
- **[Google Colab Notebooks](recursos/googleCollab.mc)**: Enlaces directos a los cuadernos prácticos de la materia.

---

## 🛠️ Tecnologías y Herramientas

- **Lenguaje**: Python 3
- **Librerías principales**: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `scikit-learn`
- **Formato de Documentación**: Markdown con notación matemática KaTeX/LaTeX (`$...$` y `$$...$$`)
