"""
Solución completa para Ejercicios Clase 3
Base de microdatos EPH 3er Trimestre 2024 (INDEC)
"""
import pandas as pd
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDIVIDUAL_PATH = os.path.join(BASE_DIR, 'usu_individual_T324.txt')

print("="*60)
print("EJERCICIOS CLASE 3 - LIMPIEZA Y TRATAMIENTO DE DATOS (EPH)")
print("="*60)

# Cargar DataFrame y hacer una copia desfragmentada
df_ind = pd.read_csv(INDIVIDUAL_PATH, sep=';', low_memory=False).copy()

# Normalizar edad: en EPH los menores de 1 año figuran con CH06 = -1
df_ind['CH06_CORREGIDA'] = np.maximum(df_ind['CH06'], 0)

# -------------------------------------------------------------
# 1. Analizar la columna P21 (Ingreso de la Ocupación Principal)
# -------------------------------------------------------------
print("\n[1] Análisis de la columna P21:")

no_respuesta = (df_ind['P21'] == -9).sum()
sin_ingreso_o_no_ocupado = (df_ind['P21'] == 0).sum()
ingreso_positivo = (df_ind['P21'] > 0).sum()
nulos_nativos = df_ind['P21'].isna().sum()

print(f"• Valores con -9 (No respuesta a ingreso): {no_respuesta:,}")
print(f"• Valores con 0 (Sin ingreso / No ocupado): {sin_ingreso_o_no_ocupado:,}")
print(f"• Valores con ingreso válido (> 0): {ingreso_positivo:,}")
print(f"• Valores nulos nativos (NaN): {nulos_nativos:,}")

print("\n--- Ponderadores Existentes ---")
print("• PONDERA: Ponderador poblacional general (expande la muestra a toda la población del país).")
print("• PONDIIO: Ponderador específico para ingresos de la ocupación principal (P21).")
print("  (Ajusta por no respuesta de ingresos dentro de la población ocupada).")

# Imputación de P21 utilizando la media de los ocupados con ingresos válidos (> 0)
ocupados_validos = df_ind[df_ind['P21'] > 0]
media_simple = ocupados_validos['P21'].mean()

# Media ponderada utilizando PONDIIO
media_ponderada = (ocupados_validos['P21'] * ocupados_validos['PONDIIO']).sum() / ocupados_validos['PONDIIO'].sum()

print(f"\nMedia simple de P21 (ocupados > 0): ${media_simple:,.2f}")
print(f"Media ponderada (PONDIIO) de P21 (ocupados > 0): ${media_ponderada:,.2f}")

# Imputación: Crear una columna P21_imputada reemplazando -9 por la media ponderada
df_ind['P21_imputada'] = df_ind['P21'].replace(-9, media_ponderada)
print(f" Imputación completada: {no_respuesta} registros de no respuesta imputados con ${media_ponderada:,.2f}")

# -------------------------------------------------------------
# 2. Evaluación de Valores Atípicos (Outliers) en P21
# -------------------------------------------------------------
print("\n[2] Evaluación de valores atípicos (outliers) en P21 (ingresos positivos):")

q1 = ocupados_validos['P21'].quantile(0.25)
q3 = ocupados_validos['P21'].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

outliers_iqr = ocupados_validos[(ocupados_validos['P21'] < limite_inferior) | (ocupados_validos['P21'] > limite_superior)]
percentil_99 = ocupados_validos['P21'].quantile(0.99)
outliers_p99 = ocupados_validos[ocupados_validos['P21'] > percentil_99]

print(f"• Q1: ${q1:,.2f} | Q3: ${q3:,.2f} | IQR: ${iqr:,.2f}")
print(f"• Límite superior IQR (Q3 + 1.5*IQR): ${limite_superior:,.2f}")
print(f"• Cantidad de outliers por método IQR: {len(outliers_iqr):,} ({len(outliers_iqr)/len(ocupados_validos):.1%})")
print(f"• Percentil 99: ${percentil_99:,.2f}")
print(f"• Cantidad de registros por encima del Percentil 99: {len(outliers_p99):,}")

print("\n--- Tratamiento Recomendado para Atípicos en Ingresos ---")
print("1. En distribuciones de ingreso con sesgo a la derecha (right-skewed), no se deben eliminar observaciones reales.")
print("2. Se recomienda winsorización/corte en percentiles (ej. p99) o la aplicación de transformaciones logarítmicas log(P21).")
print("3. Para análisis resumidos, priorizar la MEDIANA sobre la MEDIA ya que es una medida robusta frente a outliers.")

# -------------------------------------------------------------
# 3. Transformaciones sobre la Edad (CH06)
# -------------------------------------------------------------
print("\n[3] Transformaciones sobre la edad (CH06):")

# A. Agrupación por Décadas de Vida (usando la edad corregida >= 0)
df_ind['DECADA_VIDA'] = (df_ind['CH06_CORREGIDA'] // 10) * 10
print("\n• Conteo de personas por Década de Vida:")
print(df_ind['DECADA_VIDA'].value_counts().sort_index().to_string())

# B. Categorización por Grupos Etarios
bins = [-1, 14, 29, 64, 120]
labels = ['0-14 (Niños/Adolescentes)', '15-29 (Jóvenes)', '30-64 (Adultos)', '65+ (Adultos Mayores)']
df_ind['GRUPO_ETARIO'] = pd.cut(df_ind['CH06_CORREGIDA'], bins=bins, labels=labels)

print("\n• Distribución por Grupo Etario:")
print(df_ind['GRUPO_ETARIO'].value_counts().sort_index().to_string())

print("\nConclusión Clase 3: Se realizó el diagnóstico completo de P21, la imputación por media ponderada, la detección de outliers y las transformaciones etarias sin errores de bordes.")
