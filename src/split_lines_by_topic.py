import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, '..', 'data', 'processed', 'all_lines_labelled.csv')
output_file = os.path.join(script_dir, '..', 'data', 'processed', 'all_lines_labelled_by_topic.csv')

df = pd.read_csv(input_file)
df = df.drop(columns=['character'])
df_sorted = df.sort_values(by='final_label')
df_sorted.to_csv(output_file, index=False)