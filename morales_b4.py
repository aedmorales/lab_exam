import pandas as pd

input_file = 'Exam_Table.csv'
output_file = 'b4_output4.csv'

df = pd.read_csv(input_file)

grouped_df = df.groupby('Scientific Name')['Size Est (cm)'].mean().reset_index()

grouped_df.to_csv(output_file, index=False)

print(f"Unique scientific names with average size saved to {output_file}")