import csv

def extract_rows_by_value(file_path, column, value):
    extracted_rows = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get(column) == value:
                extracted_rows.append(row)
    return extracted_rows

file_path = 'Exam_Table.csv'
result = extract_rows_by_value(file_path, 'Interval', '30-0')

for row in result:
    print(row)