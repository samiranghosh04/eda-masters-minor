import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Read the data from the file and parse the dates
data = pd.read_csv('DailyDelhiClimateTest.csv', sep=',', parse_dates=['date'])

# Display the first few rows of the data
print(data.head())

# Choose specific columns for plotting
columns_to_plot = ['meantemp', 'humidity', 'wind_speed','meanpressure']

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
plt.tight_layout()

plt.show()





