import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv("student_marks_with_anomalies.csv")

df.head()

df.tail()

df.info()

df.isnull().sum()

sns.boxplot(x=df["Maths Marks"])
plt.show()

sns.boxplot(x=df["Cyber Marks"])
plt.show()

plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)
plt.show()

sns.scatterplot(x="Maths Marks", y="Cyber Marks", data=df)
plt.show()

df.isnull()
