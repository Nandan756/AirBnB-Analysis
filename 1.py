import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Load data
df = pd.read_csv("AB_NYC_2019.csv")
print(df.head())

# Basic stats
print(df.info())
print(df.describe())

# Drop unnecessary columns
df.drop(['id', 'name', 'host_name', 'last_review'], axis=1, inplace=True)

# Fill missing values
df['reviews_per_month'].fillna(0, inplace=True)

# Price distribution
plt.figure(figsize=(10, 5))
sns.histplot(df[df['price'] < 500]['price'], bins=50, kde=True)
plt.title("Price Distribution (Under $500)")
plt.xlabel("Price")
plt.show()

# Room type counts
plt.figure(figsize=(6, 4))
sns.countplot(x='room_type', data=df)
plt.title("Room Type Distribution")
plt.show()

# Listings per Borough
plt.figure(figsize=(8, 5))
sns.countplot(x='neighbourhood_group', data=df, order=df['neighbourhood_group'].value_counts().index)
plt.title("Listings by Borough")
plt.show()

# Average price per borough
plt.figure(figsize=(8, 5))
sns.barplot(x='neighbourhood_group', y='price', data=df[df['price'] < 500])
plt.title("Average Price by Borough")
plt.show()

# Availability
plt.figure(figsize=(10, 5))
sns.histplot(df['availability_365'], bins=30, kde=True)
plt.title("Availability Over the Year")
plt.xlabel("Days Available")
plt.show()

# Folium heatmap
map_nyc = folium.Map(location=[40.7128, -74.0060], zoom_start=11)
for idx, row in df[df['price'] < 500].sample(500).iterrows():
    folium.CircleMarker(
        [row["latitude"], row["longitude"]],
        radius=1,
        color='blue',
        fill=True,
        fill_opacity=0.5
    ).add_to(map_nyc)
map_nyc.save("nyc_airbnb_map.html")
