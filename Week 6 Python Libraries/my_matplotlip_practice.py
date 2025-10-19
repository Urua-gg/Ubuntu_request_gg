import matplotlib.pyplot as plt

# Data
countries = ['Kenya', 'USA', 'India', 'China', 'Brazil']
population = [55, 331, 1393, 1441, 213]  # in millions

# Create bar chart
plt.bar(countries, population)
plt.title("Population by Country")
plt.xlabel("Country")
plt.ylabel("Population (millions)")
plt.show()
