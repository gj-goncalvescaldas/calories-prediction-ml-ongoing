# Databricks notebook source
from pyspark.sql import functions as F
import matplotlib.pyplot as plt
import seaborn as sns

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /FileStore/tables

# COMMAND ----------

# MAGIC %md
# MAGIC # Data

# COMMAND ----------

test_df = spark.read.option("Header", True).option("InferSchema", True).csv('/FileStore/tables/test-3.csv')
display(test_df.head(1))
test_df.printSchema()

# COMMAND ----------

train_df = spark.read.option("Header", True).option("InferSchema", True).csv('/FileStore/tables/train-2.csv')
display(train_df.head(10))
train_df.printSchema()

# COMMAND ----------

display(train_df.describe())

# COMMAND ----------

numerical_features = ["Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp", "Calories"]

for feature in numerical_features:
    # Estadísticas en PySpark
    stats = train_df.select(
        F.mean(feature).alias("mean"),
        F.stddev(feature).alias("stddev"),
        F.min(feature).alias("min"),
        F.max(feature).alias("max"),
        F.skewness(feature).alias("skew"),
        F.count(F.when(F.col(feature).isNull() | F.isnan(feature), feature)).alias("missing")
    ).collect()[0]

    print(f"\n{feature} statistics:")
    print(f"  Mean: {stats['mean']:.2f}")
    print(f"  Std Dev: {stats['stddev']:.2f}")
    print(f"  Min: {stats['min']}")
    print(f"  Max: {stats['max']}")
    print(f"  Skewness: {stats['skew']:.2f}")
    print(f"  Missing: {stats['missing']}")

    # Visualización: convertir a Pandas
    pandas_df = train_df.select(feature).dropna().toPandas()

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    sns.histplot(pandas_df[feature], kde=True, bins=30)
    plt.title(f"Histogram of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    sns.boxplot(x=pandas_df[feature])
    plt.title(f"Box Plot of {feature}")

    plt.tight_layout()
    plt.show()

# COMMAND ----------

sex_counts_df = train_df.groupBy("Sex").count()

display(sex_counts_df)

sex_counts_pd = sex_counts_df.toPandas().set_index("Sex")["count"]


plt.figure(figsize=(6, 6))
plt.pie(sex_counts_pd, labels=sex_counts_pd.index, autopct='%1.1f%%', startangle=90)
plt.title("Distribution of Sex")
plt.axis("equal")
plt.show()

# COMMAND ----------

numeric_pd = train_df.select(*numerical_features).toPandas()

colors = sns.color_palette('husl', len(numerical_features))

for col, color in zip(numerical_features, colors):
    plt.figure(figsize=(8, 5))
    sns.kdeplot(data=numeric_pd, x=col, fill=True, color=color)
    plt.title(f'KDE Plot of {col}', fontsize=16, color=color)
    plt.xlabel(col)
    plt.ylabel('Density')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# COMMAND ----------

features = ["Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"]

for feature in features:
    plt.figure(figsize=(7, 5))
    sns.scatterplot(data=numeric_pd, x=feature, y="Calories", alpha=0.5)
    plt.title(f"{feature} vs Calories", fontsize=14)
    plt.xlabel(feature)
    plt.ylabel("Calories")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# COMMAND ----------

correlation_matrix = numeric_pd.corr()

calories_corr = correlation_matrix["Calories"].sort_values(ascending=False)
print("\nCorrelación con 'Calories':\n")
print(calories_corr)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", square=True)
plt.title("Correlation Matrix of Numerical Features", fontsize=14)
plt.tight_layout()
plt.show()

# COMMAND ----------

