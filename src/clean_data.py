import numpy as np
import pandas as pd



def normalize_column_names(dataframe):
    # convert column names to lowercase and strip whitespace
    dataframe.columns = dataframe.columns.str.lower().str.strip()

    return dataframe

def normalize_text(dataframe):
    # convert values of type object to lowercase and strip whitespace
    for col in dataframe.select_dtypes(["object","category"]).columns:
        dataframe[col] = dataframe[col].str.lower().str.strip()

    return dataframe


def clean_age(dataframe):
    # replace invalid ages with NaN
    dataframe.loc[ (dataframe["age"] > 18) | (dataframe["age"] < 15),"age"] = np.nan

    # fill the NaN values with the median age
    dataframe["age"] = dataframe["age"].fillna(dataframe["age"].median())

    #convert the type back to int if filling NaN values
    dataframe["age"] = dataframe["age"].astype("int")

    return dataframe

def clean_sex(dataframe):
    # replace words with abbreviations
    dataframe.loc[dataframe["sex"] == "male", "sex"] = "m"
    dataframe.loc[dataframe["sex"] == "female", "sex"] = "f"

    # replace invalid sex abbreviations with NaN
    dataframe.loc[ ~dataframe["sex"].isin( ["m","f"] ) ,"sex"] = np.nan

    # fill the NaN values with the sex mode
    dataframe["sex"] = dataframe["sex"].fillna(dataframe["sex"].mode()[0])

    return dataframe

def clean_bool_columns(dataframe):

    # store the columns that have yes or no values to convert them to booleans
    bool_cols = []

    for col in dataframe.columns:
        # check if the values are in (yes and no) after dropping the NaN values and then convert them to a set
        if set( dataframe[col].dropna().unique() ).issubset({"yes", "no"}):
            bool_cols.append(col)

    # replace values with True if the condition is correct and false if not
    dataframe[bool_cols] = dataframe[bool_cols] == "yes"

    return dataframe

def handle_missing_values(dataframe):
    # fill missing numeric values with the median of that column
    for col in dataframe.select_dtypes(include="number"):
        dataframe[col] = dataframe[col].fillna(dataframe[col].median())

    # fill missing text values with the mode of that column
    for col in dataframe.select_dtypes(include=["object","category"]):
        dataframe[col] = dataframe[col].fillna(dataframe[col].mode()[0])

    return dataframe


def clean_data(dataframe):
    df = dataframe.copy()
    df = normalize_column_names(df)
    df = normalize_text(df)
    df = clean_age(df)
    df = clean_sex(df)
    df = clean_bool_columns(df)
    df = handle_missing_values(df)
    df = df.drop_duplicates().reset_index(drop=True)
    return df