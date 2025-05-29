import numpy as np

class SignalGenerator:
    def generate(self, signal_type, amplitude, frequency, duration):
        """Génère un signal analogique
        
        Args:
            signal_type (str): Type de signal ('sinusoidal', 'cosinus', 'carré', 'triangulaire')
            amplitude (float): Amplitude du signal
            frequency (float): Fréquence en Hz
            duration (float): Durée en secondes
            
        Returns:
            dict: {'time': array, 'amplitude': array}
        """
        # Fréquence d'échantillonnage élevée pour un signal "analogique"
        sample_rate = 1000  # Hz
        num_samples = int(duration * sample_rate)
        t = np.linspace(0, duration, num_samples, endpoint=False)
        
        if signal_type == "sinusoidal":
            signal = amplitude * np.sin(2 * np.pi * frequency * t)
        elif signal_type == "cosinus":
            signal = amplitude * np.cos(2 * np.pi * frequency * t)
        elif signal_type == "carré":
            signal = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
        elif signal_type == "triangulaire":
            signal = amplitude * (2 * np.abs((frequency * t) % 1 - 0.5) - 0.5)
        else:
            raise ValueError("Type de signal non reconnu")
        
        return {'time': t, 'amplitude': signal}