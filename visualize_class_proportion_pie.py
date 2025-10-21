import matplotlib.pyplot as plt

from load_and_inspect_data import iris_df, diabetes_df


def visualize_class_proportion_pie(df, target_column, dataset_name):
    print(f"--- Visualizing Class Proportion for: {dataset_name} - '{target_column}' ---")

    class_counts = df[target_column].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title(f'Pie Chart: Proportion of {target_column} in {dataset_name} Dataset')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    print("Pie Chart generated.")
    print("-" * 50)


visualize_class_proportion_pie(iris_df, 'variety', 'Iris')
visualize_class_proportion_pie(diabetes_df, 'Outcome', 'Diabetes')
