# Proposal: Extraer y Consolidar Temas de Análisis de Datos con Python

## Intent

Extraer y consolidar la información teórica y práctica contenida en los libros y PDFs de la cátedra sobre los 4 ejes principales requeridos: **Conceptos Básicos**, **NumPy**, **Pandas** y **Data Cleaning**, estructurándolos en documentos Markdown exhaustivos y organizados.

## Scope

### In Scope
- **`conceptos_basicos.md`**: Sintaxis esencial de Python, tipos de datos, estructuras de control, funciones y entornos orientados al análisis de datos.
- **`numpy.md`**: Arrays multidimensionales (`ndarray`), vectorización, slicing/indexing, operaciones matemáticas/estadísticas y álgebra lineal.
- **`pandas.md`**: `Series` y `DataFrame`, indexación, filtrado, agregación, agrupamiento (`groupby`), combinación de datasets (`merge`/`join`).
- **`data_cleaning.md`**: Tratamiento de valores faltantes (`NaN`), duplicados, conversión de tipos de datos, filtrado de *outliers*, normalización y preparación de datos.
- Extracción a partir de `Python para el análisis de datos.pdf`, `AID 2022.pdf`, `NumPy.pdf`, `Pandas.pdf`, `Data cleaning (1).pdf` y los cuadernos Colab asociados en `googleCollab.mc`.

### Out of Scope
- Algoritmos avanzados de Machine Learning (supervisados/no supervisados) no contemplados en esta etapa del programa.
- Visualización de datos avanzada con Seaborn/Plotly (se tratará en un módulo posterior si corresponde).

## Capabilities

### New Capabilities
- `conceptos-basicos`: Fundamentos de Python aplicados al análisis de datos.
- `numpy-data-analysis`: Manejo eficiente de datos numéricos y matrices con NumPy.
- `pandas-data-analysis`: Estructuras de datos y manipulación tabular con Pandas.
- `data-cleaning-pipeline`: Técnicas y métodos de limpieza y preparación de datos.

### Modified Capabilities
None

## Approach

1. Inspeccionar y extraer el contenido relevante de cada uno de los archivos PDF (`NumPy.pdf`, `Pandas.pdf`, `Data cleaning (1).pdf`, `Clase 1.pdf`, `Python para el análisis de datos.pdf`) usando herramientas de línea de comandos (`pdftotext` / `python`).
2. Sintetizar y dar formato Markdown impecable a cada uno de los cuatro temas principales (`conceptos_basicos.md`, `numpy.md`, `pandas.md`, `data_cleaning.md`).
3. Incorporar ejemplos prácticos de código en Python/Pandas/NumPy e ilustrar con notación matemática (KaTeX) donde aplique.
4. Validar el contenido y commitear en el repositorio `Axldev1991/analisis-de-datos`.

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `conceptos_basicos.md` | New | Documentación de conceptos fundamentales de Python |
| `numpy.md` | New | Guía técnica y práctica de NumPy |
| `pandas.md` | New | Guía técnica y práctica de Pandas |
| `data_cleaning.md` | New | Guía completa de Data Cleaning y preprocesamiento |
| `openspec/changes/extract-python-data-analysis-topics/` | New | Especificaciones SDD de la tarea |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Pérdida de formato o código R/Python desordenado de los PDF | Medium | Utilizar scripts de parseo y revisión manual de código |
| Documentos demasiado extensos o fragmentados | Low | Mantener una estructura modular por tema con tabla de contenidos |

## Rollback Plan

Revertir los commits generados o eliminar los archivos `.md` correspondientes.

## Dependencies

- Archivos PDF de la cátedra presentes en el workspace.
- Enlaces de Google Colab especificados en `googleCollab.mc`.

## Success Criteria

- [ ] Generación de `conceptos_basicos.md` completo.
- [ ] Generación de `numpy.md` completo con ejemplos explicados.
- [ ] Generación de `pandas.md` completo con operaciones tabulares.
- [ ] Generación de `data_cleaning.md` con flujo de trabajo de saneamiento de datos.
- [ ] Subida a GitHub con mensajes de commit convencionales.
