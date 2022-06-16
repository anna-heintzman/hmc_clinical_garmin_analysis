import pandas as pd
import os
import numpy as np

list_of_csvs = os.listdir("sleep")

user_guids = []
user_means = []
user_medians = []

for csv_file in list_of_csvs:

    if csv_file == ".gitkeep":
        continue

    df = pd.read_csv("sleep/" + csv_file)

    csv_file.replace("3", "")

    mean_sleep = df["level"].mean()
    median_sleep = df["level"].median()

    user_guids.append(csv_file.replace(".csv", ""))
    user_means.append(mean_sleep)
    user_medians.append(median_sleep)

df_final = pd.DataFrame(
    {
        "garmin_guid": user_guids,
        "mean_sleep_level": user_means,
        "median_sleep_level": user_medians,
    }
)
print(df_final)

df_final.to_csv("sleep_stats.csv", index = False)

