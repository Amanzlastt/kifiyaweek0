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

def box_plot(df,name):
  plt.figure(figsize=(15, 10))
  columns=["ModA", "ModB", "WS", "WSgust"]
  for i in range(4):
    plt.subplot(3,3,i+1)
    sns.boxplot(y=df[columns[i]])
    plt.title(f"Boxplot of {name}'s {columns[i]}")
  plt.show()

box_plot(df_benin, "Benini")
st.pyplot(plt)
box_plot(df_togo, "Togo")
st.pyplot(plt)
box_plot(df_sierra, "Sierraleon")
st.pyplot(plt)

st.write("This is bar plot of the three  datas to observe the data frequency")

df_benin['datetime']=pd.to_datetime(df_benin['Timestamp'])
df_togo['datetime']=pd.to_datetime(df_benin['Timestamp'])
df_sierra['datetime']=pd.to_datetime(df_benin['Timestamp'])

df_benin['month']= df_benin['datetime'].dt.month
monthly_avg_benin= df_benin[["GHI","DNI","DHI",'TModA','TModB']].groupby(df_benin['month']).mean()

df_togo['month']= df_togo['datetime'].dt.month
monthly_avg_togo= df_togo[["GHI","DNI","DHI",'TModA','TModB']].groupby(df_togo['month']).mean()

df_sierra['month']= df_sierra['datetime'].dt.month
monthly_avg_sierra= df_sierra[["GHI","DNI","DHI",'TModA','TModB']].groupby(df_sierra['month']).mean()

fig, ax= plt.subplots(3,1, figsize=(10, 15))

# Plotting for Benin
monthly_avg_sierra.plot(kind= 'bar', ax=ax[0])
ax[0].set_title('Monthly Average for Sierraleon')
ax[0].set_xlabel('Month')
ax[0].set_ylabel('Average Values')

# plotting for Togo
monthly_avg_togo.plot(kind= 'bar', ax=ax[1])
ax[1].set_title('Monthly Average for Togo')
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
st.pyplot(plt)
temperature_analysis(df_togo, "Togo")
st.pyplot(plt)
temperature_analysis(df_sierra, "Sierraleon")
st.pyplot(plt)
