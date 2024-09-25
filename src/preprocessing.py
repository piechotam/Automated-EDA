import pandas as pd

def fill_missing_data(df: pd.DataFrame, columns: list, method: str = 'median') -> pd.DataFrame:
    for column in columns:
        if method == 'mean':
            df[column] = df[column].fillna(df[column].mean())
        elif method == 'median':
            df[column] = df[column].fillna(df[column].median())
        elif method == 'mode':
            mode_val = df[column].mode().iloc[0]
            df[column] = df[column].fillna(mode_val)
    
    return df

def one_hot_encode(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    df = pd.get_dummies(df, columns=columns, prefix=columns, drop_first=False)
    
    return df

def replace_outliers(df: pd.DataFrame, columns: list, factor: float = 1.5) -> pd.DataFrame:
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - (factor * IQR)
        upper_bound = Q3 + (factor * IQR)

        df[col] = df[col].apply(lambda x: lower_bound if x < lower_bound else upper_bound if x > upper_bound else x)

    return df