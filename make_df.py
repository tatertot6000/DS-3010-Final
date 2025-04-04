import pandas as pd
from datasets import load_from_disk
from consts import DATADIR, NAME, SUBSET

def make_df(partition: str) -> pd.DataFrame:
    ds = load_from_disk(f'{DATADIR}/{NAME}-{SUBSET}-{partition}')
    df = ds.to_pandas()
    # print(df.head())
    return df