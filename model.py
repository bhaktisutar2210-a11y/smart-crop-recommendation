import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

print("Training Started...")

df = pd.read_excel("1million dataset crop.xlsx")

X = df.iloc[:, 0:7]
y = df.iloc[:, 7]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model Saved Successfully!")