import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title("Solar Radiation Mesurement Data anlysis")
st.write("This is box plot of Benin's  data ['ModA', 'ModB', 'WS', 'WSgust']")

df_benin = pd.read_csv(r"C:\Users\Aman\Desktop\kifiyaweek0\data\benin-malanville.csv")
df_sierra = pd.read_csv(r"C:\Users\Aman\Desktop\kifiyaweek0\data\sierraleone-bumbuna.csv")
df_togo = pd.read_csv(r"C:\Users\Aman\Desktop\kifiyaweek0\data\togo-dapaong_qc.csv")

plt.figure(figsize=(15, 10))
for i, column in enumerate(["ModA", "ModB", "WS", "WSgust"]):
  plt.subplot(3,3,i+1)
  sns.boxplot(y=df_benin[column])
  plt.title(f"Boxplot of {column}")
st.pyplot(plt)

st.write("This is bar plot of the three  datas to observe the data frequency")

fig, ax= plt.subplots(3,1, figsize=(10, 15))




# Converting Timestamp to a date time data type
df_benin['datetime']=pd.to_datetime(df_benin['Timestamp'])
df_togo['datetime']=pd.to_datetime(df_benin['Timestamp'])
df_sierra['datetime']=pd.to_datetime(df_benin['Timestamp'])

df_benin['month']= df_benin['datetime'].dt.month
monthly_avg_benin= df_benin[["GHI","DNI","DHI",'TModA','TModB']].groupby(df_benin['month']).mean()

df_togo['month']= df_togo['datetime'].dt.month
monthly_avg_togo= df_togo[["GHI","DNI","DHI",'TModA','TModB']].groupby(df_togo['month']).mean()

df_sierra['month']= df_sierra['datetime'].dt.month
monthly_avg_sierra= df_sierra[["GHI","DNI","DHI",'TModA','TModB']].groupby(df_sierra['month']).mean()

# Plotting for Benin
monthly_avg_benin.plot(kind= 'bar', ax=ax[0])
ax[0].set_title('Monthly Average for Benin')
ax[0].set_xlabel('Month')
ax[0].set_ylabel('Average Values')

# plotting for Togo
monthly_avg_togo.plot(kind= 'bar', ax=ax[1])
ax[1].set_title('Monthly Average for Benin')
ax[1].set_xlabel('Month')
ax[1].set_ylabel('Average Values')

# potting for Sierra Leone
monthly_avg_benin.plot(kind= 'bar', ax=ax[2])
ax[2].set_title('Monthly Average for Benin')
ax[2].set_xlabel('Month')
ax[2].set_ylabel('Average Values')

plt.tight_layout() # Adjust layout to prevent overlapping
plt.show()
st.pyplot(plt)

st.write("This is shows the effect of cleaning  before and after cleaning has taken")
cleaned_benin = df_benin[df_benin['Cleaning'] == 1]
not_cleaned_benin = df_benin[df_benin["Cleaning"] == 0]

cleaned_togo = df_benin[df_togo['Cleaning'] == 1]
not_cleaned_togo = df_benin[df_togo["Cleaning"] == 0]

cleaned_sierra = df_benin[df_sierra['Cleaning'] == 1]
not_cleaned_sierra = df_benin[df_sierra["Cleaning"] == 0]

fig,ax =plt.subplots(6,1, figsize=(12, 15))
ax[0].plot(not_cleaned_benin['datetime'], not_cleaned_benin['ModA'], label='ModA Cleaned')
ax[0].plot(not_cleaned_benin['datetime'], not_cleaned_benin['ModB'], label='ModB Cleaned')
ax[0].set_title('Benin Sensor Redings Before Cleaning')

ax[1].plot(cleaned_benin['datetime'], cleaned_benin['ModA'], label='ModA Cleaned')
ax[1].plot(cleaned_benin['datetime'], cleaned_benin['ModB'], label='ModB Cleaned')
ax[1].set_title('Benin Sensor Redings After Cleaning')

ax[2].plot(not_cleaned_sierra['datetime'], not_cleaned_sierra['ModA'], label='ModA Cleaned')
ax[2].plot(not_cleaned_sierra['datetime'], not_cleaned_sierra['ModB'], label='ModB Cleaned')
ax[2].set_title('sierraleon Sensor Redings Before Cleaning')


