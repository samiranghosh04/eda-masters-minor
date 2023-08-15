import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import mplcursors
import mpld3

# Read the data from the file and parse the dates
data = pd.read_csv('DailyDelhiClimateTrain.csv', sep=',', parse_dates=['date'])

#Describe the data
desc = data.describe()
print(desc)

# Display the data types
types = data.dtypes
print(types)
typeDate = data['date'].dtypes
print(typeDate)
typeTemp = data['meantemp'].dtypes
print(typeTemp)
typeHumidity = data['humidity'].dtypes
print(typeHumidity)
typeWindSpeed = data['wind_speed'].dtypes
print(typeWindSpeed)
typeMeanPressure = data['meanpressure'].dtypes
print(typeMeanPressure)



# Display the first few rows of the data
print(data.head())

# Choose specific columns for plotting
columns_to_plot = ['meantemp', 'humidity', 'wind_speed']
 
# Plot selected columns
fig, ax = plt.subplots()
data.plot(x='date', y=columns_to_plot, ax=ax)

# Customize date format
date_format = DateFormatter("%Y-%m-%d")  # Example: "2023-08-08"
ax.xaxis.set_major_formatter(date_format)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Daily Delhi Climate Data')
plt.legend(columns_to_plot)

# Make the chart interactive with data labels using mplcursors
mplcursors.cursor(hover=True)

# Convert the plot to an interactive web-based visualization using mpld3
interactive_plot = mpld3.fig_to_html(fig)

# Save the interactive plot to an HTML file
with open('interactive_plot.html', 'w') as f:
    f.write(interactive_plot)

# Display the plot using Matplotlib.
plt.tight_layout()

plt.show()


