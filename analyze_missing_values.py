from load_and_inspect_data import iris_df, diabetes_df


def analyze_missing_values(df, name):

    print(f"--- Analyzing Missing Values in: {name} Dataset ---")

    print(f"\nNumber of observations (rows): {len(df)}")

    total_missing = df.isnull().sum().sum()
    print(f"\nTotal number of missing values (NaNs) across all columns: {total_missing}")

    print("\nMissing values (NaNs) per column:")
    print(df.isnull().sum())  # Counts NaN values per column

    print("\nPercentage of missing values per column:")
    print((df.isnull().sum() / len(df)) * 100)
    print("-" * 50)



analyze_missing_values(iris_df, 'Iris')
analyze_missing_values(diabetes_df, 'Diabetes')
