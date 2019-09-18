import pandas as pd


def filter_best(df, to_predict, predictors, metric, objective='min'):
    keep_list = to_predict + predictors + [metric]
    if objective == 'min':
        df = df.loc[df.groupby(predictors)[metric].idxmin()]
    else:
        df = df.loc[df.groupby(predictors)[metric].idxmax()]
    drop_list = list(set(df.columns)-set(keep_list))
    df = df.drop(drop_list, axis=1)
    return df