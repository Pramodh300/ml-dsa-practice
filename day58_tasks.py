#Kaggle project
from day57_dsa import new_data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier


df = sns.load_dataset('titanic')
df.head()
df.info()
df.describe()
df['age'] = df['age'].fillna(df['age'].mean())
df['deck'] = df['deck'].cat.add_categories('Unknown')
df['deck'] = df['deck'].fillna('Unknown')
df['embarked'] = df['embarked'].fillna('Unknown')
df['embark_town'] = df['embark_town'].fillna('Unknown')
df = df.drop_duplicates()

sns.countplot(x='sex', hue='survived', data=df)
plt.show()

sns.countplot(x='pclass', hue='survived', data = df)
plt.title("Survival by passenger class")
plt.show()

sns.histplot(df['age'], bins = 20, kde=True)
plt.title("Distribution of Age")
plt.show()


sns.boxplot(x='survived', y='age', data = df)
plt.title('Age vs Survival')
plt.show()


df = df[['survived', 'pclass', 'sex', 'age', 'fare', 'embarked']]
df = pd.get_dummies(df, columns = ['sex', 'embarked'], drop_first = True)

X = df.drop('survived', axis = 1)
y = df['survived']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 42
)

param_grid = {
    'max_depth' : [2, 3, 5],
    'min_samples_split' : [2, 3, 5]
}

model = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv = 3
)

model.fit(X_train, y_train)

with open('titanic_mode.pkl', 'wb') as file:
    pickle.dump(model, file)