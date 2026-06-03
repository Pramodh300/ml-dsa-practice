import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Random forest
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8],
    'Attendance': [50,55,60,65,70,75,80,90],
    'Sleep_Hours': [4,5,5,6,6,7,8,8],
    'Pass': [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[['Study_Hours', 'Attendance', 'Sleep_Hours']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 42
)

model = RandomForestClassifier(n_estimators = 10)
model.fit(X_train, y_train)

new_data = pd.DataFrame({
    'Study_Hours': [6],
    'Attendance': [78],
    'Sleep_Hours': [7]
})
prediction = model.predict(new_data)
print(prediction)



#Decision tree vs Random forest
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8],
    'Attendance': [50,55,60,65,70,75,80,90],
    'Sleep_Hours': [4,5,5,6,6,7,8,8],
    'Pass': [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[['Study_Hours', 'Attendance', 'Sleep_Hours']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 42
)

model_Dt = DecisionTreeClassifier()
model_Dt.fit(X_train, y_train)

model_Rf = RandomForestClassifier()
model_Rf.fit(X_train, y_train)

new_data = pd.DataFrame({
    'Study_Hours': [6],
    'Attendance': [78],
    'Sleep_Hours': [7]
})
prediction_Dt = model_Dt.predict(new_data)
print("Decision Tree Prediction:", prediction_Dt)

prediction_Rf = model_Rf.predict(new_data)
print("Random Forest Prediction:", prediction_Rf)



#Feature importance
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8],
    'Attendance': [50,55,60,65,70,75,80,90],
    'Sleep_Hours': [4,5,5,6,6,7,8,8],
    'Pass': [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[['Study_Hours', 'Attendance', 'Sleep_Hours']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 42
)

model = RandomForestClassifier(n_estimators = 10)
model.fit(X_train, y_train)

model.feature_importances_
for feature, importance in zip(X.columns, model.feature_importances_):
    print(f"{feature} , {importance:.2f}")



#Increase Trees
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8],
    'Attendance': [50,55,60,65,70,75,80,90],
    'Sleep_Hours': [4,5,5,6,6,7,8,8],
    'Pass': [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[['Study_Hours', 'Attendance', 'Sleep_Hours']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 42
)

model = RandomForestClassifier(n_estimators = 200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy with 200 trees: ", accuracy)
prediction = model.predict(X_test)
print(prediction)



#Add noisy data
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8,8,2],
    'Attendance': [50,55,60,65,70,75,80,90,90,85],
    'Sleep_Hours': [4,5,5,6,6,7,8,8,8,7],
    'Pass': [0,0,0,0,1,1,1,1,0,1]
}
df = pd.DataFrame(data)
X = df[['Study_Hours', 'Attendance', 'Sleep_Hours']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 42
)

model_Rf = RandomForestClassifier(n_estimators = 100)
model_Rf.fit(X_train, y_train)
y_pred_Rf = model_Rf.predict(X_test)
accuracy_Rf = accuracy_score(y_test, y_pred_Rf)
print("Accuracy of Random Forest with noisy data: ", accuracy_Rf)

model_Dt = DecisionTreeClassifier()
model_Dt.fit(X_train, y_train)
y_pred_Dt = model_Dt.predict(X_test)
accuracy_Dt = accuracy_score(y_test, y_pred_Dt)
print("Accuracy of Decision Tree with noisy data: ", accuracy_Dt)

print("Actual:", y_test.values)
print("RF Predictions:", y_pred_Rf)
print("DT Predictions:", y_pred_Dt)