from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle

data = {
    "size" : [600, 800, 1000, 1200, 1400, 1600, 1800, 2000],
    "bedrooms" : [2,2,3,3,4,4,5,5],
    "price" : [150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]
}
df = pd.DataFrame(data)

X = df[['size','bedrooms']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

with open('house_model.pkl', 'wb') as file:
    pickle.dump(model, file)
print("Model saved successfully.")
