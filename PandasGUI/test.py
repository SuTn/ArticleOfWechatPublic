import pandas as pd
from pandasgui import show
df = pd.read_csv("train.csv")
show(df, settings={'block': True})