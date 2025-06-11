from pymcdm.methods import TOPSIS
from data import matrix, weights, types

def run_topsis():
    topsis = TOPSIS()
    scores = topsis(matrix, weights, types)
    return scores