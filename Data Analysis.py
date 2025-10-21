from load_and_inspect_data import iris_df, diabetes_df


def analyze_dataframe_structure(df, name):
    print(f"--- Analyzing Structure of: {name} Dataset ---")

    print("\nNumber of rows and columns (Shape):")
    print(df.shape)

    print("\nFeature names (Column Names):")
    print(df.columns.tolist())

    print("\nDescription of the data (Descriptive Statistics):")
    print(df.describe())
    print("-" * 50)


analyze_dataframe_structure(iris_df, 'Iris')
analyze_dataframe_structure(diabetes_df, 'Diabetes')
