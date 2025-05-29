import numpy as np

class Sampler:
    def sample(self, signal, sampling_freq, duration):
        """Échantillonne un signal analogique
        
        Args:
            signal (dict): Signal analogique {'time': array, 'amplitude': array}
            sampling_freq (float): Fréquence d'échantillonnage en Hz
            duration (float): Durée totale en secondes
            
        Returns:
            dict: {'time': array, 'amplitude': array}
        """
        if sampling_freq <= 0:
            raise ValueError("La fréquence d'échantillonnage doit être positive")
            
        # Calcul des instants d'échantillonnage
        sample_times = np.arange(0, duration, 1/sampling_freq)
        
        # Interpolation pour obtenir les valeurs aux instants d'échantillonnage
        sampled_amplitude = np.interp(sample_times, signal['time'], signal['amplitude'])
        
        return {'time': sample_times, 'amplitude': sampled_amplitude}