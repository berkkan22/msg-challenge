import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from mpl_toolkits.basemap import Basemap

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

currenttext = fig.text(0.01, 0.95, "Current Distanz")
besttext = fig.text(0.01, 0.85, "Best Distanz")
currentDistanz = plt.figtext(0.01, 0.9, "")
bestDistanz = plt.figtext(0.01, 0.8, "")
lines = ax.plot(1, 1)

# class Close(object):
#     closeBool = False
#     def close(self, event):
#         return True

# callback = Close()
# abbruchBTN = plt.axes([0.81, 0.05, 0.1, 0.075])
# bprev = Button(abbruchBTN, 'Abbrechen')

def createBasemap():
    global m
    m = Basemap(projection='lcc', resolution='i',
                width=9E5, height=95E4,
                lat_0=51, lon_0=10)

    # TODO: Farben ändern
    # Zeichnet die Ländergrenzen ein
    m.drawcountries(linewidth=0.5, linestyle='solid', color='red',
                    antialiased=1, ax=None, zorder=None)
    # Zeichnet die Küstengrenzen ein
    m.drawcoastlines(linewidth=0.5, linestyle='solid', color='red',
                     antialiased=1, ax=None, zorder=None)
    # Färbt die Oceane Blau
    m.drawmapboundary(fill_color='blue')
    # Färbt die Seen aqua und das Land in grün ein
    m.fillcontinents(color='green', lake_color='aqua')

def path(array, distanz, best):

    # if(not callback.closeBool):
    global currentDistanz
    global bestDistanz

    ax.lines.pop(0)

    x_data = []
    y_data = []

    for i in array:
        x_data.append(float(i["Längengrad"]))
        y_data.append(float(i["Breitengrad"]))
    x_data.append(float(array[0]["Längengrad"]))
    y_data.append(float(array[0]["Breitengrad"]))

    x, y = m(x_data, y_data)

    lines.append(ax.plot(x, y, "o-", c="blue"))

    if(best):
        bestDistanz = plt.figtext(0.01, 0.8, str(distanz) + " km")
    else:
        currentDistanz = plt.figtext(0.01, 0.9, str(distanz) + " km")
    for txt in fig.texts:
        if(id(besttext) != id(txt) and id(currenttext) != id(txt) and id(currentDistanz) != id(txt) and id(bestDistanz) != id(txt)):
            txt.remove()

    
    # bprev.on_clicked(callback.close)

    plt.draw()
    plt.pause(0.00001)
# else:
#     plt.close()


def bestpath(array, distanz):
    global bestDistanz

    ax.lines.pop(0)

    for txt in fig.texts:
        if(id(besttext) != id(txt) and id(currenttext) != id(txt) and id(currentDistanz) != id(txt)):
            txt.set_visible(False)

    textvar1 = fig.text(0.01, 0.8, distanz)
    textvar1.remove()

    x_data = []
    y_data = []

    for i in array:
        x_data.append(float(i["Längengrad"]))
        y_data.append(float(i["Breitengrad"]))
    x_data.append(float(array[0]["Längengrad"]))
    y_data.append(float(array[0]["Breitengrad"]))

    x, y = m(x_data, y_data)

    lines.append(ax.plot(x, y, "o-", c="red"))

    bestDistanz = fig.text(0.01, 0.8, distanz)

    printCity(array)

    plt.draw()
    plt.pause(0.00001)


def printCity(array):
    y = 0.95
    for i in array:
        y -= 0.05
        fig.text(0.8, y, i["msg Standort"])
    