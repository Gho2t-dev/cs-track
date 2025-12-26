"Beispielcode zum lesen der csv-Datei mit listen von dictionaries"

import csv

def read_records_from_csv(path: str) -> list[dict]:
    records = []
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append({
                    "time": row["time"],
                    "temp": float(row["temp"]),
                })
    except FileNotFoundError:
        print("Datei nicht gefunden:", path)
    except KeyError as e:
        print("Spalte fehlt in CSV:", e)
    except ValueError:
        print("Ungültiger Zahlenwert in CSV")
    return records

def calc_stats(temps: list[float]) -> dict:
    return {
        "min": min(temps),
        "avg": sum(temps) / len(temps),
        "max": max(temps),
        "count": len(temps),
        "range": max(temps) - min(temps)
    }

def main():
    records = read_records_from_csv("learning/temps.csv")
    if not records:
        print("Keine Daten vorhanden")
        return

    temps = [r["temp"] for r in records]   # List Comprehension = “baue Liste aus Daten”
    stats = calc_stats(temps)

    print("Min:", stats["min"])
    print("Avg:", stats["avg"])
    print("Max:", stats["max"])

if __name__ == "__main__":
    main()

'''     
Was du hier lernst (CS-Kern):
	•	Datenmodellierung (records statt nur Werte)
	•	Trennung: I/O (lesen) vs Logik (stats)
	•	List Comprehension (sehr wichtig in Python)
'''