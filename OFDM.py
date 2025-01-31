import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_subcarriers = 50  # Number of subcarriers
sub_bandwidth = 100e6  # Bandwidth of each sub-band (100 MHz)
total_bandwidth = num_subcarriers * sub_bandwidth
sampling_rate = total_bandwidth
carrier_frequency = 5e9  # 5 GHz
transmit_power_dbm = 0  # 0 dBm
transmit_power_linear = 10**(transmit_power_dbm / 10) / 1000  # Linear scale in Watts
num_samples = 50  # Number of samples

# Time vector
time = np.arange(num_samples) / sampling_rate

# Bit stream and QPSK Mapping
bit_stream = "01100011111111110000000001100001111111111000000000"
qpsk_mapping = {
    "00": 1+1j,
    "01": 1-1j,
    "10": -1+1j,
    "11": -1-1j
}
data_symbols = [qpsk_mapping[bit_stream[i:i+2]] for i in range(0, len(bit_stream), 2)]
data_symbols = np.array(data_symbols)

# Upsample to match the number of subcarriers
data_symbols = np.tile(data_symbols, num_subcarriers // len(data_symbols))

# Serial to parallel conversion
parallel_data = np.zeros(num_subcarriers, dtype=complex)
for i, symbol in enumerate(data_symbols):
    parallel_data[i] = symbol

print("Parallel Data: ",parallel_data)
plt.figure(figsize=(10, 5))
plt.title("Parallel Data")
# bit_time = np.repeat(np.arange(len(parall)), 2)[:len(bit_stream)]
# bit_values = np.array([int(b) for b in bit_stream])
plt.plot(parallel_data.real, color='blue')
plt.plot(parallel_data.imag, color='green')
plt.xlabel("Bit Index")
plt.grid()
plt.show()

# OFDM Modulation using IFFT
ofdm_signal = np.fft.ifft(parallel_data, n=num_samples) * np.sqrt(num_samples)
# The inverse fast fourier transform is done at this stage.
# Steps after this: 
# 1. Parallel To Serial Converter
# 2. Transmit via the Channel
# 3. Receive via SDR
# 4. Serial to parallel conversion
# 5. FFT
# 6. Parallel To serial conversion
# 7. Output Data


# Normalize power
ofdm_signal *= np.sqrt(transmit_power_linear / np.mean(np.abs(ofdm_signal)**2))

# Parallel to Serial Conversion
transmitted_signal = ofdm_signal.flatten()

# ----- Receiver Side Signal -----
# Add noise (optional, for testing SNR)
noise_power = transmit_power_linear / 10  # Example: SNR of 10 dB
noise = np.sqrt(noise_power / 2) * (np.random.randn(num_samples) + 1j * np.random.randn(num_samples))
# received_signal = transmitted_signal + noise
received_signal = transmitted_signal 
# Serial to Parallel Conversion
received_ofdm_signal = received_signal.reshape((num_samples//num_subcarriers, num_subcarriers ))

# OFDM Demodulation using FFT and Parallel Data
received_parallel_data = np.fft.fft(received_ofdm_signal, n=num_samples) / np.sqrt(num_samples)
# received_symbols = received_parallel_data[:num_subcarriers]

# # Frequency domain representation
# ofdm_spectrum = np.fft.fft(ofdm_signal)
# frequencies = np.fft.fftfreq(num_samples, d=1/sampling_rate)

# Parallel to Serial Conversion
received_symbols = received_parallel_data.flatten()
print(received_parallel_data)


# QPSK Demodulation
received_bit_pairs = [
    min(qpsk_mapping.keys(), key=lambda k: abs(received_symbols[i] - qpsk_mapping[k]))
    for i in range(len(received_symbols))
]
received_bit_stream = np.array([int(bit) for pair in received_bit_pairs for bit in pair])

# Plot bit stream, OFDM signal, and spectrum
plt.figure(figsize=(15, 10))

# Plot bit stream
plt.subplot(4, 1, 1)
plt.title("Bit Stream in Time Domain")
# bit_time = np.repeat(np.arange(len(bit_stream)), 2)[:len(bit_stream)]
bit_values = np.array([int(b) for b in bit_stream])
bit_time = [i/2 for i in range(0, len(bit_values))]

print("bit values: ",bit_values)
print("bit time: ",bit_time)
plt.step(bit_time, bit_values, where='post', color='blue')
plt.xlabel("Bit Index")
plt.ylabel("Bit Value")
plt.grid()

# Plot OFDM signal
plt.subplot(4, 1, 2)
plt.title("Transmitted Signal in Time Domain")
plt.plot(time, transmitted_signal.real, label='Real Part')
plt.plot(time, transmitted_signal.imag, label='Imaginary Part', linestyle='--')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# Frequency domain data of transmitted signal
plt.subplot(4, 1, 3)
plt.title("Transmitted OFDM Signal Spectrum")
spectrum_transmitted = np.fft.fftshift(np.fft.fft(transmitted_signal))
frequencies_transmitted = np.fft.fftshift(np.fft.fftfreq(len(transmitted_signal), d=1/sampling_rate))
plt.plot(frequencies_transmitted, np.abs(spectrum_transmitted))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()

# Frequency domain data of received signal
plt.subplot(4, 1, 4)
plt.title("Received OFDM Signal Spectrum")
spectrum_received = np.fft.fftshift(np.fft.fft(received_signal))
frequencies_received = np.fft.fftshift(np.fft.fftfreq(len(received_signal), d=1/sampling_rate))
plt.plot(frequencies_received, np.abs(spectrum_received))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()

plt.tight_layout()
plt.show()





plt.figure(figsize=(10, 10))

# Received bit stream

plt.title("Received Bit Stream")
plt.plot(received_bit_stream)
plt.xlabel("Bit Index")
plt.ylabel("Bit Value")
plt.grid()
plt.tight_layout()
plt.show()

