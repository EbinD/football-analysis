import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("players.csv")

# print(df.head())
# print("Shape:", df.shape)
# print("Columns:", df.index.tolist())
# print("Missing values:\n", df.isnull().sum())
# print("Summary stats:\n", df.describe())

# forward = df[df["Position"] == "Forward"]
# print(forward)

# highscores = df[df["Goals"] > 25]
# print(highscores)

# sort = df.sort_values(by="Assists", ascending=True)
# print(sort)

# best_passer = df.sort_values(by="PassAccuracy", ascending=False).head(3)
# print(best_passer)

# average_goals_by_position = df[df.groupby("Position")["Goals"].mean()]
# print(average_goals_by_position)

# avg_goals = df.groupby("Position")["Goals"].transform("mean")
# compare = df[df["Goals"] > avg_goals]
# print(compare)

# total_assist_by_club = df.groupby("Club")["Assists"].sum()
# print(total_assist_by_club)

# avg = df.groupby("Position")["PassAccuracy"].mean()
# print(avg)


# Set a clean style
sns.set(style="whitegrid")

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x="Goals", y="Name", data=df.sort_values(by="Goals"))
plt.title("Goals Scored by Players")
plt.xlabel("Goals")
plt.ylabel("Player")
plt.tight_layout()
plt.show()


# Group and reset index so we can plot
accuracy_by_pos = df.groupby("Position")["PassAccuracy"].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x="Position", y="PassAccuracy", data=accuracy_by_pos)
plt.title("Avg Pass Accuracy by Position")
plt.ylabel("Pass Accuracy (%)")
plt.tight_layout()
plt.show()
