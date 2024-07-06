from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import style

# Load and process gold data
path = Path(r"C:\Users\user\Desktop\le wagon\gold.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
close_price, dates = [], []
for row in reader:
    date = datetime.strptime(row[0], '%Y-%m-%d')
    if date.year >= 2000:
        dates.append(date)
        price = float(row[3])
        close_price.append(price)

# Load and process SPX data
path = Path(r"C:\Users\user\Desktop\le wagon\SPX.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
close_pricespx, datesspx = [], []
for row in reader:
    date = datetime.strptime(row[0], '%Y-%m-%d')
    if date.year >= 2000:
        datesspx.append(date)
        pricespx = float(row[3])
        close_pricespx.append(pricespx)

# Create a single figure with one subplot
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()

# Plot gold data
ax.plot(dates, close_price, color='red', label='Gold', linewidth=0.6)

# Plot SPX data
ax.plot(datesspx, close_pricespx, color='blue', label='S&P 500', linewidth=0.6)

# Set title and labels
ax.set_title("Comparison of Gold and S&P 500 prices (2000 onwards)", fontsize=14)
ax.set_xlabel("date", fontsize=14)
ax.set_ylabel("Closed price", fontsize=14)
ax.tick_params(labelsize=10)
ax.set_ylim(ymin=0)


# Add legend
ax.legend()

plt.show()