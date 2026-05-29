import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


data = {
    'Age': [25, 30, 35, np.nan, 40, 28, 32, np.nan],
    
    'Experience': [1, 3, 5, 7, np.nan, 2, 4, 6],
    
    'Education': [
        'BTech',
        'MTech',
        'BTech',
        'MBA',
        np.nan,
        'MTech',
        'MBA',
        'BTech'
    ],
    
    'City': [
        'Hyderabad',
        'Bangalore',
        'Chennai',
        'Hyderabad',
        'Delhi',
        np.nan,
        'Bangalore',
        'Delhi'
    ],
    
    'Skills': [
        'Python SQL',
        'Python ML',
        'Deep Learning Python',
        'Management Excel',
        'Python AI',
        'SQL Excel',
        'Machine Learning',
        'Python Data Analysis'
    ],
    
    'High_Salary': [0,1,1,0,1,0,1,1]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Experience'] = df['Experience'].fillna(df['Experience'].mean())
df['Education'] = df['Education'].fillna(df['Education'].mode()[0])
df['City'] = df['City'].fillna(df['City'].mode()[0])

le_edu = LabelEncoder()
le_city = LabelEncoder()

df['Education'] = le_edu.fit_transform(df['Education'])
df['City'] = le_city.fit_transform(df['City'])

cv = CountVectorizer()
skills_matrix = cv.fit_transform(df['Skills'])

skills_df = pd.DataFrame(skills_matrix.toarray(), columns = cv.get_feature_names_out())

print(skills_df)

df = df.drop('Skills', axis = 1)

final_df = pd.concat([df, skills_df], axis = 1)

print(final_df)

X = final_df.drop('High_Salary', axis = 1)
y  = final_df['High_Salary']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

new_data = pd.DataFrame({
    'Age': [30],
    'Experience': [3],
    'Education': ['MTech'],
    'City': ['Hyderabad'],
    'Skills': ['Python ML']
})

new_data['Education'] = le_edu.transform(new_data['Education'])
new_data['City'] = le_city.transform(new_data['City'])

new_skills = cv.transform(new_data['Skills'])

new_skills_df = pd.DataFrame(
    new_skills.toarray(),
    columns=cv.get_feature_names_out()
)

new_data = new_data.drop('Skills', axis=1)
final_input = pd.concat(
    [new_data.reset_index(drop=True),
    new_skills_df.reset_index(drop=True)],
    axis=1
)
prediction = model.predict(final_input)
print("Prediction: ","High Salary" if prediction[0] == 1 else "Low Salary")