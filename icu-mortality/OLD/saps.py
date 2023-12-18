# Compute SAPS-1 Score
#
# History
#  - 12/7/2023, created python version from original saps_score.c, jpb
#  - 3/22/2012, saps_score.c created by G. Moody
#

import pandas as pd
import numpy as np

INVALID = -1
# MISSING = 200

def score_age(age):
    if   (age > 200): return INVALID
    elif (age >  75): return 4
    elif (age >  65): return 3
    elif (age >  55): return 2
    elif (age >  45): return 1
    elif (age >=  0): return 0
    else:             assert False

def score_hr(hr):
    if   (hr >  250): return INVALID
    elif (hr >= 180): return 4
    elif (hr >= 140): return 3
    elif (hr >= 110): return 2
    elif (hr >=  70): return 0
    elif (hr >=  55): return 2
    elif (hr >=  40): return 3
    elif (hr >=  10): return 4
    elif (hr >=   0): return INVALID
    else:             assert False

def score_sbp(sbp):
    if      (sbp >  300): return INVALID
    elif (sbp >= 190): return 4
    elif (sbp >= 150): return 2
    elif (sbp >=  80): return 0
    elif (sbp >=  55): return 2
    elif (sbp >=  20): return 4
    elif (sbp >=   0): return INVALID
    else:                assert False

def score_temp(temp):
    if      (temp >  45): return INVALID
    elif (temp >= 41): return 4
    elif (temp >= 39): return 3
    elif (temp >= 38.5): return 2
    elif (temp >= 36): return 0
    elif (temp >= 34): return 1
    elif (temp >= 32): return 2
    elif (temp >= 30): return 3
    elif (temp >= 15): return 4
    elif (temp >=  0): return INVALID
    else:		 assert False

def score_resp(resp):
    if      (resp >  80): return INVALID
    elif (resp >= 50): return 4
    elif (resp >= 35): return 3
    elif (resp >= 25): return 1
    elif (resp >= 12): return 0
    elif (resp >= 10): return 1
    elif (resp >=  6): return 2
    elif (resp >=  2): return 4
    elif (resp >=  0): return INVALID
    else:	 	 assert False

def score_ur(ur):
    if      (ur > 20.0): return INVALID
    elif (ur >= 5.0): return 2
    elif (ur >= 3.5): return 1
    elif (ur >= 0.7): return 0
    elif (ur >= 0.5): return 2
    elif (ur >= 0.2): return 3
    elif (ur >=   0): return 4
    else:	        assert False

def score_bun(bun):
    bun = bun / 2.8
    if      (bun >  100): return INVALID
    elif (bun >=  55): return 4
    elif (bun >=  36): return 3
    elif (bun >=  29): return 2
    elif (bun >= 7.5): return 1
    elif (bun >= 3.5): return 0
    elif (bun >=   1): return 1
    elif (bun >=   0): return INVALID
    else:	 	 assert False

def score_hct(hct):
    if      (hct >  80): return INVALID
    elif (hct >= 60): return 4
    elif (hct >= 50): return 2
    elif (hct >= 46): return 1
    elif (hct >= 30): return 0
    elif (hct >= 20): return 2
    elif (hct >=  5): return 4
    elif (hct >=  0): return INVALID
    else:	 	assert False

def score_wbc(wbc):
    if      (wbc > 200): return INVALID
    elif (wbc >= 40): return 4
    elif (wbc >= 20): return 2
    elif (wbc >= 15): return 1
    elif (wbc >=  3): return 0
    elif (wbc >=  1): return 2
    elif (wbc >=0.1): return 4
    elif (wbc >=  0): return INVALID
    else:	        assert False

def score_glu(glu):
    glu = glu / 18
    if      (glu >  1000): return INVALID
    elif (glu >= 44.5): return 4
    elif (glu >= 27.8): return 3
    elif (glu >= 14.0): return 1
    elif (glu >=  3.9): return 0
    elif (glu >=  2.8): return 2
    elif (glu >=  1.6): return 3
    elif (glu >=  0.5): return 4
    elif (glu >=    0): return INVALID
    else:	  	  assert False

