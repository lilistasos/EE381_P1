import numpy as np
import matplotlib.pyplot as plt

fname = '/Users/tasos/Desktop/School/CSULB/Fall 2024/EE 381/1/Sales_01_20.csv'
data1 = np.loadtxt(fname, delimiter=',', skiprows=1)

years = data1[:, 0].astype(int)
sales = data1[:, 1:].astype(float)

sortFunc = np.argsort(years)
years = years[sortFunc]
sales = sales[sortFunc]

allYears = np.unique(years)

mean = []
standardDeviation = []
probabilities = []

for year in allYears:
    yearPrices = sales[years == year]
    mean.append(np.mean(yearPrices))

    standardDeviation.append(np.std(yearPrices, ddof=1))

    count = np.sum((yearPrices >= 200000) & (yearPrices <= 300000))
    probabilities.append(count / len(yearPrices))


print("Mean Prices by Year:")
for year, mean_price in zip(allYears, mean):
    print(f"{year}: {mean_price}")


print("\nStandard Deviations by Year:")
for year, std in zip(allYears, standardDeviation):
    print(f"{year}: {std}")


print("\nProbabilities by Year:")
for year, prob in zip(allYears, probabilities):
    print(f"{year}: {prob}")


fig, ax = plt.subplots(1, 3, figsize=(18, 5))

ax[0].bar(allYears, mean, color='mediumslateblue')
ax[0].set_title('Yearly Mean Sale Prices')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Mean')
ax[0].grid(axis='y')
ax[0].set_xticks(allYears)
ax[0].set_xticklabels(allYears, rotation=45)

ax[1].bar(allYears, standardDeviation, color='dodgerblue')
ax[1].set_title('Yearly Standard Deviations of Sale Prices')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Standard Deviation')
ax[1].grid(axis='y')
ax[1].set_xticks(allYears)
ax[1].set_xticklabels(allYears, rotation=45)

ax[2].bar(allYears, probabilities, color='limegreen')
ax[2].set_title('Yearly Probability of Sale Prices ($200k-$300k)')
ax[2].set_xlabel('Year')
ax[2].set_ylabel('Probability')
ax[2].grid(axis='y')
ax[2].set_xticks(allYears)
ax[2].set_xticklabels(allYears, rotation=45)

plt.tight_layout()
plt.savefig('Sales.png')
plt.show()
