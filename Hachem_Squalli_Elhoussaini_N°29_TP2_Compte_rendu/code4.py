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

def codage_binaire(signal_quantifie, levels, n_bits):
    # Créer un dictionnaire pour mapper les valeurs quantifiées aux codes binaires
    level_to_bin = {level: format(i, '0{}b'.format(n_bits)) for i, level in enumerate(levels)}
    
    # Conversion du niveau de quantification en code binaire
    signal_code_binaire = [level_to_bin[val] for val in signal_quantifie]
    
    return signal_code_binaire

# Paramètres du signal
f = 5
Fe = 100  # Fréquence d'échantillonnage en Hz
Te = 1/Fe  # période d'échantillonnage en s
T = 1  # Durée du signal en s
t = np.arange(0, T, Te)  # Temps discret pour échantillonnage
t_fine = np.linspace(0, T, 1000)  # Temps continu pour signal analogique

# Génération des signaux
signal_analogique = np.sin(2*np.pi*f*t_fine)  # Signal analogique continu
signal_echanti = np.sin(2*np.pi*f*t)  # Signal échantillonné

n_bits = 4
signal_quantifie, niveaux = quantification_CAN_flash(signal_echanti, n_bits)

# Codage binaire du signal quantifié
signal_code_binaire = codage_binaire(signal_quantifie, niveaux, n_bits)

# Affichage

# Premier subplot: signaux analogique, échantillonné et quantifié
plt.plot(t_fine, signal_analogique, 'g-', label='Signal analogique', linewidth=1, alpha=0.7)
plt.stem(t, signal_echanti, basefmt=" ", linefmt='orange', markerfmt='o', label='Signal échantillonné')
plt.step(t, signal_quantifie, 'b-', where='post', label='Signal quantifié', linewidth=2)
for i, niveau in enumerate(niveaux):
    plt.axhline(y=niveau, color='r', linestyle='--', alpha=0.6)
    # Ajouter des étiquettes pour chaque niveau
    plt.text(1.01, niveau, f'Niveau {i}: {niveau:.3f}', verticalalignment='center')

plt.tight_layout()
plt.show()


for i in range(len(t)):
    print("Temps : {:.2f}, signal_quantifie : {:.2f}, Signal codage binaire : {}".format(t[i], signal_quantifie[i], signal_code_binaire[i]))