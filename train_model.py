import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
import pickle

# ---------------- LOAD DATA ----------------
df = pd.read_csv("train.csv")  # Kaggle Titanic dataset

# ---------------- CLEAN DATA ----------------
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']]
df['Age'].fillna(df['Age'].mean(), inplace=True)

# ---------------- ENCODING ----------------
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])  # male=1, female=0

# ---------------- FEATURES ----------------
X = df[['Pclass', 'Sex', 'Age', 'Fare']]
y = df['Survived']

# ---------------- TRAIN TEST SPLIT ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- NAIVE BAYES ----------------
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# ---------------- RANDOM FOREST ----------------
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# ---------------- ACCURACY ----------------
print("Naive Bayes Accuracy:", nb_model.score(X_test, y_test))
print("Random Forest Accuracy:", rf_model.score(X_test, y_test))

# ---------------- SAVE MODELS ----------------
pickle.dump(rf_model, open("model_rf.pkl", "wb"))
pickle.dump(nb_model, open("model_nb.pkl", "wb"))
