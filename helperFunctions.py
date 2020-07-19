import math

def berechneGesamtLaenge(array):
    ''' Berechnet die Gesamtlänge des Arrays von Start Punkt
        und wieder zurück

        Paramter
        --------
        array: array
            Ist das Array von dem die Gesamtlänge berechnet werden soll.
            Im Array ist jewals ein Dictionary enthalten mit den ganzen Daten
    '''

    gesamt = 0
    for i in range(len(array)):
        if(i + 1 < len(array)):
            gesamt += berechneEntferung(array[i], array[i+1])
        else:
            gesamt += berechneEntferung(array[i], array[0])
    return round(gesamt, 3)

def berechneEntferung(firstposition, secondposition):
    ''' Brechnet die Entfernung von einem Punkt zum anderen

        Paramter
        --------
        firstposition: array mit index
            Hält ein Array mit dem entsprechendem Index der Stadt
        secondposition: array mit index
            Hält ein Array mit dem entsprechendem Index der Stadt
        '''

    # TODO: Berechnung in km
    lat1 = float(firstposition["Breitengrad"])
    lat2 = float(secondposition["Breitengrad"])
    lon1 = float(firstposition["Längengrad"])
    lon2 = float(secondposition["Längengrad"])

    dist = 6378.388 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1))
    # dist = round(dist, 4)
    # x = abs(lat1 - lat2)
    # y = abs(lon1 - lon2)
    # print(dist)
    # return math.sqrt(x**2 + y**2)
    return dist

def printCity(array):
    ''' Gibt ein String der zu besuchenden Städts aus

    Pramater
    -------
    array: array
        Array mit den Städten
    '''
    visitingCity = ""
    for city in array:
        visitingCity += city["msg Standort"] + " -> "
    visitingCity += array[0]["msg Standort"]
    print(visitingCity)