import pandas as pd

input_file = 'Exam_Table.csv'
output_file = 'b3_output3.csv'

df = pd.read_csv(input_file)

unique_scientific_names = df['Scientific Name'].unique()

unique_names_df = pd.DataFrame({'Scientific Name': unique_scientific_names})

unique_names_df.to_csv(output_file, index=False)

print(f"Unique scientific names saved to {output_file}")
