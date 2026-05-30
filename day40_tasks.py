from sklearn.model_selection import train_test_split
import numpy as np

X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
y = np.array([10,20,30,40,50,60,70,80])

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
print("Training set: ", X_train)
print("Testing set: ",X_test)



from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
y = np.array([10,20,30,40,50,60,70,80])

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
print(model.predict(X_test))