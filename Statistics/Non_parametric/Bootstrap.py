import numpy as np
import pandas as pd

# Estimate the SE
# Improve the point estimation
# Estimate the confidence interval


# Bootstrap main method
def bootstrap(data, rpt, cl, func_dict):  # data, repeat times, confidence level, function name
    out_df = pd.DataFrame(columns=['Statistics', 'SE', 'Improved_PE', f'{cl}_IE'])
    for i, j in func_dict.items():
        ori_stat = j(data)
        bs_stats = bs_stat_cal(data, rpt, j)
        diff = bs_stats - ori_stat
        se_e = np.std(bs_stats, ddof=1)  # SE Estimation
        stat_r = 2 * ori_stat - np.mean(bs_stats)  # Point Estimation Revision
        conf_int = ori_stat - np.percentile(diff, [50 * (1 + cl), 50 * (1 - cl)])  # Interval Estimation
        print(f'For statistic {i}', f'SE, improved point estimation and {cl} confidence interval are:',
              tuple([se_e, stat_r, tuple(conf_int)]))
        out_df.loc[len(out_df)] = [i, se_e, stat_r, tuple(conf_int)]
    return out_df


# Sample and calculation for 1 time
def bs_sample(data, func):  # data, function name
    sample = np.random.choice(data, len(data))
    return func(sample)


# Calculate the statistics for enough times
def bs_stat_cal(data, rpt, func):  # data, repeat times, function name
    sample_stat = []
    for i in range(rpt):
        sample_stat.append(bs_sample(data, func))
    return np.array(sample_stat)


# Use np.mean, np.median and s_std for Mean, Median and Sample Std
def s_std(data):
    std = np.std(data, ddof=1)
    return std


funcs = {'Mean': np.mean, 'Median': np.median, 'Std': s_std}
