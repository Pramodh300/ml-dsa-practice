from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

'''#Decision tree
data = {
    'Study_Hours' : [1,2,3,6,7,8],
    'Attendance' : [50,55,60,75,80,90],
    'Pass' : [0,0,0,1,1,1]
}
df = pd.DataFrame(data)
X = df[['Study_Hours', 'Attendance']]
y = df['Pass']

model = DecisionTreeClassifier()
model.fit(X,y)
new_data = pd.DataFrame({
    'Study_Hours' : [5],
    'Attendance' : [70]
})
prediction = model.predict(new_data)
print(prediction)



#Added one more feature to the above program
data = {
    'Study_Hours' : [1,2,3,6,7,8],
    'Attendance' : [50,55,60,75,80,90],
    'Sleep_Hours' : [4,5,5,6,7,8],
    'Pass' : [0,0,0,1,1,1]
}

df = pd.DataFrame(data)
X = df[['Study_Hours', 'Attendance', 'Sleep_Hours']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
print(y_pred)



#Overfitting

data = {
    'Study_Hours': [1,2,3,4,5,6,7,8,2,5,6,9],

    'Attendance': [50,55,60,65,70,75,80,90,52,72,78,95],

    'Pass': [0,0,1,0,1,1,1,1,0,1,0,1]
}


df = pd.DataFrame(data)
X = df[['Study_Hours', 'Attendance']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(max_depth=2)
model.fit(X_train, y_train)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

train_accuracy = accuracy_score(y_train, train_pred)
test_accuracy = accuracy_score(y_test, test_pred)
print(f"Train accuracy: {train_accuracy:.2f}")
print(f"Test_accuracy: {test_accuracy:.2f}")
'''

#Mini Project
data = {
    'Study_Hours':  [1, 2, 3, 4, 5, 6, 7, 8, 2, 5, 6, 9, 3, 7, 8],
    'Sleep_Hours':  [4, 5, 5, 6, 6, 7, 8, 8, 5, 6, 7, 8, 4, 7, 8],
    'Attendance':   [50, 55, 60, 65, 70, 75, 80, 90, 58, 72, 78, 95, 62, 85, 88],
    'Mobile_Usage': [8, 7, 6, 5, 4, 3, 2, 1, 7, 4, 3, 1, 6, 2, 2],
    'Pass':         [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)
X = df[['Study_Hours', 'Sleep_Hours', 'Attendance', 'Mobile_Usage']]
y = df['Pass']

model1 = DecisionTreeClassifier()
model1.fit(X, y)

model2 = KNeighborsClassifier()
model2.fit(X, y)

new_data = pd.DataFrame({
    'Study_Hours' : [8],
    'Sleep_Hours' : [6],
    'Attendance' : [70],
    'Mobile_Usage' : [7]
})
prediction1 = model1.predict(new_data)
prediction2 = model2.predict(new_data)
print('Decision_tree: ',prediction1)
print("KNN: ",prediction2)