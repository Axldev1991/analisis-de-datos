import pandas as pd
import numpy as np

# EJERCICIO 1-2

# 1. Abrir los archivos con Pandas
# Nota: Si ya los descomprimiste, coloca la ruta donde guardaste los .txt
df_hogar = pd.read_csv('usu_hogar_T324.txt', sep=';')
df_individual = pd.read_csv('usu_individual_T324.txt', sep=';')

# 2. Analizar los DataFrames y responder
print("=== BASE HOGARES ===")
print(f"A. Filas y Columnas (Shape): {df_hogar.shape}")
print(f"   - Numero de Columnas: {df_hogar.shape[1]}")
print(f"   - Nombres de Columnas: {df_hogar.columns}")
print(f"   - Numero de Filas: {df_hogar.shape[0]}")
print(f"   - Numero de Filas: {len(df_hogar)}")
print("\nC. Tipos de columnas:")
print(df_hogar.dtypes)

# Comprobar si la combinación CODUSU + NRO_HOGAR es única por fila
es_indice_hogar = not df_hogar.duplicated(subset=['CODUSU', 'NRO_HOGAR']).any()
print("¿Es índice único en hogares?:", es_indice_hogar)  # Devuelve True

print("\n" + "="*30 + "\n")

print("=== BASE INDIVIDUAL ===")
print(f"A. Filas y Columnas (Shape): {df_individual.shape}")
print(f"   - Nombres de Columnas: {df_individual.columns}")
print(f"   - Columnas: {df_individual.shape[1]}")
print(f"   - Filas: {df_individual.shape[0]}")
print("\nC. Tipos de columnas:")
print(df_individual.dtypes)

# Comprobar si la combinación de las 3 columnas es única por fila
es_indice_individual = not df_individual.duplicated(subset=['CODUSU', 'NRO_HOGAR', 'COMPONENTE']).any()
print("¿Es índice único en personas?:", es_indice_individual)  # Devuelve True


# EJERCICIO 3-4
print("EJERCICIO 3-4")
no_respuesta = (df_individual['P21'] == -9).sum()
sin_ingreso = (df_individual['P21'] == 0).sum()
nulos = df_individual['P21'].isna().sum()

print(f"Valores con -9 (No respuesta): {no_respuesta}")
print(f"Valores con 0 (Sin ingreso u ocupación): {sin_ingreso}")
print(f"Valores nulos (NaN): {nulos}")


# ==============================================================================
# 0. CARGA DE DATOS Y LIMPIEZA INICIAL
# ==============================================================================

# Cargar la base individual de la EPH (3er Trimestre 2024)
df = pd.read_csv('usu_individual_T324.txt', sep=';')

# En la EPH, el valor -9 representa "no respuesta" o dato ignorado.
# Reemplazamos los -9 por NaN para evitar sesgar los cálculos estadísticos.
cols_a_limpiar = ['P21', 'P47T', 'PP3E_TOT']
for col in cols_a_limpiar:
    df[col] = df[col].replace(-9, np.nan)


# ==============================================================================
# PUNTO 1: ANÁLISIS UNIVARIADO Y MULTIVARIADO
# ==============================================================================

# ------------------------------------------------------------------------------
# a- Media de ingresos de la ocupación principal (P21) según nivel educativo (NIVEL_ED).
# Usamos el ponderador específico de ingresos ocupacionales: PONDIIO.
# ------------------------------------------------------------------------------
# Filtramos solo casos con ingreso positivo (>0) y nivel educativo no nulo
df_p21 = df[(df['P21'] > 0) & (df['NIVEL_ED'].notna())].copy()

# Media ponderada = Suma(P21 * PONDIIO) / Suma(PONDIIO) por cada grupo educativo
media_p21_por_nivel = df_p21.groupby('NIVEL_ED').apply(
    lambda x: np.average(x['P21'], weights=x['PONDIIO'])
)

print("=== 1a. Media de P21 según Nivel Educativo ===")
print(media_p21_por_nivel)
print("-" * 50)


