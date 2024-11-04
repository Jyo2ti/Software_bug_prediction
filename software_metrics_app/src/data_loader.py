import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(bugs_csv_path, target_column):
    try:
        # Load the dataset
        data = pd.read_csv(bugs_csv_path)
        print("CSV file loaded successfully.")

        # Check if target_column exists in the data
        if target_column not in data.columns:
            print(f"Target column '{target_column}' not found in the dataset.")
            print(f"Available columns: {data.columns.tolist()}")
            return None

        # Split the dataset into features (X) and target (y)
        X = data.drop(columns=[target_column])
        y = data[target_column]
        print("Features and target variable separated.")

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print("Data split into training and testing sets.")

        # Initialize and fit a scaler
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        print("Data scaled.")

        # Get the feature names
        feature_names = X.columns.tolist()
        print("Feature names extracted:", feature_names)

        # Return the preprocessed data
        return X_train_scaled, X_test_scaled, y_train, y_test, scaler, feature_names

    except FileNotFoundError:
        print(f"File not found: {bugs_csv_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    # Convert columns to numeric, forcing errors to NaN
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(file_path, target_column):
    # Load the data from the CSV file
    data = pd.read_csv(file_path, delimiter=';')  # Specify the delimiter if your data uses ';'

    # Convert columns to numeric, forcing errors to NaN
    data = data.apply(pd.to_numeric, errors='coerce')

    # Check if the target column exists in the data
    if target_column not in data.columns:
        raise ValueError(f"Target column '{target_column}' not found in the data. Available columns: {data.columns}")

    # Separate features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Get feature names after preprocessing
    feature_names = X.columns.tolist()

    return X_train, X_test, y_train, y_test, scaler, feature_names

