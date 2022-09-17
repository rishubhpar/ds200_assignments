import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


load_data = pd.read_excel('data1.xls')
print("Loaded data shape: {}".format(load_data.shape))
print("Loaded data head: {}".format(load_data.head()))

columns = load_data.columns
# print("Columns for the data: {}".format(columns))

# Bar plot for the 'Mean Household Size1' from the dataset for all the states
x_axis = load_data['Indicators'][:5] # | Squashing the plot to display only few state results 
y_axis = load_data['Mean Household Size1'][:5]

plt.bar(x_axis, y_axis, align='center', width=0.3)
plt.xlabel('regions')
plt.ylabel('mean household income')
plt.savefig('bar_plot.png')
plt.clf()

# --------------------------------------------------------------------------- # 

# Box plot for the distribution of the mean household income, across states 
y_values = load_data['Mean Household Size1']

plt.boxplot(y_values)
plt.title('mean household income distribution over all states')
plt.ylabel('mean household income')
plt.savefig('box_plot.png')
plt.clf()

# --------------------------------------------------------------------------- # 

# Scatter plot for household population across various age groups <14, 14-44, 45-59, 60-69, 70-79, 80+
x_values = ['0-14 Years of Household population (%)',
            '15-44 Years of Household population (%)',
            '45-59 Years of Household population (%)',
            '60-69 Years of Household population (%)',
            '70-79 Years of Household population (%)',
            '80+ Years of Household population (%)']

y_values = load_data[load_data['Indicators'] == 'INDIA']
y_values = y_values[x_values].values[0]
print("y values shape: {}".format(y_values.shape))

x_values_lab = ['0-14', '15-44', '45-59', '60-69', '70-79', '80+']
print("y values: {}".format(y_values))

plt.plot(x_values_lab, y_values)
plt.ylabel('%% of household poplulation in India')
plt.title('Distribution of the population across various age groups in India')
plt.savefig('line.png')
