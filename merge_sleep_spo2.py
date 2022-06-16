import pandas as pd
import os

# file_paths = {}
# for root, dirs, files in os.walk("."):
#    for f in files:
#        if f.endswith(".csv"):
#            if f not in file_paths:
#                file_paths[f] = []
#            file_paths[f].append(root)

# for f, paths in file_paths.items():
#    txt = []
#    for p in paths:
#        with open(os.path.merge(p, f, on = "timestamp", how = "outer")) as f2:
#            txt.append(f2.read())
#    with open(f, 'w') as f3:
#        f3.write("sleep_spo2".merge(txt))

def get_filenames():
    filenames = []
    for filename in os.listdir("sleep_&_blood_oxygenation"):
        filenames.append(filename[:-5])
    return filenames

filenames = get_filenames()
   
part_filenames = []
for filename in filenames:
    parts = []
    for part_name in os.listdir("./ners"):
        if part_name.startswith(filename+"_"):
            parts.append(part_name)