import helperFunctions as calc
import random
import math
# import visualisierung

def annealing(currentArray, temp, cooldown):
    ''' Simulated Annealing Algoritmus

    Parameter
    ---------
    currentArray: array
        Ist das Array mit dem Dictionary wo die Deteils drinstehen.
    temp: int
        Ist die Temperatur des Systems.

        Je höher die Temperatur desto besser ist das Ergebniss, 
        aber desto länger dauert die Berechnung.
    cooldown: float
        Ist die cooldown Rate des Systems.

        Je kleiner die cooldown Rate desto besser ist das 
        Ergebniss, aber desto länger dauert die Berechnung.
    '''
    
    # visualisierung.createBasemap()


    currentDistanz = calc.berechneGesamtLaenge(currentArray)

    print("Start Entfernung:", currentDistanz, "km")

    bestSolution = currentArray[:]

    while(temp > 1):
        newSolution = currentArray[:]

        first = random.randint(1, len(currentArray)-1)
        second = random.randint(1, len(currentArray)-1)

        while(first == second):
            second = random.randint(1, len(currentArray)-1)

        newSolution[first], newSolution[second] = newSolution[second], newSolution[first]

        currentDistanz = calc.berechneGesamtLaenge(currentArray)
        newDistanz = calc.berechneGesamtLaenge(newSolution)

        if(newDistanz < currentDistanz):
            currentArray = newSolution[:]
            # visualisierung.path(currentArray, calc.berechneGesamtLaenge(currentArray), False)

        elif(math.exp((currentDistanz - newDistanz)/temp) < random.random()):
            currentArray = newSolution[:]
            # visualisierung.path(currentArray, calc.berechneGesamtLaenge(currentArray), False)

        if(calc.berechneGesamtLaenge(currentArray) < calc.berechneGesamtLaenge(bestSolution)):
            bestSolution = currentArray[:]
            # visualisierung.path(currentArray, calc.berechneGesamtLaenge(currentArray), True)
        
        temp *= 1-cooldown    

    # visualisierung.bestpath(currentArray, calc.berechneGesamtLaenge(currentArray))
    print("Kürzseste Entfernung:", calc.berechneGesamtLaenge(bestSolution), "km")

    calc.printCity(bestSolution)
