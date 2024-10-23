import csv
def calculate_mode(csv_file, column_name):
    frequency_dict = {}
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                value = row[column_name]
                if value in frequency_dict:
                    frequency_dict[value] += 1
                else:
                    frequency_dict[value] = 1
            except ValueError:
                pass
    max_frequency = max(frequency_dict.values())
    mode_values = [value for value, frequency in frequency_dict.items() if frequency == max_frequency]
    if len(mode_values) == 1:
        return mode_values[0]
    else:
        return mode_values
csv_file = 'C:/Users/cgmst/OneDrive/Desktop/CSV files/merged_reports.csv'  
column_name = 'delivered' 
mode = calculate_mode(csv_file, column_name)
print(mode)
