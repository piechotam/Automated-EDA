import pandas as pd

def data_summary(df: pd.DataFrame) -> dict:
    summary = {
        "Shape": df.shape,
        "Data Types": df.dtypes.to_dict(),
        "Missing Values": df.isnull().sum().to_dict(),
        "Statistics": df.describe().to_dict()
    }
    return summary

def detect_column_types(df: pd.DataFrame, categorical_threshold: int = 10) -> dict:
    categorical_cols, numeric_cols, datetime_cols, other = [], [], [], []
    
    for col_name in df.columns:
        column = df[col_name]
        number_of_unique_values = len(column.unique())

        if number_of_unique_values <= categorical_threshold:
            categorical_cols.append(col_name)
        elif pd.api.types.is_numeric_dtype(column):
            numeric_cols.append(col_name)
        elif pd.api.types.is_datetime64_dtype(column):
            datetime_cols.append(col_name)
        elif pd.api.types.is_object_dtype(column):
            try:
                pd.to_datetime(column, errors='raise', format=None)
                datetime_cols.append(col_name)
                continue
            except:
                pass
        else:
            other.append(col_name)

    return {"categorical": categorical_cols,
            "numeric": numeric_cols,
            "datetime": datetime_cols,
            "other": other}