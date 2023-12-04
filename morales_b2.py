import csv

def extract_rows_by_starting_letter(file_path, column, start_letter):
    extracted_rows = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get(column, '').startswith(start_letter):
                extracted_rows.append(row)
    return extracted_rows

file_path = 'Exam_Table.csv'
result = extract_rows_by_starting_letter(file_path, 'Genus', 'St')

for row in result:
    print(row)