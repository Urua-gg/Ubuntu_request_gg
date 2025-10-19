import my_nump_practice as np

# Create an array with numbers from 10 to 50
arr = np.arange(10, 51)
print("Array:", arr)

# Find the maximum and minimum values
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))

# Multiply all elements by 3
arr_multiplied = arr * 3
print("Array multiplied by 3:", arr_multiplied)
# Calculate the mean and standard deviation
print("Mean value:", np.mean(arr))
print("Standard deviation:", np.std(arr))
