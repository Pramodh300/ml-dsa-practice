import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
'''#Liner Regression
size = np.array([600, 800, 1000, 1200, 1400, 1600, 1800, 2000]).reshape(-1, 1)
price = np.array([150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000])

model = LinearRegression()
model.fit(size, price)

print("Coefficient: ", model.coef_[0])
print("Intercept: ", model.intercept_)

new_size = np.array([[2200]])
predicted_price = model.predict(new_size)
print("\n Predicted price for 2200 sqft: ", predicted_price[0])

y_pred = model.predict(size)
mse = mean_squared_error(price, y_pred)
r2 = r2_score(price, y_pred)

print("\n Mean Squared Error: ", mse)
print("R2 Score: ", r2)

plt.scatter(size, price, color='blue', label='Actual Data')
plt.plot(size, y_pred, color='red', label='Best Fit Line')

plt.xlabel('Size (sqft)')
plt.ylabel("Price")
plt.title('Linear Regression: Size vs Price')

plt.legend()
plt.show()
'''


#Sort + Regression Combined
def bubble_sort(hours, marks):
    n = len(hours)

    for i in range(n):
        for j in range(0, n-i-1):
            if hours[j] > hours[j+1]:
                hours[j], hours[j+1] = hours[j+1], hours[j]
                marks[j], marks[j+1] = marks[j+1], marks[j]

    return hours, marks
    
hours = [2, 4, 1, 6, 3, 8, 5, 7, 9, 10]
marks = [35, 55, 25, 75, 45, 90, 65, 80, 92, 98]

sorted_hours, sorted_marks = bubble_sort(hours, marks)
print("Sorted Hours: ", sorted_hours)
print("Sorted Marks: ", sorted_marks)

X = np.array(sorted_hours).reshape(-1, 1)
y = np.array(sorted_marks)

model = LinearRegression()
model.fit(X, y)

new_hours = np.array([[11], [12]])
predicted_marks = model.predict(new_hours)
print(f" Predicted Marks for 11 and 12 hours: {predicted_marks[0]: .0f}, {predicted_marks[1]: .0f}")

y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("R2 Score: ", r2)

residual = y - y_pred

plt.scatter(X, y, color = 'blue', label='Actual Data')
plt.plot(X, y_pred, color = 'red', label='Best Fit Line')
plt.plot(X, residual, color = 'green', label='Residuals')

plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Linear Regression: Study Hours vs Marks')

plt.legend()
plt.show()