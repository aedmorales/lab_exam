import pandas as pd

input_file = 'Exam_Table.csv'
output_file = 'b2_output2.csv'

df = pd.read_csv(input_file)

filtered_df = df[df['Genus'].str.lower().str.startswith('st', na=False)]

filtered_df.to_csv(output_file, index=False)

print(f"Filtered rows saved to {output_file}")
