import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 819168380

def solution(x: np.array, y: np.array) -> bool:
    p_value = ks_2samp(x, y).pvalue
    return p_value < 0.03
