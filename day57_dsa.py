#Save a decision tree model
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
import pickle
import pandas as pd

data = {
    'Study_Hours': [1,2,3,4,5,6,7,8],
    'Pass': [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)
X = df[['Study_Hours']]
y = df['Pass']

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)
#Save the model to a file
with open('student_model.pkl', 'wb') as file:
    pickle.dump(model, file)
    print("Model saved successfully.")

#Load the model
with open('student_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
new_data = [[3]]
prediction = loaded_model.predict(new_data)
print(f"Prediction for Study_Hours = 3: {prediction[0]}")



#Random forest save and load
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8],
    'Pass': [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)
X = df[['Study_Hours']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size = 0.2,
    random_state = 42
)

param_grid = {
    'n_estimators': [10, 50, 100],
    'max_depth' : [2, 3, 5] 
}

model = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv = 3
)
model.fit(X_train, y_train)

with open('rf_model.pkl', 'wb') as file:
    pickle.dump(model, file)
    print('Model saved successfully.')

with open('rf_model.pkl', 'rb') as file:
    pickled_model = pickle.load(file)

new_data = pd.DataFrame({
    'Study_Hours' : [7]
})
prediction = pickled_model.predict(new_data)
print(f"Prediction for study hours {new_data['Study_Hours'][0]}: {prediction[0]}")