"""Provides functions used in performing ANOVA."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import kurtosis, skew


def experiment_groups(df_in, group_col, sample_size, seed):
    """Takes DataFrame, group label column, sample size, and random seed,
    returns DataFrame with groups based on group label column of given sample size."""
    #Randomly sample from each group and create dictionary of DataFrames
    d = {group: df_in[df_in[group_col] == group].sample(n=sample_size, random_state=seed)\
         for group in df_in[group_col].unique()}

    #Concatenate groups into one DataFrame and reset index
    df_out = pd.concat(df for _, df in d.items())
    df_out.reset_index(drop=True, inplace=True)
    return df_out


def qq_plots(d, ncols, nrows):
    """Takes a dictionary of values grouped by key, number of columns,
    and number of rows, returns Q-Q plots of standardized data grouped
    and labeled by key against a standard normal distribution.
    """
    fig, axes = plt.subplots(ncols=ncols, nrows=nrows, figsize=(ncols*3, nrows*3))
    for key, ax in zip(d, np.ravel(axes)):
        sm.qqplot(d[key], fit=True, line='45', ax=ax)
        ax.set_title(f'{key} QQ Plot')
    plt.tight_layout()
    return fig, axes


def skew_kurtosis(d):
    """Takes a dictionary, prints skew and kurtosis of
    data grouped and labeled by key.
    """
    for key in d:
        print(key + f' skew: {skew(d[key], bias=False)}')
        print(key + f' kurtosis: {kurtosis(d[key], fisher=False, bias=False)}')


def tukey(df, col, id_col):
    """Takes a DataFrame, column of interest, and id column
    returns the id column value of probable and possible outliers."""
    #Compute the IQR and inner and outer fences
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    inner_fence = 1.5 * iqr
    outer_fence = 3 * iqr

    #Compute inner fence lower and upper ends
    inner_fence_lower = q1 - inner_fence
    inner_fence_upper = q3 + inner_fence

    #Compute outer fence lower and upper ends
    outer_fence_lower = q1 - outer_fence
    outer_fence_upper = q3 + outer_fence

    #If value is an outlier, append the id to the appropriate outlier list
    outliers_prob = []
    outliers_poss = []
    for index, x in enumerate(df[col]):
        if x <= outer_fence_lower or x >= outer_fence_upper:
            outliers_prob.append(df.iloc[index][id_col])
        elif x <= inner_fence_lower or x >= inner_fence_upper:
            outliers_poss.append(df.iloc[index][id_col])
    return outliers_prob, outliers_poss


def anova_table(fit, title):
    """Takes a fitted statsmodels model and title, prints ANOVA table."""
    aov_table = sm.stats.anova_lm(fit, typ=3)
    print(title)
    print(aov_table)
    print()


def cohens_d(sample_a, sample_b):
    """Takes two sample arrays, returns Cohen's d."""
    diff = np.abs(np.mean(sample_a) - np.mean(sample_b))
    pooled_std = np.sqrt((np.std(sample_a)**2 + np.std(sample_b)**2)/2)
    result = diff/pooled_std
    return result


def standardized_resids(resids, sample_size):
    """Takes a set of residuals and sample size, computes standardized residuals."""
    resids_ss = np.sum(resids**2)
    resids_std = np.sqrt(resids_ss/(sample_size - 2))
    result = resids/resids_std
    return result
