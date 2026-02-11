import pandas as pd

df = pd.read_csv("student_focus_data.csv")

# Check missing values
print(df.isnull().sum())

# Convert time into numeric feature
df["start_hour"] = df["start_time"].str.split(":").str[0].astype(int)

# Drop unnecessary column
df.drop("start_time", axis=1, inplace=True)

# Save cleaned data
df.to_csv("clean_data.csv", index=False)

print("Data cleaned successfully!")
