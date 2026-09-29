import pandas as pd

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