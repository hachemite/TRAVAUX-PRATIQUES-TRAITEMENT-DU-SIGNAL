import numpy as np
import matplotlib.pyplot as plt
import librosa
from codage_quantification import quantification_CAN_flash, codage_binaire

# Charger l'audio
audio_file = "sample-1.wav"
y, sr = librosa.load(audio_file, sr=None)

# Pour plus de clarté, on prend juste un petit segment de l'audio
# (sinon il y aurait trop de points à afficher)
segment_length = 1000  # Nombre d'échantillons à traiter
if len(y) > segment_length:
    y_segment = y[:segment_length]
else:
    y_segment = y

time_segment = np.linspace(0, len(y_segment)/sr, len(y_segment))

# Quantification avec différents nombre de bits
n_bits = 4  # Utiliser moins de bits pour mieux voir l'effet de quantification
signal_quantifie, niveaux = quantification_CAN_flash(y_segment, n_bits)

# Codage binaire
signal_code_binaire = codage_binaire(signal_quantifie, niveaux, n_bits)

# Affichage
plt.figure(figsize=(14, 10))

# Signal original et quantifié
plt.plot(time_segment, y_segment, 'g-', label='Signal audio original', alpha=0.7)
plt.step(time_segment, signal_quantifie, 'b-', where='post', label='Signal quantifié', linewidth=1.5)

# Afficher les niveaux de quantification
for niveau in niveaux:
    plt.axhline(y=niveau, color='r', linestyle='--', alpha=0.3)

plt.title(f'Quantification CAN Flash ({n_bits} bits)')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.xlim(0.012, 0.020)
plt.ylim( -0.0006 ,0.0002)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Afficher quelques échantillons et leur code binaire
print("Extrait des résultats:")
for i, t in enumerate(time_segment):
    if 0.012 <= t <= 0.020:
        print(f"Temps: {t:.4f}s, Valeur: {y_segment[i]:.4f}, Quantifiée: {signal_quantifie[i]:.4f}, Code binaire: {signal_code_binaire[i]}")
