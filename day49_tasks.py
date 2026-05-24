from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
'''#Precision & Recall
TP = 40
FP = 10
FN = 20
precision = TP / (TP + FP)
print(precision)


#F1 score
Precision = 0.8
Recall = 0.5

F1__score = 2 * (Precision * Recall) / (Precision + Recall)
print(F1__score)


y_true = [1,0,1,1,0,1]
y_pred = [1,1,1,0,0,1]

print(f1_score(y_true, y_pred))

cm = confusion_matrix(y_true, y_pred)
TN, FP, FN, TP = cm.ravel()
print("TP: ", TP)
print("FP: ", FP)
print("FN: ", FN)
'''

#Cross validation
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
model = LogisticRegression()
scores = cross_val_score(model, X, y, cv=5)
print(scores)
print("Average:", scores.mean())

X, y = load_iris(return_X_y=True)
model = LogisticRegression()
scores = cross_val_score(model, X, y, cv=3)
print(scores)
print("Average:", scores.mean())


X, y = load_iris(return_X_y=True)
model = LogisticRegression()
scores = cross_val_score(model, X, y, cv=10)
print(scores)
print("Average:", scores.mean())