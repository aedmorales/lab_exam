import csv
from collections import defaultdict

def calculate_average_count(file_path, target_scientific_name):
    sum_counts = 0
    entry_count = 0

    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            scientific_name = row["Scientific Name"]

            if scientific_name == target_scientific_name:
                count_str = row.get("Count", "0")  
                try:
                    count = int(count_str)
                    sum_counts += count
                    entry_count += 1
                except ValueError:
                    print(f"Warning: Could not convert '{count_str}' to int for Scientific Name '{target_scientific_name}'. Skipping this entry.")

    if entry_count > 0:
        average_count = sum_counts / entry_count
        return average_count
    else:
        return None

input_file_path = 'Exam_Table.csv'  
target_scientific_name = 'Pomacentrus adelus'

average_count = calculate_average_count(input_file_path, target_scientific_name)

if average_count is not None:
    print(f"The average count for {target_scientific_name} is: {average_count}")
else:
    print(f"No data found for {target_scientific_name}")