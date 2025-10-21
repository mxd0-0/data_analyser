import pandas as pd


def load_and_inspect_data(filepath):
    print(f"--- Loading and Inspecting: {filepath} ---")
    df = pd.read_csv(filepath)

    print("\nShape of the data (rows, columns):")
    print(df.shape)

    print("\nData types of each column:")
    print(df.info())

    print("\nFirst 3 rows of the data:")
    print(df.head(3))
    print("-" * 50)
    return df


# Load and inspect iris dataset
iris_df = load_and_inspect_data('Data/iris.csv')

# Load and inspect diabetes dataset
diabetes_df = load_and_inspect_data('Data/diabetes.csv')
