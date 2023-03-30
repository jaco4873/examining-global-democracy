import pwd
import pandas as pd

pwd

freedomhouse = pd.read_csv(
    "https://raw.githubusercontent.com/dirty-cat/datasets/master/data/Happiness_report_2022.csv",
    thousands=",",
)
