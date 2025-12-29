import csv

def read_records(path: str) -> list[dict]:
    """
    Reads CSV with columns: time,temp
    Returns: list of {"time": str, "temp": float}
    """
    records: list[dict] = []
    # TODO FileNotFoundError, KeyError und ValueError handling
    try:
        with open(path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                record = {
                   "time": row["time"],
                   "temp": float(row["temp"])
                }
                records.append(record)
        return records
        print("File succesfully read")
    except FileNotFoundError:
        print(f"File in path: {path} not found.")
    except KeyError:
        print(f"Mapping key not found")
    except ValueError:
        print(f"Value Error for file in path: {path}")

def calc_stats(temps: list[float]) -> dict:
    
    # TODO: if temps is empty -> return {}
    if not temps:
        return {}
    return

def main() -> None:
    path = "/Users/fabian/Documents/cs-track/learning/temps.csv"

    records = read_records(path)
    if not records:
        print("No data.")
        return

    temps = [r["temp"] for r in records]

    stats = calc_stats(temps)
    if not stats:
        print("No stats.")
        return

    print("count:", stats["count"])
    print("min:", stats["min"])
    print("avg:", stats["avg"])
    print("max:", stats["max"])
    print("range:", stats["range"])

if __name__ == "__main__":
    main()