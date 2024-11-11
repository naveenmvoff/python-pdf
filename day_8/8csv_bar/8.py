#  Implement a program that reads a CSV file and generates a bar chart to represent the data using Matplotlib.

# require to install - pip install matplotlib pandas

import matplotlib.pyplot as plt  # use to create a visiuvalise table and chart 
import pandas as pd              # use to read the csv into data

data = pd.read_csv(r'C:\python-pdf\day_8\8csv_bar\data.csv')  #use to aload csv file into dataframe-the structure in pandas

catagories = data['Category']  # use to assign the csv value to the "catagories"
value = data['Value']          # use to assign the csv value to the "value"

plt.figure(figsize=(10, 6))    # use to create the chart bar frame
plt.bar(catagories, value, color='skyblue') # use to assign the value to the bar, and color

plt.title('The Bar chart of Category and value')   # title name
plt.xlabel('Category')                             # x axis name
plt.ylabel('Value')                                # Y axis name

plt.show()                                         # act like a print function to show the bar