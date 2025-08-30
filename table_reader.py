# table_reader.py

import csv

def read_data(filename="data.csv"):
    """Read CSV file into a list of dicts."""
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def sort_data(data, column):
    """Sort data by chosen column."""
    if column == "score":
        # sort numerically
        return sorted(data, key=lambda x: int(x["score"]), reverse=True)
    elif column == "name":
        # sort alphabetically
        return sorted(data, key=lambda x: x["name"].lower())
    else:
        print("Invalid column. Choose 'name' or 'score'.")
        return data

def main():
    data = read_data()
    print("Data loaded from CSV:")
    print(data)

    column = input("Sort by 'name' or 'score': ").strip().lower()
    sorted_data = sort_data(data, column)

    print("\nTop 5 results:")
    for row in sorted_data[:5]:
        print(f"{row['name']}, {row['score']}")

if __name__ == "__main__":
    main()
