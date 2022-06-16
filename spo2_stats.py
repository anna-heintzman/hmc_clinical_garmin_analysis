import os
from statistics import mean
import numpy as np
import pandas as pd

list_of_csvs = os.listdir("blood_oxygenation")

user_guids = []
user_means = []
user_medians = []
user_mins = []
user_maxs = []

for csv_file in list_of_csvs:

    if csv_file == ".gitkeep":
        continue

    df = pd.read_csv("blood_oxygenation/" + csv_file)

    mean_spo2 = df["spo2"].mean()
    median_spo2 = df["spo2"].median()
    min_spo2 = df["spo2"].min()
    max_spo2 = df["spo2"].max()

    user_guids.append(csv_file.replace(".csv", ""))
    user_means.append(mean_spo2)
    user_medians.append(median_spo2)
    user_mins.append(min_spo2)
    user_maxs.append(max_spo2)


df_final = pd.DataFrame(
    {
        "garmin_guid": user_guids,
        "mean_spo2": user_means,
        "median_spo2": user_medians,
        "minimum_spo2": user_mins,
        "maximum_spo2": user_maxs,
    }
)
print(df_final)

df_final.to_csv("spo2_stats.csv", index = False)

# import pdb; pdb.set_trace()