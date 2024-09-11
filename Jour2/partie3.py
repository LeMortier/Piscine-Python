import sys

import pandas as pd


def create_series() -> pd.Series:
  
    return pd.Series(list(map(int, sys.argv[1:])))


# --------------------
def series_operations(series: pd.Series) -> (int, float, float):
    
    return series.sum(), series.mean(), series.std()


# --------------------
def create_dataframe(products: list[str], quantities: list[int], prices: list[float]) -> pd.DataFrame:
    
    return pd.DataFrame({
        'products': products,
        'quantities': quantities,
        'prices': prices
    })


# --------------------
def dataframe_accession(data: pd.DataFrame) -> tuple:
   
    return (data['products'].tolist(), data.iloc[1].to_dict(), data.iloc[3]['quantities'])