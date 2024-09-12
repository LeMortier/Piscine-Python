import sys

import pandas as pd


def create_series() -> pd.Series:
  
    return pd.Series(list(map(int, sys.argv[1:])))


# --------------------
def series_operations(series: pd.Series) -> (int, float, float):
    
    return series.sum(), series.mean(), series.std()


# --------------------
def create_dataframe(product: list[str], quantity: list[int], total_price: list[float]) -> pd.DataFrame:
    
    return pd.DataFrame({
        'product': product,
        'quantity': quantity,
        'total_price': total_price
    })


# --------------------
def dataframe_accession(data: pd.DataFrame) -> tuple:
   
    return (data['product'].tolist(), data.iloc[1].to_dict(), data.iloc[3]['quantity'])