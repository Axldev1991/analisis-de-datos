"""
Solución completa para Ejercicios Clase 4
Base de microdatos EPH 3er Trimestre 2024 (INDEC)
"""
import pandas as pd
import numpy as np
from scipy import stats
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDIVIDUAL_PATH = os.path.join(BASE_DIR, 'usu_individual_T324.txt')

print("="*60)
print("EJERCICIOS CLASE 4 - ANÁLISIS UNIVARIADO, MULTIVARIADO Y ESTADÍSTICA")
print("="*60)

# Cargar base individual y desfragmentar
df_ind = pd.read_csv(INDIVIDUAL_PATH, sep=';', low_memory=False).copy()

# Normalizar edad (CH06 = -1 indica menores de 1 año en EPH)
df_ind['CH06_CORREGIDA'] = np.maximum(df_ind['CH06'], 0)

# -------------------------------------------------------------
# 1. Análisis Univariado y Multivariado (P21, P47T, NIVEL_ED, PP3E_TOT)
# -------------------------------------------------------------
print("\n[1] Análisis de variables seleccionadas (P21, P47T, NIVEL_ED, PP3E_TOT):")

# Filtrar subconjunto con ingresos positivos para análisis de P21
ocupados_p21 = df_ind[df_ind['P21'] > 0].copy()

# a. Media de ingresos P21 según Nivel Educativo (NIVEL_ED) (Simple y Ponderada por PONDIIO)
print("\n--- a) Media de Ingresos P21 según Nivel Educativo ---")

def calc_weighted_mean_p21(g):
    return (g['P21'] * g['PONDIIO']).sum() / g['PONDIIO'].sum()

p21_simple_ned = ocupados_p21.groupby('NIVEL_ED')['P21'].mean()
p21_pond_ned = ocupados_p21.groupby('NIVEL_ED').apply(calc_weighted_mean_p21)

df_ned_res = pd.DataFrame({
    'Media Simple ($)': p21_simple_ned,
    'Media Ponderada ($)': p21_pond_ned
})

labels_ned = {
    1: '1- Primaria Incompleta',
    2: '2- Primaria Completa',
    3: '3- Secundaria Incompleta',
    4: '4- Secundaria Completa',
    5: '5- Superior/Univ. Incompleta',
    6: '6- Superior/Univ. Completa',
    7: '7- Sin instrucción / Ns.Nr.'
}
df_ned_res.index = df_ned_res.index.map(lambda x: labels_ned.get(x, str(x)))
print(df_ned_res.to_string())

