import csv

def add_hrid_column(input_file_path, output_file_path):
    with open(input_file_path, 'r', newline='') as infile, \
            open(output_file_path, 'w', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['HRID']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            location = row.get("location", "")
            site = row.get("site", "")
            replicate = row.get("replicate", "")

           
            hrid = '-'.join([location, site, replicate]).replace(',', '-')

            row["HRID"] = hrid

            writer.writerow(row)

input_file_path = 'Exam_Table.csv' 
output_file_path = 'b6_output6.csv'

add_hrid_column(input_file_path, output_file_path)

print(f"New file with HRID column created: {output_file_path}")