# ------------------------------------------------------------------------------
# b- Media del Ingreso Total Individual (P47T) según década de vida del respondent.
# Usamos la edad (CH06) para armar la década y el ponderador PONDII.
# ------------------------------------------------------------------------------
# Calculamos la década mediante división entera (ej: 25 // 10 * 10 = 20)
df['decada_vida'] = (df['CH06'] // 10) * 10

# Filtramos solo personas con P47T mayor a 0
df_p47 = df[df['P47T'] > 0].copy()

# Media ponderada de P47T usando PONDII
media_p47_por_decada = df_p47.groupby('decada_vida').apply(
    lambda x: np.average(x['P47T'], weights=x['PONDII'])
)

print("\n=== 1b. Media de P47T según Década de Vida ===")
print(media_p47_por_decada)
print("-" * 50)


# ------------------------------------------------------------------------------
# c- Medidas de tendencia central para P21 (Media, Mediana y Moda)
# ------------------------------------------------------------------------------
media_p21 = np.average(df_p21['P21'], weights=df_p21['PONDIIO'])  # Ponderada
mediana_p21 = df_p21['P21'].median()                               # Mediana
moda_p21 = df_p21['P21'].mode()[0]                                 # Moda

print("\n=== 1c. Medidas de Tendencia Central para P21 ===")
print(f"Media ponderada: ${media_p21:.2f}")
print(f"Mediana:         ${mediana_p21:.2f}")
print(f"Moda:            ${moda_p21:.2f}")
print("-" * 50)


# ------------------------------------------------------------------------------
# d- Medidas de posición para P21 (Cuartiles Q1, Q2, Q3 y Percentil 90)
# ------------------------------------------------------------------------------
q1 = df_p21['P21'].quantile(0.25)
q2 = df_p21['P21'].quantile(0.50)  # Equivale a la mediana
q3 = df_p21['P21'].quantile(0.75)
p90 = df_p21['P21'].quantile(0.90)

print("\n=== 1d. Medidas de Posición para P21 ===")
print(f"Q1 (Percentil 25): ${q1:.2f}")
print(f"Q2 (Percentil 50): ${q2:.2f}")
print(f"Q3 (Percentil 75): ${q3:.2f}")
print(f"Percentil 90:      ${p90:.2f}")
print("-" * 50)


# ==============================================================================
# PUNTO 2: CORRELACIÓN DE PEARSON PARA P21 Y PP3E_TOT
# Mide la relación lineal entre ingreso principal y horas trabajadas.
# ==============================================================================
# Filtramos registros con valores positivos en ambas variables
df_corr = df[(df['P21'] > 0) & (df['PP3E_TOT'] > 0)].dropna(subset=['P21', 'PP3E_TOT'])

# Calculamos el coeficiente r de Pearson directamente con Pandas
coef_pearson = df_corr['P21'].corr(df_corr['PP3E_TOT'], method='pearson')

print("\n=== 2. Correlación de Pearson ===")
print(f"Coeficiente r (P21 vs PP3E_TOT): {coef_pearson:.4f}")
print("-" * 50)


# ==============================================================================
# PUNTO 3: V DE CRAMÉR Y T DE STUDENT (SIN SCI PY)
# ==============================================================================

# --- A. V de Cramér ---
# Mide la relación entre dos variables cualitativas (NIVEL_ED y CH07: Estado civil).
# Creamos la tabla de contingencia de frecuencias observadas
tabla_obs = pd.crosstab(df['NIVEL_ED'], df['CH07'])

# Calculamos las frecuencias esperadas mediante producto matricial
total = tabla_obs.values.sum()
filas = tabla_obs.values.sum(axis=1, keepdims=True)
cols = tabla_obs.values.sum(axis=0, keepdims=True)
esperados = (filas @ cols) / total

# Cálculo del estadístico Chi-cuadrado y fórmula de V de Cramér
chi2 = np.sum((tabla_obs.values - esperados) ** 2 / esperados)
r, k = tabla_obs.shape
v_cramer = np.sqrt((chi2 / total) / min(k - 1, r - 1))

print("\n=== 3a. V de Cramér ===")
print(f"V de Cramér (Nivel Educativo vs Estado Civil): {v_cramer:.4f}")


# --- B. T de Student ---
# Compara el promedio de horas trabajadas (PP3E_TOT) entre Hombres (CH04=1) y Mujeres (CH04=2).
hombres = df[(df['CH04'] == 1) & (df['PP3E_TOT'] > 0)]['PP3E_TOT'].dropna()
mujeres = df[(df['CH04'] == 2) & (df['PP3E_TOT'] > 0)]['PP3E_TOT'].dropna()

# Medias, varianzas y tamaños muestrales
m1, m2 = hombres.mean(), mujeres.mean()
v1, v2 = hombres.var(ddof=1), mujeres.var(ddof=1)
n1, n2 = len(hombres), len(mujeres)

# Fórmula del estadístico t de Welch / Student
t_stat = (m1 - m2) / np.sqrt((v1 / n1) + (v2 / n2))

print("\n=== 3b. T de Student ===")
print(f"Estadístico t (Horas trabajadas Hombres vs Mujeres): {t_stat:.4f}")
print("-" * 50)


# ==============================================================================
# PUNTO 4: TASA DE DESOCUPACIÓN USANDO LA VARIABLE ESTADO
# En ESTADO: 1 = Ocupado, 2 = Desocupado, 3 = Inactivo.
# PEA (Población Económicamente Activa) = Ocupados + Desocupados (ESTADO 1 o 2).
# Se utiliza el ponderador general poblacional: PONDERA.
# ==============================================================================
# Filtramos solo la PEA
df_pea = df[df['ESTADO'].isin([1, 2])].copy()

# Sumatoria de ponderadores para desocupados y para toda la PEA
desocupados_pond = df_pea[df_pea['ESTADO'] == 2]['PONDERA'].sum()
pea_pond = df_pea['PONDERA'].sum()

# Tasa de desocupación oficial
tasa_desocupacion = (desocupados_pond / pea_pond) * 100

print("\n=== 4. Tasa de Desocupación ===")
print(f"Tasa de Desocupación estimada: {tasa_desocupacion:.2f}%")