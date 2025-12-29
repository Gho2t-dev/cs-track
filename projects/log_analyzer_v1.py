import csv

def read_records(path: str) -> list[dict]:
    """
    Reads CSV with columns: time,temp
    Returns: list of {"time": str, "temp": float}
    """
    records: list[dict] = []

    # TODO: open file safely (with open)
    with open(path, newline='') as file:

    # TODO: use csv.DictReader
        reader = csv.DictReader(file)

    # TODO: append dicts with parsed float
        for row in reader:
            record = {
                "time": row["time"],
                "temp": float(row["temp"])
            }
            records.append(record)
    # TODO: handle errors:
    #   - FileNotFoundError -> print message, return []
    if FileNotFoundError:
        print(f"File not found: {path}")
        return []
    #   - KeyError (missing column) -> print message, return []
    if KeyError:
        print(f"Missing column in CSV file: {path}")
        return []
    #   - ValueError (bad number) -> print message, return []
    if ValueError:
        print(f"Invalid Value in CSV file: {path}")
        return []
    return records

def calc_stats(temps: list[float]) -> dict:
    """
    Returns dict with: count, min, avg, max, range
    """
    # TODO: if temps is empty -> return {}
    if not temps:
        return {}
    return {}

def main() -> None:
    path = "learning/temps.csv"

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