import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import pickle

# Load dataset
df = pd.read_csv("train.csv")

# Select features
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']]

# Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Encode Sex
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])

# Split data
X = df[['Pclass', 'Sex', 'Age', 'Fare']]
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Models
rf = RandomForestClassifier()
nb = GaussianNB()

rf.fit(X_train, y_train)
nb.fit(X_train, y_train)

# Accuracy
print("Random Forest Accuracy:", rf.score(X_test, y_test))
print("Naive Bayes Accuracy:", nb.score(X_test, y_test))

# Save models
pickle.dump(rf, open("model_rf.pkl", "wb"))
pickle.dump(nb, open("model_nb.pkl", "wb"))

print("Models saved ✔")