def score_k(k):
    if      (k >   20): return INVALID
    elif (k >= 7.0): return 4
    elif (k >= 6.0): return 3
    elif (k >= 5.5): return 2
    elif (k >= 3.5): return 0
    elif (k >= 3.0): return 1
    elif (k >= 2.5): return 2
    elif (k >= 0.5): return 4
    elif (k >=   0): return INVALID
    else:	       assert False

def score_na(na):
    if      (na >  200): return INVALID
    elif (na >= 180): return 4
    elif (na >= 161): return 3
    elif (na >= 156): return 2
    elif (na >= 151): return 1
    elif (na >= 130): return 0
    elif (na >= 120): return 2
    elif (na >= 110): return 3
    elif (na >=  50): return 4
    elif (na >=  0): return INVALID
    else:	 	assert False

def score_hco3(hco3):
    if      (hco3 > 100): return INVALID
    elif (hco3 >= 40): return 4
    elif (hco3 >= 30): return 1
    elif (hco3 >= 20): return 0
    elif (hco3 >= 10): return 1
    elif (hco3 >=  5): return 2
    elif (hco3 >=  2): return 4
    elif (hco3 >=  0): return INVALID
    else:	 	 assert False

def score_gcs(gcs):
    if      (gcs >  15): return INVALID
    elif (gcs >= 13): return 0
    elif (gcs >= 10): return 1
    elif (gcs >=  7): return 2
    elif (gcs >=  4): return 3
    elif (gcs >=  3): return 4
    elif (gcs >=  0): return INVALID
    else:	 	assert False

map_score = {
    'Age':      ['1', score_age],
    'HR':       ['mm', score_hr],
    'SBP':      ['mm', score_sbp],
    'Temp':     ['mm', score_temp],
    'RespRate': ['mm', score_resp],
    #MechVent
    #'Urine':   ['mm', score_ur],
    'BUN':     ['mm', score_bun],
    'HCT':     ['mm', score_hct],
    'WBC':     ['mm', score_wbc],
    'Glucose': ['mm', score_glu],
    'K':       ['mm', score_k],
    'Na':      ['mm', score_na],
    'HCO3':    ['mm', score_hco3],
    'GCS':     ['mm', score_gcs],
    }

def saps_score_v1(df):
    dfr = df.copy()

    dfr['score'] = np.nan
    dfr['valid'] = -1

    m = (dfr.Parameter == 'SysABP') | (dfr.Parameter == 'NISysABP')
    dfr.loc[m, 'Parameter'] = 'SBP'

    m = (dfr.Parameter == 'MechVent')
    dfr.loc[m, 'Parameter'] = 'RespRate'
    dfr.loc[m, 'Value']     = 49

    urine_sum = (dfr.query("Parameter == 'Urine'")
                    .groupby('record_id')
                    .agg(
                        Time  = ('Time', 'min'),
                        Value = ('Value', 'sum') )
                    .reset_index() )
    urine_sum['Parameter'] = 'UrineSum'
    urine_sum['Value']     = urine_sum['Value'] / 1000
    urine_sum['score']     = urine_sum.Value.map(score_ur)
    urine_sum['valid']     = (urine_sum.Value <= 20).astype(int)

    cols = map_score.keys()
    for col in cols:
        _, score_func = map_score[col]

        m = dfr.Parameter == col
        dfr.loc[m, 'score']   =  dfr.loc[m, 'Value'].map(score_func)
        dfr.loc[m, 'valid'] = (dfr.loc[m, 'score'] >= 0).astype(int)

    dfr = pd.concat([dfr, urine_sum], axis=0)

    return dfr



def saps_score_pivot(df):
    res = []

    res.append(pd.DataFrame({'record_id': df.record_id}))

    for col in ['Age', 'HR', 'Glucose']:
        tp, score_func = map_score[col]
        if tp == '1':
            res.append(pd.DataFrame(
                {col: df[f'{col}_min'].map(score_func)} ))
        elif tp == 'mm':
            t = pd.DataFrame(
                dict(
                    col_min = df[f'{col}_min'].map(score_func),
                    col_max = df[f'{col}_max'].map(score_func),
                ) )
            res.append(pd.DataFrame(
                {col: t.max(axis=1) } ))

    return pd.concat(res, axis=1)
               
