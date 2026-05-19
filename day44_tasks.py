import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
#Feature engineering basics
data = {
    'Name':     ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age':      [17, 25, 35, 45, 60],
    'Salary':   [20000, 50000, 70000, 90000, 120000],
    'Gender':   ['Female', 'Male', 'Male', 'Male', 'Female'],
    'City':     ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai'],
    'JoinDate': ['2023-01-15', '2020-06-20',
                 '2019-03-10', '2018-09-05', '2015-11-30']
}

df = pd.DataFrame(data)

df['Is_Senior'] = df['Age'].apply(lambda x: 1 if x >= 22 else 0)
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 25, 40, 60], labels=['Young', 'Middle', 'Senior'])

labelencoder = LabelEncoder()
df['Gender_encoded'] = labelencoder.fit_transform(df['Gender'])

print(df[['Gender', 'Gender_encoded']])

df_encoded = pd.get_dummies(df, columns=['City'], prefix='City')
print(df_encoded[['Name', 'City_Delhi', 'City_Mumbai', 'City_Chennai']])

df['JoinDate'] = pd.to_datetime(df['JoinDate'])
df['JoinYear'] =df['JoinDate'].dt.year
df['JoinMonth'] = df['JoinDate'].dt.month

print(df[['Name', 'Is_Senior', 'Age_Group', 'Gender_encoded', 'JoinYear', 'JoinMonth']])



#Feature Engineering + Train Model
data = {
    'Age':        [22, 35, 28, 45, 52, 31, 29, 41, 38, 26],
    'Gender':     ['Male', 'Female', 'Male', 'Female',
                   'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'City':       ['Delhi', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai',
                   'Chennai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi'],
    'Experience': [1, 8, 4, 15, 20, 7, 3, 12, 10, 2],
    'Salary':     [25000, 75000, 45000, 120000, 150000,
                   70000, 35000, 100000, 90000, 28000]
}

df = pd.DataFrame(data)

df['Salary_per_exp'] = df['Salary']/df['Experience']
df['Is_Senior'] = (df['Experience'] > 7).astype(int)
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 30, 40, 60], labels=['Young', 'Middle', 'Senior'])
le = LabelEncoder()
df['Gender_encoded'] = le.fit_transform(df['Gender'])
df = pd.get_dummies(df, columns=['City'], prefix='City', drop_first=True)
scale = StandardScaler()
df[['Age_scaled', 'Experience_scaled']] = scale.fit_transform(df[['Age', 'Experience']])
#Train Linear Regression Model
X = df[['Age_scaled', 'Experience_scaled', 'Gender_encoded', 'City_Mumbai', 'City_Delhi', 'Is_Senior']]
y = df['Salary']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
print("R2 Score: ", r2)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
print("RMSE: ", rmse)

coefficients = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_})
coefficients = coefficients.reindex(coefficients['Coefficient'].abs().sort_values(ascending=False).index)

print('\n Top 3 Important Features: ')
print(coefficients.head(3))