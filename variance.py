import csv
import statistics

def calculate_variance(csv_file, column_name):
    values = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                value = float(row[column_name])
                values.append(value)
            except ValueError:
                pass

    variance = statistics.variance(values)
    return variance
csv_file = 'C:/Users/cgmst/OneDrive/Desktop/CSV files/merged_reports.csv'  # Replace with your CSV file path
column_name = 'delivered'  # Replace with the name of the column you want to calculate the variance for
variance = calculate_variance(csv_file, column_name)
print(variance)

