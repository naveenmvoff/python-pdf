# Write a function that reads a JSON file and extracts specific information from it.

# require to install - pip install matplotlib pandas

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file using pandas
data = pd.read_csv('your_file.csv')

# Assuming the CSV has columns 'Category' and 'Value' for the bar chart
categories = data['Category']  # Category column
values = data['Value']  # Value column

# Generate the bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart from CSV Data')

# Display the chart
plt.show()
