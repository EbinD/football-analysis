import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# df = pd.read_csv("players.csv")

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
# sns.set(style="whitegrid")

# Plot
# plt.figure(figsize=(10, 6))
# sns.barplot(x="Goals", y="Name", data=df.sort_values(by="Goals"))
# plt.title("Goals Scored by Players")
# plt.xlabel("Goals")
# plt.ylabel("Player")
# plt.tight_layout()
# # plt.show()


# Group and reset index so we can plot
# accuracy_by_pos = df.groupby("Position")["PassAccuracy"].mean().reset_index()

# plt.figure(figsize=(8, 5))
# sns.barplot(x="Position", y="PassAccuracy", data=accuracy_by_pos)
# plt.title("Avg Pass Accuracy by Position")
# plt.ylabel("Pass Accuracy (%)")
# plt.tight_layout()
# plt.show()

# Load raw player data (real-world messy version)
raw_df = pd.read_csv("raw_player.csv")
# print(raw_df)

# print("Shape:", raw_df.shape)
# print("Columns:\n", raw_df.columns.tolist())
# print("Data types:\n", raw_df.dtypes)
# print("Missing values:\n", raw_df.isnull(
# ).sum().sort_values(ascending=False).head(20))

# 1. Count fully missing columns
# fully_missing = raw_df.columns[raw_df.isnull().all()].tolist()
# print(f"❌ Fully missing columns ({len(fully_missing)}):")
# print(fully_missing)

# 2. Show top 30 columns by missing values
# missing_vals = raw_df.isnull().sum().sort_values(ascending=False)
# print("\n🔍 Top 30 columns with most missing values:")
# print(missing_vals.head(30))

# 3. Count non-null columns (i.e. useful columns)
# non_null_cols = raw_df.columns[raw_df.notnull().any()].tolist()
# print(f"\n✅ Columns with at least some data: {len(non_null_cols)}")


def print_top_level(path):
    print(f"{os.path.basename(path)}/")
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"    {item}/")
        else:
            print(f"    {item}")


print_top_level("C:/Users/solly/Desktop/football-analysis")
