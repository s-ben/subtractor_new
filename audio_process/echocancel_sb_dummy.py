

import numpy as np
import matplotlib.pyplot as plt
import adaptfilt as adf
import scipy.io.wavfile
from scipy.io.wavfile import write

# import pyaudio
# from scipy.io.wavfile import read


# Get u(n) - this is available on github or pypi in the examples folder
# u = np.load('speech.npy')

# p = pyaudio.PyAudio()
# stream = p.open(format = p.get_format_from_width(2),
#                         channels = 1,
#                         rate = 44100,
#                         input = True,
#                         output = True,
#                         #stream_callback = self.callback
#                         )


# Import impulse response
rate_ir, ir_data = scipy.io.wavfile.read('living_room_2_PCM_Live.wav')
ir = ir_data.astype(np.float64)


	# Plot IR
# plt.figure()
# plt.title("Impulse Response")
# plt.plot(ir_data, label="Amplitude")
# plt.grid()
# plt.legend()
# plt.xlabel('samples')
# 
# plt.show()


# Import raw music file
rate, data = scipy.io.wavfile.read('GhostsNStuff_mono_4s.wav')

u = data.astype(np.float64)


# print data.dtype
# print u.dtype
# wf = wave.open("GhostsNStuff_mono_4s.wav", 'rb')




# Generate received signal d(n) using randomly chosen coefficients
# coeffs = np.concatenate(([0.8], np.zeros(8), [-0.7], np.zeros(9),
#                          [0.5], np.zeros(11), [-0.3], np.zeros(3),
#                          [0.1], np.zeros(20), [-0.05]))

coeffs = ir

print 'convolving IR'

d = np.convolve(u, coeffs)

# scaled_d = np.int16(d/np.max(np.abs(d)) * 32767)
# write('Ghosts_echoed_RIR.wav', 44100, scaled_d)


# Add background noise
v = np.random.randn(len(d)) * np.sqrt(5000)
d += v

scaled_d = np.int16(d/np.max(np.abs(d)) * 32767)
write('Ghosts_echoed_RIR_noise.wav', 44100, scaled_d)

# print type(d)
# print d.dtype

print 'applying adaptive filt'
# Apply adaptive filter
M = 8000 #100  # Number of filter taps in adaptive filter
step = 0.1  # Step size
y, e, w = adf.nlms(u, d, M, step, returnCoeffs=True)

 
frame_size = 1000	# window size in samples
num_frames = len(e)/frame_size
print num_frames

mse = []
erle = []

for fr in range(num_frames):
	x = d[fr*frame_size:((fr+1)*frame_size-1)]  # Slice to get view of M latest samples of "recorded" signal
	err = e[fr*frame_size:((fr+1)*frame_size-1)]   # Slice to get view of M latest samples of error signal

	err_2 = np.mean(np.square(err))
	x_2 = np.mean(np.square(x))
	
	mse_x = 10*np.log10(err_2)
	erle_fr = 10*np.log10(x_2/err_2)
	
	# Calculate Mean Square Error (MSE) of error signal
	mse.append(mse_x)
	erle.append(erle_fr)
	
	
	# 	print np.mean(err_2)
	# 	print fr
	
# 	for 
	# Plot RERLE
plt.figure()
plt.title("ERLE")
plt.plot(erle, label="ERLE (dB)")
plt.grid()
plt.legend()
plt.xlabel('frames')

# plt.show()


	# Plot MSE
plt.figure()
plt.title("MSE")
plt.plot(mse, label="MSE dB")
plt.grid()
plt.legend()
plt.xlabel('frames')

plt.show()
# 
# 	raw_input("Press Enter to continue...")


	# Plot speech signals
# 	plt.figure()
# 	plt.title("Error signal")
# 	plt.plot(err, label="Music signal, u(n)")
# 	plt.plot(err_2, label="Music signal ^2, u(n)")
# 	plt.grid()
# 	plt.legend()
# 	plt.xlabel('Samples')
# 
# 	plt.show()
# 
# 	raw_input("Press Enter to continue...")
	



# Perform filtering
# for n in xrange(len(e)):
#  	
#      x = np.flipud(d[n:n+M])  # Slice to get view of M latest samples of "recorded" signal
#      err = np.flipud(e[n:n+M])  # Slice to get view of M latest samples of "recorded" signal
#      
#      
#      
#      y[n] = np.dot(x, w)
#      e[n] = d[n+M-1] - y[n]
#  
#      normFactor = 1./(np.dot(x, x) + eps)
#      w = leakstep * w + step * normFactor * x * e[n]
#      y[n] = np.dot(x, w)
#      if returnCoeffs:
#          W[n] = w




scaled_e = np.int16(e/np.max(np.abs(e)) * 32767)
write('Ghosts_subtracted_RIR.wav', 44100, scaled_e)

# Calculate mean square weight error
mswe = adf.mswe(w, coeffs)

# Plot speech signals
plt.figure()
plt.title("Speech signals")
plt.plot(u, label="Music signal, u(n)")
plt.plot(d, label="Echo'd music signal, d(n)")
plt.grid()
plt.legend()
plt.xlabel('Samples')
# 
# plt.draw()

# Plot error signal - note how the measurement noise affects the error
plt.figure()
plt.title('Error signal e(n)')
plt.plot(e)
plt.grid()
plt.xlabel('Samples')

# Plot mean squared weight error - note that the measurement noise causes the
# error the increase at some points when Emily isn't speaking
plt.figure()
plt.title('Mean squared weight error')
plt.plot(mswe)
plt.grid()
plt.xlabel('Samples')

# Plot final coefficients versus real coefficients
plt.figure()
plt.title('Real coefficients vs. estimated coefficients')
plt.plot(w[-1], 'g', label='Estimated coefficients')
plt.plot(coeffs, 'b--', label='Real coefficients')
plt.grid()
plt.legend()
plt.xlabel('Samples')

plt.show()