ax[3].plot(cleaned_sierra['datetime'], cleaned_sierra['ModA'], label='ModA Cleaned')
ax[3].plot(cleaned_sierra['datetime'], cleaned_sierra['ModB'], label='ModB Cleaned')
ax[3].set_title('Sierra Sensor Redings After Cleaning')

ax[4].plot(not_cleaned_togo['datetime'], not_cleaned_togo['ModA'], label='ModA Cleaned')
ax[4].plot(not_cleaned_togo['datetime'], not_cleaned_togo['ModB'], label='ModB Cleaned')
ax[4].set_title('Togo Sensor Redings Before Cleaning')

ax[5].plot(cleaned_togo['datetime'], cleaned_togo['ModA'], label='ModA Cleaned')
ax[5].plot(cleaned_togo['datetime'], cleaned_togo['ModB'], label='ModB Cleaned')
ax[5].set_title('Togo Sensor Redings After Cleaning')
plt.legend()

st.pyplot(plt)
st.write("Wind speed and direction analysis")

wind_bins = np.arange(0,136,10)
wind_speed_bins = np.arange(0, df_benin['WS'].max() + 1, 1)

hist, xedges, yedges = np.histogram2d(df_benin['WD'], df_benin['WS'], bins=[wind_bins, wind_speed_bins])
hist= hist/hist.sum()

# Calculate average wind speed per direction bin
average_speed = hist.mean(axis=1)

# Create a radial bar plot
angles = np.linspace(0, 2 * np.pi, len(average_speed), endpoint=False).tolist()
average_speed = np.concatenate((average_speed, [average_speed[0]]))  # Close the loop
angles += angles[:1]

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.fill(angles, average_speed, color='blue', alpha=0.25)
ax.plot(angles, average_speed, color='blue', linewidth=2)
ax.set_xticks(np.linspace(0, 2 * np.pi, len(average_speed)-1, endpoint=False))  # Set direction labels
ax.set_xticklabels(['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'W', 'NW'])
ax.set_title('Radial Bar Plot of Average Wind Speed')
plt.show()

st.pyplot(plt)

st.write("Temperature analysis")

def temperature_analysis(df, name):
  plt.figure(figsize=(15,6))
  plt.scatter(data=df, x="RH", y='TModA', label='TModA', alpha=0.6)
  plt.scatter(data=df, x="RH", y='TModB', label='TModB', alpha=0.6)
  plt.xlabel('Relative Humidity vs. Temperature')
  plt.ylabel('Relative Humidity (%)')
  plt.ylabel("Temperature (°C)")
  plt.legend()

  plt.subplot(1,2,2)
  plt.scatter(data=df, x="RH", y='GHI', label='GHI', alpha=0.6)
  plt.scatter(data=df, x="RH", y='DNI', label='DNI', alpha=0.6)
  plt.scatter(data=df, x="RH", y='DHI', label='DHI', alpha=0.6)
  plt.title(f"{name}'s Relatice hiumidity vs. Solar Radiation")
  plt.xlabel('Relative Humidity (%)')
  plt.ylabel('Solar Radiation (w/m²)')
  plt.legend()

  plt.tight_layout()
  return plt.show()

temperature_analysis(df_benin,"Benin")
temperature_analysis(df_togo, "Togo")
temperature_analysis(df_sierra, "Sierraleon")


st.pyplot(plt)




st.write("Correlation analysis")

def correlation_plot(df,name, plot_no):
  correlation_matrix = df[["RH", "TModA", 'TModB', 'GHI', 'DNI', 'DHI' ]].corr()
  plt.subplot(3,1,plot_no, fig_size=(4,3))
  # plt.figure(figsize=(8,6))
  sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
  plt.title(f"{name}'sCorrelation Matrix of Relative Humidity, Temperature, and Solar Rasiation")
  plt.tight_layout()
  plt.show()

correlation_plot(df_benin, "Benin",1)
correlation_plot(df_togo, "Togo",2)
correlation_plot(df_sierra, "Sierraleon",3)

st.pyplot(plt)