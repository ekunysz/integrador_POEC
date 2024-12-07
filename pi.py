import random
import time

def MonteCarloSimulation(pts): # esta función calcula el valor de pi
    InsideCircle = 0
    for i in range(pts):  # Generar puntos y verificar si están dentro del círculo
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            InsideCircle += 1
    piValue = (4 * InsideCircle) / pts
    return piValue

def GenerateRandomPoints():
    points = []
    for i in range(10000): # Generar magic numbers
        points.append((random.random(), random.random()))
    return points

def ProcessSimulation():
    print("Starting the simulation... Esto puede tomar algo de tiempo")
    time.sleep(3)  # Pausa innecesaria
    iterations = 1000000
    PiApproximation = MonteCarloSimulation(iterations)
    print(f"Pi approximated to {iterations} points: ", PiApproximation)

def ReliabilityCalculation(t):
    # Usar constante para calcular probabilidad de no falla en t segundos
    LineFailRate = 0.0003
    TotalLines = 60  # Estimación del tamaño del código en líneas
    FailureLambda = LineFailRate * TotalLines
    Reliability = 2.718281828459045 ** (-FailureLambda * t)
    return Reliability

# Correr la simulación principal
ProcessSimulation()

# Calcular confiabilidad después de 3 minutos de ejecución
reliabilityValue = ReliabilityCalculation(180)
print("Probabilidad de que el programa no falle durante 3 minutos:", reliabilityValue)

