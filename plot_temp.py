import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data/climate_data.csv")

# Convert date to datetime if needed
df["date"] = pd.to_datetime(df["date"])

# Create line plot
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["temperature_celsius"], marker="o")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Over Time")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig("temperature_plot.png")
plt.close()
