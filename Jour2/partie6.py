import pandas as pd


def pandas_json_read(file: str) -> pd.DataFrame:
   
    return pd.read_json(file)


def pandas_json_write(file: str, data: pd.DataFrame):
   
    data.to_json(file, indent=4, orient="records")
    