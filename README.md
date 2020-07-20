# mas-challange

## Vorraussetzung

Python 3.8

### Visualisierung
Matplotlib 3.2.1

Basemap 1.2.1

## Ausführung

Code z.B. als zip-Datei runterladen und entpacken.

Anschließend *main.py* ausführen.

Wenn sie die Visualisierung aktivieren möchten. Muss *matplotlib* und *basemap* installiert sein. Anschließend kommentieren sie die Zeilen in *simulatedannealing.py* aus.

##
```python
simulatedanneling.annealing(cityList, 100000, 0.00003)
```
Bei dieser Ausführung habe ich als beste Route 103712.728 km erhalten.
Dabei wurde folgende Route gewählt:

Ismaning/München (Hauptsitz) -> Passau -> Stuttgart -> Ingolstadt -> St. Georgen -> Hamburg -> Köln/Hürth -> Görlitz -> Münster -> Hannover -> Chemnitz -> Essen -> Lingen (Ems) -> Berlin -> Schortens/Wilhelmshaven -> Nürnberg -> Düsseldorf -> Braunschweig -> Frankfurt -> Bretten -> Walldorf -> Ismaning/München (Hauptsitz) (Wieder zurück)

Ich habe den Code auf *Windows 10* mit *python 3.8* geteste.



## Warum Simulated Annealing?
Dieses Verfahren erzeugt ein gutes Ergebnis in kurzer Zeit. Im Vergleich zum HillClimbing, welches bei einem Lokalen Maxima sein Ende erreicht hat. Simulated Annealing kann aus diesem Lokalen Maxima entkommen. Somit wird ein besseres Ergebnis erziehlt.

### Funktionsweise
Bei Simulated Annealing wir eine Temperatur und eine Cooldown Rate übergeben. Je höher die Temperatur und je kleiner die Cooldown Rate, desto besser ist das Ergebnis, aber desto länger dauert die Berechnung.
In diesem Beispiel ist als Temperatur 10000 und als Cooldown Rate 0.003 eine gute Option.
Nachdem die Parameter übergeben wurden wird zuerst ein Start Route erzeugt. Anschließend werden zwei Zufällige Städte genommen und vertauscht. Dann wird geguckt, ob die Gesamtstrecke , welche auch als Energie angegeben wird. Wenn die kleiner geworden ist wird sie akzeptiert und es wird weiter gemacht.
Falls die Stecke größer geworden ist wird
```mathe
e^((gesamtStrecke - NeueStecke) / Temperatur)
```
berechnet. Anschließend wird entschieden, ob die Stecke doch akzeptiert werden soll. Am Anfang wird viel mehr akzeptiert. Dies sorgt dafür das man nicht im Lokalen Maxima stecken bleibt.

```
C = Start Route
E(C)
Next = Neue Stecke
E(N)
if(E(N) < E(C))
   akzeptiere
elif(e^(...) < Zufällige Zahl)
   akzepiere
Temperatur = Temperatur * Cooldown
```
