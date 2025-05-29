import numpy as np

class Quantizer:
    def quantize(self, signal, bits):
        """Quantifie un signal échantillonné
        
        Args:
            signal (dict): Signal échantillonné {'time': array, 'amplitude': array}
            bits (int): Nombre de bits pour la quantification
            
        Returns:
            dict: {'time': array, 'amplitude': array, 'levels': array}
        """
        if bits <= 0:
            raise ValueError("Le nombre de bits doit être positif")
            
        amplitude = signal['amplitude']
        max_amp = np.max(np.abs(amplitude))
        
        # Calcul des niveaux de quantification
        num_levels = 2**bits
        step_size = 2 * max_amp / num_levels
        
        # Quantification
        quantized = np.round(amplitude / step_size) * step_size
        
        return {
            'time': signal['time'],
            'amplitude': quantized,
            'levels': num_levels,
            'step_size': step_size
        }