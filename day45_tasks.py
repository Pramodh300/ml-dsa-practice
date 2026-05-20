import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score, confusion_matrix

'''#Logistic Regression
data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

print("\n Classification Report: \n", classification_report(y_test, y_pred))

correct = (y_test == y_pred).sum()
incorrect = (y_test != y_pred).sum()

print("Correct Predictions: ", correct)
print("Incorrect Predictions: ", incorrect)



#Confusion matrix from scratch
y_actual = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0,
            1, 1, 0, 0, 1, 0, 1, 1, 0, 1]
y_pred   = [1, 0, 1, 0, 0, 1, 1, 0, 0, 0,
            1, 1, 0, 1, 1, 0, 0, 1, 0, 1]

def confusion_matrix(y_actual, y_pred):

    TP = FP = TN = FN = 0

    for actual, pred in zip(y_actual, y_pred):
        if actual == 1 and pred == 1:
            TP += 1
        elif actual == 0 and pred == 1:
            FP += 1
        elif actual == 0 and pred == 0:
            TN += 1
        elif actual == 1 and pred == 0:
            FN += 1
    
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print("Accuracy: ", accuracy)
    print("Precision: ", precision)
    print("Recall: ", recall)
    print("F1 Score: ", f1_score)

#Using sklearn
cm = confusion_matrix(y_actual, y_pred)
print("Confusion Matrix: ", cm)

accuracy = accuracy_score(y_actual, y_pred)
precision = precision_score(y_actual, y_pred)
recall = recall_score(y_actual, y_pred)
f1 = f1_score(y_actual, y_pred)

print("Accuracy: ", accuracy)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1 Score: ", f1)
'''


#Full Pipeline


data = {
    'Age':          [22, 45, 35, 28, 52, 31, 29, 41, 38, 26,
                     48, 33, 27, 55, 42, 36, 24, 50, 39, 30],
    'Study_Hours':  [1, 8, 5, 3, 9, 6, 2, 7, 6, 2,
                     8, 4, 1, 9, 7, 5, 2, 8, 6, 3],
    'Sleep_Hours':  [5, 8, 7, 6, 9, 7, 5, 8, 7, 6,
                     8, 7, 5, 9, 8, 7, 6, 8, 7, 6],
    'Passed':       [0, 1, 1, 0, 1, 1, 0, 1, 1, 0,
                     1, 0, 0, 1, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

df['Study_Sleep_Ratio'] = (df['Study_Hours'] / df['Sleep_Hours'])
df['Is_Experienced'] = df['Age'].apply(lambda x: 1 if x > 35 else 0)

X = df.drop('Passed', axis = 1)
y = df['Passed']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.25,
    random_state = 42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:", cm)

TN, FP, FN, TP = cm.ravel()
print("TN: ", TN)
print("FP: ", FP)
print("FN: ", FN)
print("TP: ", TP)

print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Precision: ", precision_score(y_test, y_pred))
print("Recall: ", recall_score(y_test, y_pred))
print("F1 Score: ", f1_score(y_test, y_pred))

age               = 30
study_hours       = 7
sleep_hours       = 8
study_sleep_ratio = study_hours / sleep_hours
is_experienced    = 1 if age > 35 else 0

new_data = np.array([[age, study_hours, sleep_hours, study_sleep_ratio, is_experienced]])

prediction = model.predict(new_data)
probability = model.predict_proba(new_data)[:,1]

print(f"\n Prediction: {'Pass' if prediction[0] == 1 else 'Fail'}")
print(f"Probability of passing: {probability[0]:.2f}")