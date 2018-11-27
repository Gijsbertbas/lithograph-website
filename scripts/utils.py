
import welly
import numpy as np


def las2df(fname):
    w = welly.Well.from_las(fname)
    df = w.df()
    df['DEPT'] = df.index
    return df


def minmax_idx(logs_df, tracks):
    imin = 0
    imax = logs_df.shape[0]-1

    for itrack in tracks:
        vals = logs_df[itrack].values
        idx = np.where(np.isnan(vals) == False)[0]
        imin = max(imin, idx.min())
        imax = min(imax, idx.max())

    return imin, imax


def minmax_depth(logs_df, tracks):
    #imax, imin = minmax_idx(logs_df, tracks)
    imin, imax = minmax_idx(logs_df, tracks)
    return logs_df.index[imin], logs_df.index[imax]

def label2category(data):
    for j in range(data.shape[1]):
        u = np.unique(data[:, j])
        d = {}
        if isinstance(u[0], str):
            for i, v in enumerate(u):
                d[v] = i

            data[:, j] = np.vectorize(d.get)(data[:, j])

    return data


def fill_intervales(data0):
    data = np.copy(data0)

    for j in range(data.shape[1]):
        prev = -1
        for i in range(data.shape[0]):
            if data[i, j] != -1:
                prev = data[i, j]
            else:
                data[i, j] = prev

    return data


def scale(logs_df, tracks):
    for col in tracks:
        logs_df[col] = preprocessing.scale(logs_df[col])
    return logs_df

def reducedf(df,mi,ma):
    return df[(df['DEPT'] >= mi) & (df['DEPT'] <= ma)]
