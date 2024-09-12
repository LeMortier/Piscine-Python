import pandas as pd


def pandas_excel_read(file: str, sheet: str) -> pd.DataFrame:
    
    return pd.read_excel(file, sheet_name=sheet)


# --------------------
def pandas_excel_write(data: pd.DataFrame, filename: str):
    # ExcelWriter avec le mode 'append' pour ne pas effacer les autres feuilles
    with pd.ExcelWriter(filename, mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
        data.to_excel(writer, sheet_name="orders", index=False)

#pd.excel writer
# --------------------
def pandas_excel_selective_read(filename: str) -> pd.DataFrame:
   
    data = pd.read_excel(filename, sheet_name="orders").iloc[11:][['product', 'total_price']]
    return data.drop_duplicates(subset=['product'])


# --------------------
def pandas_excel_manipulation(filename: str):
    
    data = pd.read_excel(filename, sheet_name="orders")
    summary = data.groupby(['product']).agg(
        total_orders=('product', 'size'),
        total_quantity=('quantity', 'sum')
    )
    summary['mean_quantity_per_order'] = (summary['total_quantity'] / summary['total_orders']).round(2)
    summary.reset_index(inplace=True)
    with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        summary.to_excel(writer, sheet_name='summary', index=False)
        