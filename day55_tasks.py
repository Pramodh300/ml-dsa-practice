#First K-Means Model
from sklearn.cluster import KMeans
import pandas as pd

# Dataset
data = {
    'Study_Hours': [1,2,3,7,8,9],
    'Sleep_Hours': [4,5,5,8,9,8]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features
X = df[['Study_Hours', 'Sleep_Hours']]

# Create Model
model = KMeans(
    n_clusters=2,
    random_state=42
)

# Train Model
model.fit(X)

# Predict Clusters
clusters = model.predict(X)

# Print Clusters
print(clusters)



#Add Cluster Column
from sklearn.cluster import KMeans
import pandas as pd

# Dataset
data = {
    'Study_Hours': [1,2,3,7,8,9],
    'Sleep_Hours': [4,5,5,8,9,8]
}

# DataFrame
df = pd.DataFrame(data)

# Features
X = df[['Study_Hours', 'Sleep_Hours']]

# Model
model = KMeans(
    n_clusters=2,
    random_state=42
)

# Train
model.fit(X)

# Predict
clusters = model.predict(X)

# Add Cluster Column
df['Cluster'] = clusters

# Print DataFrame
print(df)



#Print Centroids
from sklearn.cluster import KMeans
import pandas as pd

# Dataset
data = {
    'Study_Hours': [1,2,3,7,8,9],
    'Sleep_Hours': [4,5,5,8,9,8]
}

# DataFrame
df = pd.DataFrame(data)

# Features
X = df[['Study_Hours', 'Sleep_Hours']]

# Model
model = KMeans(
    n_clusters=2,
    random_state=42
)

# Train
model.fit(X)

# Print Centroids
print("Centroids:")
print(model.cluster_centers_)



#Change K Value
from sklearn.cluster import KMeans
import pandas as pd

# Dataset
data = {
    'Study_Hours': [1,2,3,7,8,9],
    'Sleep_Hours': [4,5,5,8,9,8]
}

# DataFrame
df = pd.DataFrame(data)

# Features
X = df[['Study_Hours', 'Sleep_Hours']]

# Different K Values
for k in [2,3,4]:

    print(f"\nK = {k}")

    # Model
    model = KMeans(
        n_clusters=k,
        random_state=42
    )

    # Train
    model.fit(X)

    # Predict
    clusters = model.predict(X)

    # Add Cluster Column
    df['Cluster'] = clusters

    # Print DataFrame
    print(df)



#Real Student Grouping Project
from sklearn.cluster import KMeans
import pandas as pd

# Dataset
data = {
    'Study_Hours': [2,4,5,6,8,9],

    'Sleep_Hours': [4,5,6,7,8,9],

    'Attendance': [50,60,70,75,85,95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features
X = df[['Study_Hours', 'Sleep_Hours', 'Attendance']]

# Create Model
model = KMeans(
    n_clusters=3,
    random_state=42
)

# Train Model
model.fit(X)

# Predict Clusters
clusters = model.predict(X)

# Add Cluster Column
df['Cluster'] = clusters

# Print Final DataFrame
print(df)

# Print Centroids
print("\nCentroids:")
print(model.cluster_centers_)