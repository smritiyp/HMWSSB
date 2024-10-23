import csv
import statistics

def calculate_mean_by_division_and_section(csv_file):
    division_delivered = {}
    section_delivered = {}
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            division = row['division']
            section = row['section']
            delivered = row['delivered']
            try:
                delivered = float(delivered)
            except ValueError:
                continue
            if division not in division_delivered:
                division_delivered[division] = []
            division_delivered[division].append(delivered)
            
            # Calculate mean by section
            if section not in section_delivered:
                section_delivered[section] = []
            section_delivered[section].append(delivered)

    mean_by_division = {division: statistics.mean(delivered_values) for division, delivered_values in division_delivered.items()}
    mean_by_section = {section: statistics.mean(delivered_values) for section, delivered_values in section_delivered.items()}

    return mean_by_division, mean_by_section

csv_file = 'C:/Users/cgmst/OneDrive/Desktop/CSV files/merged_reports.csv'  # Replace with your CSV file path
mean_by_division, mean_by_section = calculate_mean_by_division_and_section(csv_file)


print("\nSections where mean delivered exceeds mean delivered by division:")
for section, mean_delivered_section in mean_by_section.items():
    print(section)
    division = section.split("-")[0]  # Assuming section names are in the format division-section
    mean_delivered_division = mean_by_division.get(division, None)
    if mean_delivered_division is not None and mean_delivered_section > mean_delivered_division:
        print(f"Section '{section}' has mean delivered value ({mean_delivered_section}) greater than mean delivered by division ({mean_delivered_division})")
