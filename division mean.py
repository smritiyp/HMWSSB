import csv
import statistics

def calculate_mean_by_division(csv_file):
    division_delivered = {}
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            division = row['division']  # Assuming the column name is 'division'
            delivered = row['delivered']  # Assuming the column name is 'delivered'
            try:
                delivered = float(delivered)
                if division not in division_delivered:
                    division_delivered[division] = []
                division_delivered[division].append(delivered)
            except ValueError:
                pass

    mean_by_division = {}
    for division, delivered_values in division_delivered.items():
        mean_by_division[division] = statistics.mean(delivered_values)

    return mean_by_division

# Example usage:
csv_file = 'C:/Users/cgmst/OneDrive/Desktop/CSV files/merged_reports.csv'  # Replace with your CSV file path
mean_by_division = calculate_mean_by_division(csv_file)
for division, mean_delivered in mean_by_division.items():
    print(f"Mean delivered for division '{division}': {mean_delivered}")

