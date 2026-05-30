from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

study_hours = [1,2,3,4,5,6]
marks = [35,45,50,60,65,75]

X = np.array(study_hours).reshape(-1, 1)
y = np.array(marks)
model = LinearRegression()
model.fit(X, y)

print("Slope (Cofficient): ", model.coef_[0])
print("Intercept: ", model.intercept_)

predicted_marks = model.predict([[7]])
print("\n Predicted Marks for 7 hours:")
print(predicted_marks[0])

y_pred = model.predict(X)

mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("\n Mean Squared Error: ",mse)
print("R2 Score: ",r2)



#House Price Prediction
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

data = [
    [500,  1, 150000],
    [800,  2, 200000],
    [1000, 2, 250000],
    [1200, 3, 300000],
    [1500, 3, 350000],
    [1800, 4, 400000],
    [2000, 4, 450000],
    [2500, 5, 500000],
]

data = np.array(data)

X = data[:, :2]
y = data[:, 2]

print("Features: ",X)
print("Target: ",y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

new_house = np.array([[2000, 4]])
predicted_price = model.predict(new_house)

print("\n Predicted Price: ", predicted_price[0])

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("Rsquare Score: ",r2)
print("Mean Squared Error: ",mse)



#Linear Regression without sklearn using Gradient Descent
import numpy as np

# Data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([150, 200, 250, 300, 350,
              400, 450, 500, 550, 600])

# 1. Initialize parameters
m = 0
c = 0

learning_rate = 0.01
epochs = 1000

n = len(X)

# Gradient Descent
for epoch in range(epochs):

    # Predictions
    y_pred = m * X + c

    # Calculate MSE
    mse = (1/n) * np.sum((y - y_pred) ** 2)

    # Calculate gradients
    dm = (-2/n) * np.sum(X * (y - y_pred))
    dc = (-2/n) * np.sum(y - y_pred)

    # Update m and c
    m = m - learning_rate * dm
    c = c - learning_rate * dc

    # Print every 200 epochs
    if epoch % 200 == 0:
        print(f"Epoch {epoch}")
        print(f"m = {m:.4f}, c = {c:.4f}")
        print(f"MSE = {mse:.4f}")
        print("----------------------")

# Final equation
print("\nFinal Equation:")
print(f"y = {m:.2f}x + {c:.2f}")

# 4. Predictions
x1 = 11
x2 = 12

y1 = m * x1 + c
y2 = m * x2 + c

print(f"\nPrediction for x=11: {y1:.2f}")
print(f"Prediction for x=12: {y2:.2f}")