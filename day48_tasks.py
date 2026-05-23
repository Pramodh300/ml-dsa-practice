from sklearn.metrics import confusion_matrix
'''#Identify TP, TN, FP, FN
actual = [1, 1, 0, 0]
predicted = [1, 0, 1, 0]
cm = confusion_matrix(actual, predicted)
TN, FP, FN, TP = cm.ravel()

print("TP: ", TP)
print("TN: ", TN)
print("FP: ", FP)
print("FN: ", FN)


#Calculate Accuracy
TP = 40
TN = 50
FP = 5
FN = 5

accuracy = (TP + TN) / (TP + TN + FP + FN)
print(accuracy)


#Calculate Precision
TP = 30
FP = 10
Precision = TP / (TP + FP)
print(Precision)


#Calculate Recall
TP = 25
FN = 5
Recall = TP / (TP + FN)
print(Recall)
'''


#Sklearn Metrics Practice
from sklearn.metrics import accuracy_score, precision_score, recall_score
y_true = [1, 0, 1, 1, 0, 1]
y_pred = [1, 0, 1, 0, 0, 1]

print("Accuracy: ", accuracy_score(y_true, y_pred))
print("Precision: ",precision_score(y_true, y_pred))
print("Recall: ", recall_score(y_true, y_pred))