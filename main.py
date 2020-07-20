import csv
import simulatedanneling
import sys

try:
    cityList = []

    with open('msg_standorte_deutschland.csv', encoding='utf-8') as adressen:
        csv_reader_object = csv.DictReader(adressen, delimiter=',')
        for row in csv_reader_object:
            cityList.append(row)

    simulatedanneling.annealing(cityList, 100000, 0.00003)

except OSError as err:
    print("OS error: {0}".format(err))
