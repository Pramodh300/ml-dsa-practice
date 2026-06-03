import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

'''#Tune KNN Manually
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8],
    'Attendance': [50,55,60,65,70,75,80,90],
    'Pass': [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)
X = df[['Study_Hours', 'Attendance']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

for k in [1,3,5,6]:
    print(f"\nK = {k}")

    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")
    



#Decision Tree Hyperparameter Tuning
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8],
    'Attendance': [50,55,60,65,70,75,80,90],
    'Pass': [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)
X = df[['Study_Hours', 'Attendance']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

for depth in [2,3,5,10]:
    model = DecisionTreeClassifier(
        max_depth = depth,
        random_state = 42
    )

    model.fit(X_train, y_train)
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    acc_train = accuracy_score(y_train, train_pred)
    acc_test = accuracy_score(y_test, test_pred)

    print(f"\nMax Depth: {depth}")
    print(f"Train Accuracy: {acc_train:.2f}")
    print(f"Test Accuracy: {acc_test:.2f}")



#Random Forest Tuning
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8],
    'Attendance': [50,55,60,65,70,75,80,90],
    'Pass': [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)
X = df[['Study_Hours', 'Attendance']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

for n in [10,50,100,200]:
    model = RandomForestClassifier(
        n_estimators = n,
        random_state = 42
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"\nNumber of Trees: {n}")
    print(f"Accuracy: {accuracy:.2f}")



#Logistic Regression Tuning
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8],
    'Attendance': [50,55,60,65,70,75,80,90],
    'Pass': [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)
X = df[['Study_Hours', 'Attendance']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

for c in [0.01, 0.1, 1, 10, 100]:
    model = LogisticRegression(
        C = c,
        random_state = 42
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"\nC: {c}")
    print(f"Accuracy: {accuracy:.2f}")
'''


#GridSearchCV
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8],
    'Attendance': [50,55,60,65,70,75,80,90],
    'Pass': [0,0,0,0,1,1,1,1]
}
df = pd.DataFrame(data)
X = df[['Study_Hours', 'Attendance']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

param_grid = {
    'n_neighbors' : [1,3]
}

grid = GridSearchCV(
    KNeighborsClassifier(),
    param_grid,
    cv = 3
)
grid.fit(X_train, y_train)
print("Best Parameters: ", grid.best_params_)
print("Best Score: ", grid.best_score_)