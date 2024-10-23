import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
data = pd.read_csv(r'C:\Users\cgmst\OneDrive\Desktop\CSV files\merged_reports.csv')
X = data.drop('delivered', axis=1)  
y = data['delivered']  
X_encoded = pd.get_dummies(X, columns=['year', 'month', 'division', 'section'])
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)