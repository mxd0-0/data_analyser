import matplotlib.pyplot as plt

from load_and_inspect_data import iris_df, diabetes_df


def visualize_class_proportion_pie(df, target_column, dataset_name):
    """
    Generates a pie chart to display the proportion of each class
    in a specified target column of a DataFrame.
    """
    print(f"--- Visualizing Class Proportion for: {dataset_name} - '{target_column}' ---")

    # Get value counts for the target column
    class_counts = df[target_column].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title(f'Pie Chart: Proportion of {target_column} in {dataset_name} Dataset')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.show()
    print("Pie Chart generated.")
    print("-" * 50)


# Assuming iris_df and diabetes_df are already loaded from Code 1
# If not, run Code 1 first or load them here:
# iris_df = pd.read_csv('iris.csv')
# diabetes_df = pd.read_csv('diabetes.csv')

# For the Iris dataset, the target variable is 'variety'
visualize_class_proportion_pie(iris_df, 'variety', 'Iris')

# For the Diabetes dataset, the target variable is 'Outcome'
visualize_class_proportion_pie(diabetes_df, 'Outcome', 'Diabetes')
