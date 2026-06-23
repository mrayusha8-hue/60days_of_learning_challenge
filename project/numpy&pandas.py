'''Create a 5×5 NumPy array filled with integers 1–25.
• Extract the 3rd row.
• Extract the last 2 columns.
• Get the element at row 2, column 4.
• Slice the inner 3×3 block (rows 1–3, cols 1–3).
• Check its dtype, shape, and ndim.
• Cast it to float32 and verify the dtype changed.
• Create a 3D array of shape (2, 3, 4) filled with zeros and check its dimensions.'''

'''import numpy as np
arr = np.arange(1,26).reshape(5,5)
print(arr)
print(f"The 3rd row: {arr[2]}")
print(f"The last 2 columns: {arr[-2:]}")
print(f"The element at row2, column4: {arr[1,4]}")
print(f"Sliced inner 3*3 block(row1-3, cols 1-3 : {arr[1:4, 1:4]}")
print(f"Its dtype:{arr.dtype}, shape:{arr.shape}, dimension:{arr.ndim}")
arr = arr.astype(float)
print(arr.dtype)
arr = np.zeros((2,3,4))
print(arr.ndim)'''

'''Create a Pandas Series of 5 student scores with custom index labels (student names).
• Access a score by name.
• Filter students who scored above 70.
• Change the dtype to float64'''

import pandas as pd
s = pd.Series([58,69,78,50,79] , index=['Alice','Bob','Cara','Dan','Eve'])
print(s)
print(f"A score of Bob is: {s['Bob']}")
print(f"Filtering students who scored above 70: {s[s>70]}")
s = s.astype(float)
print(s)
print(s.dtype)

'''
Create a DataFrame with columns: Name, Age, City, Salary for at least 6 people.
• Check its shape and dtypes.
• Select only the Name and Salary columns.
• Filter rows where Salary > 50000
• Show the first 3 rows with head().
• Show the last 2 rows with tail().
• Get full summary statistics with describe().
• Use info() to see column types and null counts'''
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice','Bob','Cara','Dan','Eve','Jim'],
    'Age': [21,22,20,25,23,24],
    'City': ['KTM', 'BKT', 'PTN', 'PKH','BRT', 'NPG'],
    'Salary': [25500,45000,18000,35000,59000,20000]
})
print(df)
print(f"its shape: {df.shape} ")
print(f"its dtypes: {df.dtypes}")
print(df[['Name', 'Salary']])
print(df[df['Salary'] > 50000])

print(df.head(3))
print(df.tail(2))
print(df.describe())
print(df.info())
'''
Save your DataFrame as a CSV with to_csv(), then read it back with read_csv().
• Check that the index column was handled (use index_col=0).
• Cast the Age column from int to float32.
• Cast the Salary column to int32.'''

df.to_csv("employee.csv", index=False)
df2 = pd.read_csv('employee.csv', index_col=0)
print(df2['Age'].astype('float32'))
print(df2['Salary'].astype('int32'))

