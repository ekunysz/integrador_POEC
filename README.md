# Ejercicio Integrador: **Cálculo de \( \pi \) y Confiabilidad del Sistema**

Este ejercicio tiene como objetivo trabajar con un programa en Python que aproxima el valor de \( \pi \) utilizando el método de Montecarlo. El código contiene **errores intencionados** de estilo y diseño, los cuales deben ser identificados y corregidos. Además, se realizará un análisis de la confiabilidad del sistema basado en una tasa de fallas predefinida.

---

## Instrucciones

### 1. Análisis del Código
- Descargue el código proporcionado y ejecútelo para observar su comportamiento. 
- Identifique errores utilizando herramientas de análisis de código estático, como `pylint`. 
- Realice las correcciones necesarias para cumplir con los estándares de codificación de PEP8. 

### 2. Errores de Codificación
- Corrija errores relacionados con:
  - Uso de *magic numbers*. 
  - Nombres de variables y funciones poco descriptivos. 
  - Falta de comentarios y docstrings. 
  - Líneas de código excesivamente largas. 
- Documente los cambios realizados y justifique cada corrección aplicada.

### 3. Diagrama de Pareto
- Identifique las frecuencias de fallas. 
- Realice con ello el diagrama de Pareto

### 4. Optimización
- Identifique partes del código que puedan ser optimizadas, como bucles ineficientes o retrasos innecesarios. Utilizando `pofilers` 
- Mejore el rendimiento y explique las modificaciones realizadas.

### 5. Confiabilidad del Sistema
El sistema tiene una tasa de fallas \( \lambda = 0.0003 \) por línea de código. Dado que el programa tiene aproximadamente **60 líneas de código**, calcule la probabilidad de que el sistema funcione sin fallas durante un tiempo \( t \) utilizando la fórmula de confiabilidad: 

\[
R(t) = e^{-\lambda t}
\]

Donde: 
- \( R(t) \): Probabilidad de funcionamiento sin fallas durante \( t \) segundos. 
- \( \lambda \): Tasa de fallas por línea de código. 
- \( t \): Tiempo en segundos.

1. Realice el cálculo para \( t = 180 \) segundos (3 minutos). 
2. Interprete el resultado obtenido y evalúe la confiabilidad del sistema.


