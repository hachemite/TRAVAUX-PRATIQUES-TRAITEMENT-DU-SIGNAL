import numpy as np

class BinaryEncoder:
    def encode(self, quantized_signal, bits):
        """Encode les valeurs quantifiées en binaire
        
        Args:
            quantized_signal (dict): Signal quantifié
            bits (int): Nombre de bits utilisés
            
        Returns:
            list: Liste de strings binaires
        """
        amplitude = quantized_signal['amplitude']
        step_size = quantized_signal['step_size']
        max_amp = np.max(np.abs(amplitude))
        
        # Normalisation et décalage pour avoir des valeurs positives
        normalized = (amplitude + max_amp) / (2 * max_amp)
        digital = np.round(normalized * (2**bits - 1)).astype(int)
        
        # Conversion en binaire
        binary_data = [format(val, f'0{bits}b') for val in digital]
        
        return binary_data