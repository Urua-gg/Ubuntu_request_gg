import pandas as pd

# Create a DataFrame with 3 students
data = {
    'Name': ['Alice', 'Brian', 'Cathy'],
    'Age': [18, 19, 17],
    'Grade': [75, 45, 82]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Add a 'Passed' column where grade > 50 = True
df['Passed'] = df['Grade'] > 50
print("\nDataFrame with 'Passed' column:")
print(df)

# Filter and display only students who passed
passed_students = df[df['Passed'] == True]
print("\nStudents who passed:")
print(passed_students)
