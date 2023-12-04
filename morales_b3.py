import csv

def get_unique_scientific_names(file_path, column_name):
    unique_scientific_names = set()
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            scientific_name = row.get(column_name)
            if scientific_name:
                unique_scientific_names.add(scientific_name)
    return unique_scientific_names

file_path = 'Exam_Table.csv'
column_name = 'Scientific Name'
result = get_unique_scientific_names(file_path, column_name)

for name in result:
    print(name)