import pandas as pd
from topsis_analysis import run_topsis
from spotis_analysis import run_spotis

def compare_methods():
    topsis_scores = run_topsis()
    spotis_scores = run_spotis()
    alternatives = [f'A{i+1}' for i in range(len(topsis_scores))]

    df = pd.DataFrame({
        'Alternative': alternatives,
        'TOPSIS': topsis_scores,
        'SPOTIS': spotis_scores
    })

    df['TOPSIS_Rank'] = df['TOPSIS'].rank(ascending=False)
    df['SPOTIS_Rank'] = df['SPOTIS'].rank(ascending=True)

    return df