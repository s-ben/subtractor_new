import numpy as np


def room_sim(u):
    """
    Creates simulated room signal
    """
    
	# Generate received signal d(n) using randomly chosen coefficients
    coeffs = np.concatenate(([0.8], np.zeros(8), [-0.7], np.zeros(9),
                         [0.5], np.zeros(11), [-0.3], np.zeros(3),
                         [0.1], np.zeros(20), [-0.05]))
    d = np.convolve(u, coeffs)
    
    # Add background noise
    v = np.random.randn(len(d)) * np.sqrt(5000)
    d += v
	
    return d
