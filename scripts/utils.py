
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
    imin, imax = minmax_idx(logs_df, tracks)
    return logs_df.index[imin], logs_df.index[imax]
