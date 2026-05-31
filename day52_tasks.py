# Basic KNN Model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd
data = {
    'Hours' : [1,2,3,6,7,8],
    'Pass' : [0,0,0,1,1,1]
}
df = pd.DataFrame(data)

X = df[['Hours']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
prediction = model.predict([[5]])
print(prediction)


data = {
    'Age' : [18,20,25,30,35],
    'Bought_phone' : [0,0,1,1,1] 
}
df = pd.DataFrame(data)
X = df[['Age']]
y = df['Bought_phone']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

prediction = model.predict([[22]])
print(prediction)



#Task 3
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8,2,5,6,9],
    
    'Sleep_Hours': [4,5,5,6,6,7,8,8,4,7,6,9],
    
    'Attendance': [50,55,60,65,70,75,80,90,52,72,78,95],
    
    'Pass': [0,0,0,0,1,1,1,1,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[['Study_Hours', 'Sleep_Hours', 'Attendance']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
new_student = pd.DataFrame({
    'Study_Hours' : [6],
    'Sleep_Hours' : [7],
    'Attendance' : [76]
})

prediction = model.predict(new_student)
print(prediction)
print("Accuracy: ",accuracy)