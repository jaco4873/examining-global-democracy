import pandas as pd
import numpy as np
from dirty_cat import fuzzy_join

# We will ignore the warnings:
import warnings

# Load Data
freedomhouse = pd.read_csv('data/freedomhouse.csv')
worlddatabank_clean_long = pd.read_csv("data/worlddatabank_clean_long.csv")

# Join by Fuzzy Join
warnings.filterwarnings("ignore")

merged_data = fuzzy_join(
    worlddatabank_clean_long,  # our table to join
    freedomhouse,  # the table to join with
    left_on="country",  # the first join key column
    right_on="country",  # the second join key column
    return_score=True,
)

# Inspect with Numpy
def print_worst_matches(joined_table, n=5):
    """Prints n worst matches for inspection."""
    max_ind = np.argsort(joined_table["matching_score"], axis=0)[:n]
    max_dist = pd.Series(
        joined_table["matching_score"][max_ind.ravel()].ravel(),
        index=max_ind.ravel(),
    )
    worst_matches = joined_table.iloc[list(max_ind.ravel())]
    worst_matches = worst_matches.assign(matching_score=max_dist)
    return worst_matches

merged_data.to_csv('fuzzy_merge_data.csv', index=True)