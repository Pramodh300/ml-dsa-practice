import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.datasets import load_breast_cancer

# Load data
data    = load_breast_cancer()
X, y    = data.data, data.target

# Split and scale
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# Train
model   = LogisticRegression()
model.fit(X_train, y_train)
y_pred  = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Visualize with heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cm,
            annot=True,          # show numbers inside
            fmt='d',             # integer format
            cmap='Blues',        # color scheme
            xticklabels=['Predicted 0', 'Predicted 1'],
            yticklabels=['Actual 0',    'Actual 1'])

plt.title('Confusion Matrix Heatmap')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.show()


#Confusion Matrix
y_actual = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred   = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

TP = 4
TN = 4
FP = 1
FN = 1

accuracy = (TP + TN) / (TP + TN + FP + FN)
print("Accuracy: ", accuracy)

precision = TP / (TP + FP)
print("Precision: ", precision)

recall = TP / (TP + FN)
print("Recall: ", recall)

f1_score1 = 2 * (precision * recall) / (precision + recall)
print("F1 Score: ", f1_score1)

print("\n Using sklearn: \n")
cm = confusion_matrix(y_actual, y_pred)
print("Confusion Matrix:\n", cm)

accuracy_sklearn = accuracy_score(y_actual, y_pred)
precision_sklearn = precision_score(y_actual, y_pred)
recall_sklearn = recall_score(y_actual, y_pred)
f1_score_sklearn = f1_score(y_actual, y_pred)

print("Accuracy: ", accuracy_sklearn)
print("Precision: ", precision_sklearn) 
print("Recall: ", recall_sklearn)
print("F1 Score: ", f1_score_sklearn)



#ROC Curve + AUC
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model    import LogisticRegression
from sklearn.ensemble        import RandomForestClassifier
from sklearn.neighbors       import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing   import StandardScaler
from sklearn.metrics import roc_curve, roc_auc_score

data    = load_breast_cancer()
X, y    = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest' : RandomForestClassifier(),
    'KNN' : KNeighborsClassifier(n_neighbors=5)
}

plt.figure(figsize=(8, 6))
best_model = None
best_auc = 0

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    auc = roc_auc_score(y_test, y_prob)
    print(f"\n{name} = Auc: {auc:.4f}")
    plt.plot(fpr, tpr,
             label = f'ROC Curve (AUC = {auc: .4f})')
    
    if auc > best_auc:
        best_auc = auc
        best_model = name


plt.plot([0, 1], [0, 1], linestyle='--')

plt.title('ROC Curve Comparison')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")

plt.legend()
plt.show()

print(f"Best Model: {best_model} with AUC: {best_auc: .4f}")



#Full Code
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve
)

# ----------------------------------------
# Create DataFrame
# ----------------------------------------

data = {
    'Age': [22, 45, 35, 28, 52, 31, 29, 41,
            38, 26, 48, 33, 27, 55, 42, 36,
            24, 50, 39, 30, 44, 37, 23, 51,
            32, 47, 25, 43, 40, 34],

    'Study_Hours': [1, 8, 5, 3, 9, 6, 2, 7,
                    6, 2, 8, 4, 1, 9, 7, 5,
                    2, 8, 6, 3, 7, 5, 1, 9,
                    4, 8, 2, 7, 6, 4],

    'Sleep_Hours': [5, 8, 7, 6, 9, 7, 5, 8,
                    7, 6, 8, 7, 5, 9, 8, 7,
                    6, 8, 7, 6, 8, 7, 5, 9,
                    7, 8, 6, 8, 7, 7],

    'Passed': [0, 1, 1, 0, 1, 1, 0, 1,
               1, 0, 1, 0, 0, 1, 1, 1,
               0, 1, 1, 0, 1, 1, 0, 1,
               0, 1, 0, 1, 1, 1]
}

df = pd.DataFrame(data)


# ----------------------------------------
# Feature Engineering
# ----------------------------------------

df['Study_Sleep_Ratio'] = (
    df['Study_Hours'] / df['Sleep_Hours']
)

df['Is_Experienced'] = np.where(
    df['Age'] > 35,
    1,
    0
)


# ----------------------------------------
# Features and Target
# ----------------------------------------

X = df.drop('Passed', axis=1)
y = df['Passed']


# ----------------------------------------
# Train-Test Split
# ----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ----------------------------------------
# Scaling AFTER split
# ----------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)


# ----------------------------------------
# Logistic Regression
# ----------------------------------------

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]


# ----------------------------------------
# Confusion Matrix
# ----------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)


# ----------------------------------------
# Heatmap
# ----------------------------------------

plt.figure(figsize=(6, 4))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()


# ----------------------------------------
# Normalized Confusion Matrix
# ----------------------------------------

cm_normalized = (
    cm.astype('float') /
    cm.sum(axis=1)[:, np.newaxis]
)

plt.figure(figsize=(6, 4))

sns.heatmap(
    cm_normalized,
    annot=True,
    fmt='.2f',
    cmap='Blues'
)

plt.title("Normalized Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()


# ----------------------------------------
# ROC Curve
# ----------------------------------------

fpr, tpr, thresholds = roc_curve(
    y_test,
    y_prob
)

auc_score = roc_auc_score(
    y_test,
    y_prob
)

plt.figure(figsize=(7, 5))

plt.plot(
    fpr,
    tpr,
    label=f"AUC = {auc_score:.2f}"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle='--'
)

plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")

plt.legend()

plt.show()


# ----------------------------------------
# Metrics
# ----------------------------------------

accuracy  = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall    = recall_score(y_test, y_pred)

f1        = f1_score(y_test, y_pred)

auc       = roc_auc_score(y_test, y_prob)

print("\nMetrics:")
print(f"Accuracy : {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall   : {recall:.2f}")
print(f"F1 Score : {f1:.2f}")
print(f"AUC Score: {auc:.2f}")


# ----------------------------------------
# Error Analysis
# ----------------------------------------

TN, FP, FN, TP = cm.ravel()

print("\nError Analysis:")

print(f"FP = {FP}")
print(f"FN = {FN}")

print("\nMore Dangerous Error:")

print("False Negatives (FN) are more dangerous.")
print(
    "Because predicting a student will FAIL "
    "when they would actually PASS can lead "
    "to unnecessary interventions or wrong decisions."
)