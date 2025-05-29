import numpy as np
import matplotlib.pyplot as plt


# Fonction de quantification suivant la methode CAN Flash
def quantification_CAN_flash(signal, n_bits):
    # Nombre niveau de quantification
    N_levels = 2**n_bits
    
    # Déterminer la plage du signal audio
    min_signal = np.min(signal)
    max_signal = np.max(signal)
    
    # Création des niveaux de référence, uniformément espacés
    levels = np.linspace(min_signal, max_signal, N_levels)
    
    # Quantification
    quantized_signal = np.zeros_like(signal)
    for i, value in enumerate(signal):
        # Trouver l'indice du niveau le plus proche
        index = np.argmin(np.abs(levels - value))
        # Quantification
        quantized_signal[i] = levels[index]
        
    return quantized_signal, levels

def codage_binaire(signal_quantifie, levels, n_bits):
    # Créer un dictionnaire pour mapper les valeurs quantifiées aux codes binaires
    level_to_bin = {level: format(i, '0{}b'.format(n_bits)) for i, level in enumerate(levels)}
    
    # Conversion du niveau de quantification en code binaire
    signal_code_binaire = []
    
    for val in signal_quantifie:
        # Trouver le niveau le plus proche au lieu de chercher une correspondance exacte
        closest_level = levels[np.argmin(np.abs(levels - val))]
        signal_code_binaire.append(level_to_bin[closest_level])
    
    return signal_code_binaire