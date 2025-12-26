import csv

temps = []  # Liste zur Speicherung der Temperaturen

with open("learning/temps.csv", newline="") as file:
    # open() öffnet die Datei
    # with garantiert: Datei wird sauber geschlossen
    # newline="" vermeidet CSV-Probleme auf verschiedenen OS

    reader = csv.DictReader(file)   
    # jedes Zeile als Dictionary lesen
    for row in reader:
        temps.append(float(row["temp"]))
    # Keys = Spaltennamen (time, temp)
    # float() → CSV ist Text, wir brauchen Zahlen

print(max(temps))  # Ausgabe der maximalen Temperatur