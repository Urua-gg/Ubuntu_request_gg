import matplotlib.pyplot as plt
# Example: showing frequency of values
ages = [22, 21, 20, 23, 24, 22, 20, 21, 22, 25, 23]

plt.hist(ages, bins=5, color='purple')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
 