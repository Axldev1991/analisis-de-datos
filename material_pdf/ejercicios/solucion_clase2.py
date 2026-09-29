"""
Solución completa para Ejercicios Clase 2
Base de microdatos EPH 3er Trimestre 2024 (INDEC)
"""
import pandas as pd
import os

# Determinar la ruta de los archivos de microdatos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOGAR_PATH = os.path.join(BASE_DIR, 'usu_hogar_T324.txt')
INDIVIDUAL_PATH = os.path.join(BASE_DIR, 'usu_individual_T324.txt')

print("="*60)
print("EJERCICIOS CLASE 2 - INTRODUCCIÓN AL ANÁLISIS DE DATOS")
print("="*60)

# 1. Abrir las bases con pandas
print("\n[1] Cargando bases de microdatos...")
df_hogar = pd.read_csv(HOGAR_PATH, sep=';', low_memory=False)
df_individual = pd.read_csv(INDIVIDUAL_PATH, sep=';', low_memory=False)
print("¡Bases cargadas con éxito!")

# 2. Analizar DataFrames y responder A, B, C
print("\n[2] Análisis de dimensiones y estructura:")

print("\n--- BASE HOGARES ---")
print(f"A. Número de columnas: {df_hogar.shape[1]}")
print(f"B. Número de filas: {df_hogar.shape[0]}")
print("C. Tipos de datos presentes:")
print(df_hogar.dtypes.value_counts())

print("\n--- BASE INDIVIDUAL ---")
print(f"A. Número de columnas: {df_individual.shape[1]}")
print(f"B. Número de filas: {df_individual.shape[0]}")
print("C. Tipos de datos presentes:")
print(df_individual.dtypes.value_counts())

# 3. Detectar columnas índice
print("\n[3] Verificación de columnas índice únicas:")

# Base Hogar: combinación de CODUSU (código de vivienda) y NRO_HOGAR
es_indice_hogar = not df_hogar.duplicated(subset=['CODUSU', 'NRO_HOGAR']).any()
print(f"• Base Hogares - ¿Es 'CODUSU + NRO_HOGAR' un índice único?: {es_indice_hogar}")

# Base Individual: combinación de CODUSU, NRO_HOGAR y COMPONENTE (número de persona)
es_indice_individual = not df_individual.duplicated(subset=['CODUSU', 'NRO_HOGAR', 'COMPONENTE']).any()
print(f"• Base Individual - ¿Es 'CODUSU + NRO_HOGAR + COMPONENTE' un índice único?: {es_indice_individual}")

print("\nConclusión Clase 2: Las llaves compuestas identifican de manera unívoca cada registro de hogar e individuo.")
