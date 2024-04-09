import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load COVID-19 data into a DataFrame
data = pd.read_csv('covid_data.csv')

# Display the first few rows of the DataFrame
print(data.head())

# Check data types and missing values
print(data.info())

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Basic statistics
print(data.describe())

# Total cases, deaths, and recoveries over time
total_cases = data.groupby('Date')['Confirmed'].sum()
total_deaths = data.groupby('Date')['Deaths'].sum()
total_recoveries = data.groupby('Date')['Recovered'].sum()

# Plotting
plt.figure(figsize=(15, 10))

# Total cases, deaths, and recoveries over time
plt.subplot(2, 2, 1)
plt.plot(total_cases, label='Total Cases', color='blue')
plt.plot(total_deaths, label='Total Deaths', color='red')
plt.plot(total_recoveries, label='Total Recoveries', color='green')
plt.title('COVID-19 Cases, Deaths, and Recoveries Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Daily new cases
plt.subplot(2, 2, 2)
data['New Cases'] = data['Confirmed'].diff()
plt.plot(data['Date'], data['New Cases'], color='purple')
plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.xticks(rotation=45)
plt.grid(True)

# Total cases, deaths, recoveries by continent
plt.subplot(2, 2, 3)
continent_data = data.groupby('Continent').agg({'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum'})
continent_data.plot(kind='bar', stacked=True)
plt.title('COVID-19 Cases, Deaths, and Recoveries by Continent')
plt.xlabel('Continent')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(True)

# Total cases by country
plt.subplot(2, 2, 4)
top_countries = data.groupby('Country').agg({'Confirmed': 'max'}).sort_values(by='Confirmed', ascending=False).head(10)
top_countries.plot(kind='bar')
plt.title('Top 10 Countries by Total COVID-19 Cases')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()

# Correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of COVID-19 Data')
plt.show()

# Monthly trends
data['Month'] = data['Date'].dt.month
monthly_data = data.groupby('Month').agg({'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum'})
monthly_data.plot(kind='bar', stacked=True)
plt.title('Monthly COVID-19 Trends')
plt.xlabel('Month')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()

# Fatality rate over time
data['Fatality Rate'] = (data['Deaths'] / data['Confirmed']) * 100
plt.plot(data['Date'], data['Fatality Rate'], color='orange')
plt.title('COVID-19 Fatality Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Fatality Rate (%)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Moving average of new cases
data['New Cases MA'] = data['New Cases'].rolling(window=7).mean()
plt.plot(data['Date'], data['New Cases MA'], color='brown')
plt.title('7-Day Moving Average of Daily New Cases')
plt.xlabel('Date')
plt.ylabel('New Cases (7-Day MA)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Growth rate of cases
data['Growth Rate'] = data['Confirmed'].pct_change() * 100
plt.plot(data['Date'], data['Growth Rate'], color='magenta')
plt.title('COVID-19 Growth Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Growth Rate (%)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Exponential growth phase detection
growth_phase_threshold = 5 # Example threshold for exponential growth phase
exponential_growth_phase = data[data['Growth Rate'] >= growth_phase_threshold]
plt.plot(data['Date'], data['Confirmed'], color='blue', label='Total Cases')
plt.scatter(exponential_growth_phase['Date'], exponential_growth_phase['Confirmed'], color='red', label='Exponential Growth Phase')
plt.title('Exponential Growth Phase Detection')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()
