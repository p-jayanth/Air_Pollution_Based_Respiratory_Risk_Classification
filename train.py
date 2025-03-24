
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset (replace 'aqi_dataset.csv' with actual dataset file)
data = pd.read_csv("MainDataSet.csv")


# Data Cleaning and Preparation
data_cleaned = data.iloc[3:].reset_index(drop=True)
data_cleaned.columns = ['S.No', 'State', 'City', 'Station Name', 'Current AQI value']
data_cleaned.dropna(subset=['State', 'Current AQI value'], inplace=True)
data_cleaned['Current AQI value'] = pd.to_numeric(data_cleaned['Current AQI value'], errors='coerce')

data_cleaned['Living Condition'] = data_cleaned['Current AQI value'].apply(lambda x: 1 if x > 100 else 0)


X = data_cleaned[['Current AQI value']]
y = data_cleaned['Living Condition']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save trained model
with open("prediction_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

print("Model saved as prediction_model.pkl")


# import pickle
# import pandas as pd
# from sklearn.ensemble import GradientBoostingClassifier, VotingClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
#
# # Load dataset (replace 'MainDataSet.csv' with actual dataset file)
# data = pd.read_csv("MainDataSet.csv")
#
# # Data Cleaning and Preparation
# data_cleaned = data.iloc[3:].reset_index(drop=True)
# data_cleaned.columns = ['S.No', 'State', 'City', 'Station Name', 'Current AQI value']
# data_cleaned.dropna(subset=['State', 'Current AQI value'], inplace=True)
# data_cleaned['Current AQI value'] = pd.to_numeric(data_cleaned['Current AQI value'], errors='coerce')
#
# # Creating a target variable: 1 if AQI > 100 (poor living condition), else 0
# data_cleaned['Living Condition'] = data_cleaned['Current AQI value'].apply(lambda x: 1 if x > 100 else 0)
#
# # Feature and target selection
# X = data_cleaned[['Current AQI value']]
# y = data_cleaned['Living Condition']
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Ensemble Model 1: Gradient Boosting Classifier
# gbc_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
# gbc_model.fit(X_train, y_train)
#
# # Model Evaluation for Gradient Boosting
# y_pred_gbc = gbc_model.predict(X_test)
# accuracy_gbc = accuracy_score(y_test, y_pred_gbc)
# print(f"Gradient Boosting Model Accuracy: {accuracy_gbc:.2f}")
#
# # Ensemble Model 2: Voting Classifier (Combination of Decision Tree and Logistic Regression)
# dt_model = DecisionTreeClassifier(random_state=42)
# lr_model = LogisticRegression()
#
# voting_model = VotingClassifier(estimators=[
#     ('dt', dt_model),
#     ('lr', lr_model)
# ], voting='hard')
#
# voting_model.fit(X_train, y_train)
#
# # Model Evaluation for Voting Classifier
# y_pred_voting = voting_model.predict(X_test)
# accuracy_voting = accuracy_score(y_test, y_pred_voting)
# print(f"Voting Classifier Model Accuracy: {accuracy_voting:.2f}")
#
# # Save trained models
# with open("gradient_boosting_model.pkl", "wb") as gbc_file:
#     pickle.dump(gbc_model, gbc_file)
# print("Gradient Boosting Model saved as gradient_boosting_model.pkl")
#
# with open("voting_model.pkl", "wb") as voting_file:
#     pickle.dump(voting_model, voting_file)
# print("Voting Classifier Model saved as voting_model.pkl")
