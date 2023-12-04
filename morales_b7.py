import csv

def transpose_csv(input_file, output_file):

    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)

    transposed_data = list(map(list, zip(*data)))

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(transposed_data)

if __name__ == "__main__":

    input_file_path = 'Exam_Table.csv'
    output_file_path = 'b7_output7.csv'

    transpose_csv(input_file_path, output_file_path)

    print(f"Transposed data written to {output_file_path}")