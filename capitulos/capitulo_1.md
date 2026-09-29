# Capítulo 1: Introducción a la Minería de Datos

> *En algún lugar, algo increíble está esperando por ser descubierto.*  
> — **Carl Sagan**

---

## 1.1 Orígenes

La minería de datos (*data mining* en inglés) surge con el análisis de los datos sociales de **Quetelet**, los datos biológicos de **Galton** y los datos agronómicos de **Fisher**.

### Adolphe Quetelet (1796-1874)
Hizo un gran aporte en el área de la **Física Social**. Entre sus notables conclusiones podemos mencionar:
- El delito es un fenómeno social que puede conocerse y determinarse estadísticamente.
- Los delitos se cometen año a año con absoluta regularidad y precisión.
- Posibles causas de la actividad delictiva pueden ser la pobreza, el clima, la miseria, el analfabetismo, entre otras.

### Francis Galton (1822-1911)
Fue el primero en aplicar métodos estadísticos en el estudio de las Ciencias Humanísticas, enfocándose en la herencia de la inteligencia. Algunos de sus resultados son:
- Creación del concepto estadístico de **correlación y regresión hacia la media**.
- Introducción del uso de cuestionarios y encuestas con el objetivo de obtener datos sobre las comunidades humanas.
- Desarrollo de estudios genealógicos, biográficos y antropométricos aplicando estadística.

### Ronald Fisher (1890-1962)
Trabajó desde 1919 como estadístico en la estación agrícola de Rothamsted Research, donde desarrolló el **análisis de la varianza (ANOVA)** aplicado a datos de cultivos. Realizó aportes fundamentales en la genética de poblaciones:
- El principio de Fisher.
- El modelo de selección sexual denominado *runaway*.
- La hipótesis del *hijo sexy*.

---

## 1.2 El Escenario Actual

Hasta hace pocos años, la única estrategia para extraer información de utilidad de una base de datos era la **Estadística clásica**. Sin embargo, los tamaños y la disponibilidad de las bases han crecido notablemente gracias a la tecnología informática. La minería de datos brinda una respuesta al análisis de gigantescas bases de datos con alta complejidad donde la Estadística clásica resulta un recurso limitado.

Se evidencia un aumento considerable en la cantidad de datos:
- Colectados
- Almacenados
- Accesibles
- Distribuidos

**Orígenes de estos datos:**
- Transacciones bancarias
- Reservas de aerolíneas
- Llamadas y mensajes por celulares
- Registros de atención de pacientes
- Datos obtenidos por sensores remotos
- Operaciones con tarjetas de crédito
- Búsquedas en internet
- Compras en supermercados

En esta disciplina confluyen técnicas provenientes de diferentes áreas como:
- Bases de datos y Computación
- Aprendizaje automático (*Machine Learning*)
- Visualización
- Inteligencia Artificial
- Estadística
- Redes neuronales
- Procesamiento de imágenes

---

## 1.3 Aspectos a Considerar en la Preparación de los Datos

Al analizarse una gran base de datos es importante considerar cuestiones de diversa índole, tales como:

1. **Almacenamiento** de cantidades ingentes de información.
2. **El análisis en "tiempo real"** del conjunto.
3. **Tecnología capaz de trabajar con diversidad de datos**.
4. Objetivos del análisis.
5. Disponibilidad de medios para resolver el problema.
6. Estructura y preparación de los datos.
7. Costos insumidos por el estudio.
8. Necesidad de interpretación de resultados.
9. Redacción de un informe comprensible que incluya los alcances de las conclusiones.

---

## 1.4 Dominios de Aplicación

Entre los diversos dominios de aplicación que han surgido en *data mining*, encontramos:
- Análisis y procesamiento de imágenes y señales
- Análisis multidimensional de procesos
- Análisis de datos textuales
- *Web mining*
- Detección de fraudes
- Bioinformática

---

## 1.5 Software Disponible

Entre la oferta de software especializado para *data mining* se destacan:

- **SAS Enterprise Miner**: Desarrollado por SAS Corporation. Permite crear modelos predictivos y descriptivos para grandes volúmenes de datos.
- **R**: Entorno y lenguaje de programación libre enfocado al análisis estadístico, reimplementación del lenguaje S con soporte para alcance estático.
- **Python**: Lenguaje de programación interpretado multiparadigma (orientado a objetos, imperativo, funcional) con sintaxis legible y fuerte ecosistema en ciencia de datos.
- **Statistica Data Miner**: Desarrollado por Dell, provee paquetes exhaustivos para manipulación y análisis de datos.
- **SPSS Clementine**: Aplicación de IBM para análisis de texto y minería de datos con interfaz visual.
- **T (Textual)**: Aplicado al análisis de datos simbólicos.
- **ISL Decision Systems**: Orientado a conversión de datos en decisiones de negocios (detección de fraude, fidelidad de clientes, predicción de audiencia).
- **Salford Systems**: Especializado en aprendizaje automático para modelos predictivos.
- **MineSet**: Desarrollado por Silicon Graphics para análisis y visualización de datos.
- **WEKA**: Software libre desarrollado en Java con colección de algoritmos de *machine learning*.
- **SODAS (Symbolic Official Data Analysis System)**: Software modular donde cada método estadístico se manipula como un ícono enlazado.
- **IBM Intelligent Miner**: Conjunto de productos para modelado, evaluación y visualización de minería inteligente.
- **SPAD (Système Portable pour l'Analyse de Données)**: Tratamiento exploratorio multivariado de grandes tablas de datos.

---

## 1.6 Estadística versus Data Mining

| Características | Análisis Estadístico | Data Mining |
| :--- | :--- | :--- |
| **Procedimiento** | Hipotético-deductivo | Inductivo |
| **Técnicas** | Confirmatorias | Exploratorias |
| **Supuestos** | Supuestos iniciales | Sin supuestos iniciales |
| **Herramientas y enfoque** | Herramientas informáticas opcionales | Difusión entre especialistas en Computación |

*Tabla 1.1: Comparación de características entre Estadística clásica y Data Mining.*

---

## 1.7 Nueva Terminología

### M2M (Machine to Machine)
Concepto genérico referido al intercambio de información o comunicación en formato de datos entre dos máquinas remotas. Facilita el control de fraudes, reducción de costos y monitoreo en tiempo real.  
*Aplicaciones:* Gestión de flotas, alarmas domésticas, contadores de agua/luz/gas, telemantenimiento de ascensores, estaciones meteorológicas, terminales punto de venta (POS), máquinas vending.

### IoT (Internet of Things)
Acuñado en 1999 por **Kevin Ashton** (MIT), refiere a la interconexión digital de objetos cotidianos mediante internet (sensores, RFID, Wi-Fi, *wearables* como relojes inteligentes, balanzas inalámbricas, etc.).  
*Dato histórico:* El primer dispositivo conectado a internet fue una máquina de Coca-Cola en la Universidad Carnegie Mellon a principios de los años 80.

### WoT (Web of Things)
Enfoques, estilos arquitectónicos y patrones de software que permiten que objetos del mundo real formen parte de la World Wide Web. Proporciona una capa de aplicación sobre IoT.

### IoE (Internet of Everything)
Filosofía que plantea la conexión inteligente entre **personas, dispositivos, datos en proceso y cosas** en una red global unificada.