# b. Media de P47T (Ingreso Total Individual) según la Década de Vida (ponderada por PONDERA)
print("\n--- b) Media de Ingreso Total Individual (P47T) según Década de Vida ---")
df_p47t_val = df_ind[df_ind['P47T'] > 0].copy()
df_p47t_val['DECADA_VIDA'] = (df_p47t_val['CH06_CORREGIDA'] // 10) * 10

def calc_weighted_mean_p47t(g):
    return (g['P47T'] * g['PONDERA']).sum() / g['PONDERA'].sum()

p47t_pond_decada = df_p47t_val.groupby('DECADA_VIDA').apply(calc_weighted_mean_p47t)
print(p47t_pond_decada.to_frame('Media Ponderada P47T ($)').to_string())

# c. Medidas de Tendencia Central para P21
print("\n--- c) Medidas de Tendencia Central para P21 (Ocupados con Ingreso > 0) ---")
media_p21_simple = ocupados_p21['P21'].mean()
media_p21_ponderada = (ocupados_p21['P21'] * ocupados_p21['PONDIIO']).sum() / ocupados_p21['PONDIIO'].sum()
mediana_p21 = ocupados_p21['P21'].median()
moda_p21 = ocupados_p21['P21'].mode()[0]

print(f"• Media Simple: ${media_p21_simple:,.2f}")
print(f"• Media Ponderada (PONDIIO): ${media_p21_ponderada:,.2f}")
print(f"• Mediana: ${mediana_p21:,.2f}")
print(f"• Moda: ${moda_p21:,.2f}")

# d. Medidas de Posición para P21
print("\n--- d) Medidas de Posición para P21 ---")
cuartiles = ocupados_p21['P21'].quantile([0.25, 0.50, 0.75])
print("• Cuartiles (Q1, Q2, Q3):")
for q, val in cuartiles.items():
    print(f"  - Q{int(q*4)} (p{int(q*100)}): ${val:,.2f}")

deciles = ocupados_p21['P21'].quantile(np.linspace(0.1, 0.9, 9))
print("\n• Deciles (D1 a D9):")
for d, val in deciles.items():
    print(f"  - Decil {int(round(d*10))}: ${val:,.2f}")

# -------------------------------------------------------------
# 2. Correlación de Pearson entre P21 y PP3E_TOT
# -------------------------------------------------------------
print("\n[2] Correlación de Pearson entre P21 e Ingreso / Horas Trabajadas (PP3E_TOT):")

# Filtrar ocupados con horas trabajadas válidas (> 0) e ingresos positivos (> 0)
df_corr = ocupados_p21[(ocupados_p21['PP3E_TOT'] > 0) & (ocupados_p21['PP3E_TOT'] < 168)].copy()
corr_pearson, p_val_corr = stats.pearsonr(df_corr['P21'], df_corr['PP3E_TOT'])

print(f"• Coeficiente de correlación de Pearson (r): {corr_pearson:.4f}")
print(f"• Valor p (p-value): {p_val_corr:.4e}")
print("• Interpretación: Existe una correlación positiva moderada-baja entre las horas semanales trabajadas y el ingreso percibido en la ocupación principal.")

# -------------------------------------------------------------
# 3. Investigar y aplicar V de Cramer y T de Student
# -------------------------------------------------------------
print("\n[3] Pruebas Estadísticas Avanzadas:")

# A. V de Cramer entre NIVEL_ED y ESTADO
print("\n--- A) V de Cramer (Nivel Educativo vs Estado Ocupacional) ---")
df_act = df_ind[df_ind['CH06_CORREGIDA'] >= 15].copy()
tabla_contingencia = pd.crosstab(df_act['NIVEL_ED'], df_act['ESTADO'])
chi2, p_val_chi2, dof, _ = stats.chi2_contingency(tabla_contingencia)
n_obs = tabla_contingencia.sum().sum()
r_rows, k_cols = tabla_contingencia.shape
v_cramer = np.sqrt(chi2 / (n_obs * min(r_rows - 1, k_cols - 1)))

print(f"• Chi-cuadrado (χ²): {chi2:,.2f} | Grados de libertad: {dof}")
print(f"• Valor p: {p_val_chi2:.4e}")
print(f"• V de Cramer: {v_cramer:.4f}")
print("• Interpretación: V de Cramer mide la fuerza de la asociación categórica entre el nivel educativo alcanzado y la condición de actividad/empleo.")

# B. T de Student para comparar P21 entre Varones (CH04=1) y Mujeres (CH04=2)
print("\n--- B) Prueba T de Student para Muestras Independientes (Brecha de Ingresos por Sexo) ---")
p21_varones = ocupados_p21[ocupados_p21['CH04'] == 1]['P21']
p21_mujeres = ocupados_p21[ocupados_p21['CH04'] == 2]['P21']

t_stat, p_val_ttest = stats.ttest_ind(p21_varones, p21_mujeres, equal_var=False)

print(f"• Media Varones: ${p21_varones.mean():,.2f} (n={len(p21_varones):,})")
print(f"• Media Mujeres: ${p21_mujeres.mean():,.2f} (n={len(p21_mujeres):,})")
print(f"• Estadística t de Welch: {t_stat:.4f}")
print(f"• Valor p: {p_val_ttest:.4e}")
if p_val_ttest < 0.05:
    print(" Conclusión: La diferencia de medias de ingreso entre varones y mujeres es estadísticamente significativa (p < 0.05).")

# -------------------------------------------------------------
# 4. Calcular la Tasa de Desocupación con ESTADO y PONDERA
# -------------------------------------------------------------
print("\n[4] Cálculo de la Tasa de Desocupación Ponderada:")

pea_df = df_ind[df_ind['ESTADO'].isin([1, 2])].copy()

ocupados_pond = pea_df[pea_df['ESTADO'] == 1]['PONDERA'].sum()
desocupados_pond = pea_df[pea_df['ESTADO'] == 2]['PONDERA'].sum()
pea_total_pond = ocupados_pond + desocupados_pond

tasa_desocupacion_pond = (desocupados_pond / pea_total_pond) * 100
tasa_desocupacion_raw = ((pea_df['ESTADO'] == 2).sum() / len(pea_df)) * 100

print(f"• Población Económicamente Activa (PEA) Muestral: {len(pea_df):,} personas")
print(f"• PEA Ponderada (Estimación Poblacional): {pea_total_pond:,.0f} personas")
print(f"• Ocupados Ponderados: {ocupados_pond:,.0f}")
print(f"• Desocupados Ponderados: {desocupados_pond:,.0f}")
print(f"\n Tasa de Desocupación Ponderada (EPH T3 2024): {tasa_desocupacion_pond:.2f}%")
print(f"  (Tasa Muestral sin ponderar: {tasa_desocupacion_raw:.2f}%)")

print("\nConclusión Clase 4: Se completaron todos los análisis estadísticos univariados, multivariados, pruebas de correlación, hipótesis y estimación de tasa de desocupación ponderada.")
