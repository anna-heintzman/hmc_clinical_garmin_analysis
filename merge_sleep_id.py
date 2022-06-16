from numpy import outer
import pandas as pd
import os

ids = pd.read_csv("../mapping_hmc_id_garmin.csv")
diagnoses = pd.read_csv("../hmc_clinical_/hmc_diag.csv")
sleep_stats = pd.read_csv("sleep_stats.csv")

merge1 = pd.merge(ids, diagnoses, on = "RecordID", how = "outer")
# print(merge1)

merge2 = pd.merge(merge1, sleep_stats, on = "garmin_guid", how = "outer")
print(merge2)

# merge2.to_csv("garmin_sleep_diag_id.csv", index = False)