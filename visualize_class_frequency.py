import matplotlib.pyplot as plt
import seaborn as sns  # Often used for better aesthetics

from load_and_inspect_data import iris_df, diabetes_df


def visualize_class_frequency(df, target_column, dataset_name):
    print(f"--- Visualizing Class Frequency for: {dataset_name} - '{target_column}' ---")

    # Get value counts for the target column
    class_counts = df[target_column].value_counts()
    classes = class_counts.index
    counts = class_counts.values

    # Bar Chart
    plt.figure(figsize=(8, 5))
    sns.barplot(x=classes, y=counts, palette='viridis')
    plt.title(f'Bar Chart: Frequency of {target_column} in {dataset_name} Dataset')
    plt.xlabel(target_column)
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    print("Bar Chart generated.")

    # Line Chart (often less intuitive for pure frequency, but can show trends if classes have an order)
    # For categorical data, we typically don't use a line chart for frequency unless there's an inherent order.
    # However, to meet the request, we can plot it against an index.
    plt.figure(figsize=(8, 5))
    sns.lineplot(x=classes, y=counts, marker='o', palette='viridis', sort=False)
    plt.title(f'Line Chart: Frequency of {target_column} in {dataset_name} Dataset')
    plt.xlabel(target_column)
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    print("Line Chart generated.")

    # Scatter Chart (similar to line chart for frequency; points represent frequencies)
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=classes, y=counts, s=100, hue=classes, palette='viridis', legend=False)
    plt.title(f'Scatter Chart: Frequency of {target_column} in {dataset_name} Dataset')
    plt.xlabel(target_column)
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    print("Scatter Chart generated.")
    print("-" * 50)


# Assuming iris_df and diabetes_df are already loaded from Code 1
# If not, run Code 1 first or load them here:
# iris_df = pd.read_csv('iris.csv')
# diabetes_df = pd.read_csv('diabetes.csv')

visualize_class_frequency(iris_df, 'variety', 'Iris')
visualize_class_frequency(diabetes_df, 'Outcome', 'Diabetes')
