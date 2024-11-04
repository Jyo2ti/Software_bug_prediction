from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    try:
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        print("Model trained successfully.")
        return model
    except Exception as e:
        print(f"An error occurred while training the model: {str(e)}")
        return None
