from load_and_inspect_data import iris_df, diabetes_df


def analyze_missing_values(df, name):
    """
    Analyzes and prints the number of observations,
    total missing values, and missing values per column for a DataFrame.
    """
    print(f"--- Analyzing Missing Values in: {name} Dataset ---")

    print(f"\nNumber of observations (rows): {len(df)}")

    total_missing = df.isnull().sum().sum()
    print(f"\nTotal number of missing values (NaNs) across all columns: {total_missing}")

    print("\nMissing values (NaNs) per column:")
    print(df.isnull().sum())  # Counts NaN values per column

    print("\nPercentage of missing values per column:")
    print((df.isnull().sum() / len(df)) * 100)
    print("-" * 50)


# Assuming iris_df and diabetes_df are already loaded from Code 1
# If not, run Code 1 first or load them here:
# iris_df = pd.read_csv('iris.csv')
# diabetes_df = pd.read_csv('diabetes.csv')

analyze_missing_values(iris_df, 'Iris')
analyze_missing_values(diabetes_df, 'Diabetes')
