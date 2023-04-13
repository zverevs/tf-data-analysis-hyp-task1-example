import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.stats.proportion import proportions_ztest

chat_id = 235789175 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    count = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])

    pval = proportions_ztest(count, nobs, alternative='larger')[1]
    alpha = 0.07
    if pval < alpha:
        return True
    else:
        return False
