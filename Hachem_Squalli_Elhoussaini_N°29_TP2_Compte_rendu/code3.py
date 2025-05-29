import numpy as np
import matplotlib.pyplot as plt

# Fonction de quantification suivant la methode CAN Flash
def quantification_CAN_flash(signal, n_bits):
    # Nombre niveau de quantification
    N_levels = 2**n_bits
    
    # Plage de signal analogique (supposée entre -1 et 1)
    min_signal = -1
    max_signal = 1
    
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
# Paramètres du signal
f = 5
Fe = 50  # Fréquence d'échantillonnage en Hz
Te = 1/Fe  # période d'échantillonnage en s
T = 1  # Durée du signal en s
t = np.arange(0, T, Te)  # Temps discret pour échantillonnage
t_fine = np.linspace(0, T, 1000)  # Temps continu pour signal analogique

# Génération des signaux
signal_analogique = np.sin(2*np.pi*f*t_fine)  # Signal analogique continu
signal_echanti = np.sin(2*np.pi*f*t)  # Signal échantillonné

n_bits = 4
signal_quantifie ,niveaux= quantification_CAN_flash(signal_echanti, n_bits)

# Affichage
plt.figure(figsize=(12, 6))

# Signal analogique
plt.plot(t_fine, signal_analogique, 'g-', label='Signal analogique', linewidth=1, alpha=0.7)

# Signal échantillonné
plt.stem(t, signal_echanti, basefmt=" ", linefmt='orange', markerfmt='o', label='Signal échantillonné')

# Signal quantifié
plt.step(t, signal_quantifie, 'b-', where='post', label=f'Signal quantifié ({n_bits} bits)', linewidth=2)

for i, niveau in enumerate(niveaux):
    plt.axhline(y=niveau, color='r', linestyle='--', alpha=0.6)
    # Ajouter des étiquettes pour chaque niveau
    plt.text(1.01, niveau, f'Niveau {i}: {niveau:.3f}', verticalalignment='center')


plt.title("Signal Analogique, Échantillonné et Quantifié (Flash ADC)")
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()