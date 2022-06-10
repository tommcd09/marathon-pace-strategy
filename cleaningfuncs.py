"""Provides various functions for data cleaning."""

import numpy as np
import pandas as pd
import pycountry


def percent_missing(df):
    """Takes a DataFrame, prints percentage of data missing for each column,
    rounded to 2 decimal places.
    """
    for col in df.columns:
        pct_missing = np.round((np.mean(df[col].isnull()) * 100), decimals = 2)
        print(f'{col} - {pct_missing}%')


def timedelta_to_hours(array):
    """Takes an array of timedeltas, converts to hours."""
    array = array.values/np.timedelta64(1, 'h')
    return array


def convert_types(df, numeric_cols, time_cols):
    """Takes lists of numeric and time columns and a DataFrame, converts
    columns of DataFrame to type int, filling blank numeric columns with 0.
    """
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce', axis=1).fillna(0)
    df[numeric_cols] = df[numeric_cols].astype('int')
    df[time_cols] = df[time_cols].apply(pd.to_timedelta, unit='s', errors='coerce')
    df[time_cols] = df[time_cols].apply(timedelta_to_hours)


def name_split(df):
    """Takes a DataFrame with name columns, splits name column into
    last_name, first_name, and country columns and drops original name column.
    """
    #Split the name column into 'country', 'last_name', and 'first_name'
    df[['name', 'country']] = df['name'].str.split(r'\s\((?=[A-Z]{3})', 1, expand=True)
    df[['last_name', 'first_name']] = df['name'].str.split(', ', 1, expand=True)

    #Strip the trailing parenthesis from 'country'
    df['country'] = df['country'].str.strip(')')

    #Drop the old 'name' column
    df.drop(['name'], axis=1, inplace=True)


def country_convert(df):
    """Takes a DataFrame, returns country name if code
    matches ISO 3166 country code, otherwise returns 'NA'.
    """
    country_list = [country.alpha_3 for country in list(pycountry.countries)]
    if (len(df['country']) == 3 and df['country'] in country_list):
        return pycountry.countries.get(alpha_3 = df['country']).name
    return 'NA'


def compute_split_diff(df):
    """Takes a DataFrame with finish and first half split times,
    computes second half split time and split difference as percentage of finish time.
    """
    df['second_half'] = df['finish'].values - df['first_half'].values
    df['split_diff'] = (df['second_half'].values
                        - df['first_half'].values)*100/df['finish'].values
