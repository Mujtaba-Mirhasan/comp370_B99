import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("C:\\Users\\Kevin\\Documents\\McGill\\COMP_370\\comp370_B99\\data\\character_comparison.csv")

# Set the 'Topic' column as the index for easier plotting
df.set_index('Topic', inplace=True)

# Plot the DataFrame as a bar chart (each column is a group)
ax = df.plot.bar(rot=0, figsize=(10, 6), width=0.8)

# Customize the plot
plt.title('Topic Comparison Across Characters', fontsize=30)
plt.ylabel('Count', fontsize=30)
plt.xlabel('Topic', fontsize=30)
plt.legend(title='Character', fontsize=30, title_fontsize=30)
plt.tick_params(axis='both', which='major', labelsize=25)
plt.tight_layout() # Adjust layout to make room for labels


plt.show()