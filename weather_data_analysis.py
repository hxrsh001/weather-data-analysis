import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-arya/main/temperature_data.json"
df = pd.read_json(url)
print(df)
print("\n")

print(df.head())
print(df.columns)
print(df.info())
print("\n")

# Drop row 3 -> day = wednesday
df.dropna(subset=['temperature_c'], inplace=True)

# Fill average value -> humidity = NAN
avg_humidity = df["humidity_pct"].mean()
df["humidity_pct"] = df["humidity_pct"].fillna(avg_humidity)


# New column -> farenheit | cell*1.8 _> +32
df['temperature_f'] = (df['temperature_c'] * 1.8) + 32
print(df)
print("\n")

# Subplots -> Plot | Pie-
fig, aux = plt.subplots(1, 2)

aux[0].plot(df["temperature_c"], df["day"])
aux[0].set_xlabel("Temperature")
aux[0].set_ylabel("Days")
aux[0].set_title("Temperature Per Days")
aux[0].grid(True)

aux[1].pie(df["humidity_pct"], labels=df["day"], autopct="%1.1f%%")
aux[1].set_title("Humidity as per Days")

plt.tight_layout()
plt.savefig("Temperature.png")
plt.show()