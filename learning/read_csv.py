import csv

'''
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
'''

def read_temps_from_csv(path):
    temps = []

    try:
        with open(path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                temps.append(float(row["temp"]))
    except FileNotFoundError:
        print("Datei nicht gefunden:", path)
    except ValueError:
        print("Ungültiger Zahlenwert in CSV")

    return temps

'''
Was hier passiert
	•	path abstrahiert die Datenquelle
	•	Funktion gibt Daten, nicht Output zurück
	•	Wiederverwendbar für andere CSVs
    •	Fehler = erwarteter Zustand
	•	Programm stürzt nicht ab
	•	Kontrolle bleibt beim Entwickler
'''

def main():
    temps = read_temps_from_csv("learning/temps.csv")

    if not temps:
        print("Keine Daten vorhanden")
        return

    print("Max temp:", max(temps))


main()