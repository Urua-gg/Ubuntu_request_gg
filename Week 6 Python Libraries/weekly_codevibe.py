# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# 1. Create a NumPy array of numbers from 1 to 10 and calculate the mean
arr = np.arange(1, 11)
mean_value = np.mean(arr)
print("NumPy Array:", arr)
print("Mean:", mean_value)

# 2. Load a small dataset into a pandas DataFrame and display summary statistics
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Score': [88, 92, 79, 95, 85]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
print("\nSummary Statistics:\n", df.describe())

# 3. Fetch data from a public API using requests and print a key piece of information
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    data = response.json()
    print("\nCurrent Bitcoin Price (USD):", data['bpi']['USD']['rate'])
else:
    print("Failed to fetch data from API")

# 4. Plot a simple line graph using matplotlib
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]

plt.plot(numbers, squares)
plt.title("Line Graph of Numbers and Their Squares")
plt.xlabel("Number")
plt.ylabel("Square")
plt.show()
