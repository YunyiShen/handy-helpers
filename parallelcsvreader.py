import pandas as pd
import glob
from concurrent.futures import ThreadPoolExecutor
import os
def read_one_csv(path):
    return pd.read_csv(path)
def read_all_csvs_parallel(directory, pattern="*.csv", max_workers=8):
    files = glob.glob(os.path.join(directory, pattern))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        dfs = list(executor.map(read_one_csv, files))
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df
