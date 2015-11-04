import numpy as np


def nlms(u):
    """
    Creates simulated room signal
    """
    
Generate received signal d(n) using randomly chosen coefficients
	coeffs = np.concatenate(([0.8], np.zeros(8), [-0.7], np.zeros(9),
                         [0.5], np.zeros(11), [-0.3], np.zeros(3),
                         [0.1], np.zeros(20), [-0.05]))
    d = np.convolve(u, coeffs)
    
    # Add background noise
	v = np.random.randn(len(d)) * np.sqrt(5000)
	d += v
	
	scaled_d = np.int16(d/np.max(np.abs(d)) * 32767)
	write('Ghosts_echoed_RIR_noise_from_views.wav', 44100, scaled_d)
    

#     return y, e, w
