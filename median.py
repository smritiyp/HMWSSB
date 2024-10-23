import csv
import statistics

def calculate_median(csv_file, column_name):
    values = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                value = float(row[column_name])
                values.append(value)
            except ValueError:
                pass
    median = statistics.median(values)
    return median
csv_file = 'C:/Users/cgmst/OneDrive/Desktop/CSV files/merged_reports.csv'
column_name = 'delivered'  
median = calculate_median(csv_file, column_name)
print(median)
