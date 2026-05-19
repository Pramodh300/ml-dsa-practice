'''''''''#Find and Fix Missing Values
import pandas as pd
import numpy as np

data = {
    'Name':   ['Alice', 'Bob', None, 'David', 'Eve'],
    'Age':    [25, None, 30, 22, None],
    'Salary': [50000, 60000, None, 45000, 55000],
    'City':   ['Delhi', 'Mumbai', 'Chennai', None, 'Pune']
}

df = pd.DataFrame(data)

print("Missing values: ",df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['Name'] = df['Name'].fillna("Unknown")
df['City'] = df['City'].fillna('Unknown')

print(df)


#Full data cleaning
import pandas as pd
import numpy as np

data = {
    'Name':   ['Alice', 'bob', 'CHARLIE', 'Alice', None, 'Eve'],
    'Age':    [25, 30, 999, 25, 22, 28],
    'Salary': [50000, -1000, 55000, 50000, 45000, None],
    'Gender': ['Female', 'male', 'MALE', 'Female', 'female', 'Male']
}

df = pd.DataFrame(data)

print(df.shape)
print(df.isnull().sum())

df = df.drop_duplicates()

Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 -Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['Age']>= lower) & (df['Age']<= upper)]

df['Salary'] = df['Salary'].apply(lambda x : df['Salary'].median() if x < 0 else x)
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

df['Name'] = df['Name'].str.title()
df['Gender'] = df['Gender'].str.lower()

print(df)
'''

#Clean Data + Train Model
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt

data = {
    'Experience': [1, 2, None, 4, 5, 6, 999, 8, 9, 10],
    'Salary':     [25000, 30000, 35000, None, 45000,
                   50000, 55000, -9999, 65000, 70000]
}

df = pd.DataFrame(data)

print(df.isnull().sum())
print(df.shape)

df['Experience'] = df['Experience'].apply(lambda x: df['Experience'].median() if x < 0 else x)

Q1 = df['Experience'].quantile(0.25)
Q3 = df['Experience'].quantile(0.75)

IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['Experience']>= lower) & (df['Experience']<= upper)]

df['Salary'] = df['Salary'].replace(-9999, np.nan)
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

print(df)

X = df['Experience'].values.reshape(-1, 1)
y = df['Salary'].values

model = LinearRegression()

model.fit(X, y)
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

print("Coefficient: ", model.coef_[0])
print("Intercept: ", model.intercept_)
print("R2 Score: ", r2)
print("RMSE: ",rmse)

new_data = np.array([[11],[12]])
predicted_salary = model.predict(new_data)
print(f"Predicted Salary for 11 and 12 years of experience: {predicted_salary[0]: .2f}, {predicted_salary[1]: .2f}")

plt.scatter(X, y, color = 'blue', label = 'Actual Data')
plt.plot(X, y_pred, color = 'red', label = 'Best Fit Line')
plt.xlabel('Experience (Years)')
plt.ylabel("Salary")

plt.title("Experience vs Salary")

plt.legend()
plt.show()