import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("student_focus_data.csv")

print(df.head())
print(df.describe())

# Focus distribution
sns.histplot(df["focus_level"])
plt.title("Focus Level Distribution")
plt.show()

# Phone usage vs focus
sns.boxplot(x="phone_used", y="focus_level", data=df)
plt.title("Phone Usage vs Focus")
plt.show()

# Mood vs focus
sns.scatterplot(x="mood", y="focus_level", data=df)
plt.title("Mood vs Focus")
plt.show()
