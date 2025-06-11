from pymcdm.methods import SPOTIS
from data import matrix, weights, types
import numpy as np

def run_spotis():
    # Obliczamy dolne i górne granice dla każdego kryterium
    bounds = np.array([
        [np.min(matrix[:, i]), np.max(matrix[:, i])]
        for i in range(matrix.shape[1])
    ])

    # Tworzymy obiekt SPOTIS z podanymi bounds
    spotis = SPOTIS(bounds)
    scores = spotis(matrix, weights, types)
    return scores