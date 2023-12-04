import pandas as pd

input_file = 'Exam_Table.csv'
output_file = 'b1_output1.csv'

df = pd.read_csv(input_file)

filtered_df = df[df['Interval'] == '30-0']

filtered_df.to_csv(output_file, index=False)

print(f"Filtered rows saved to {output_file}")
