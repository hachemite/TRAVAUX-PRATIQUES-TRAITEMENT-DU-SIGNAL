import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class PlotManager:
    def __init__(self, tab_original, tab_sampled, tab_quantized, tab_binary):
        self.tab_original = tab_original
        self.tab_sampled = tab_sampled
        self.tab_quantized = tab_quantized
        self.tab_binary = tab_binary
        
        # Initialisation des figures
        self.init_plots()
        
    def init_plots(self):
        """Initialise les graphiques dans chaque onglet"""
        # Signal original
        self.fig_original = Figure(figsize=(6, 4), dpi=100)
        self.ax_original = self.fig_original.add_subplot(111)
        self.canvas_original = FigureCanvasTkAgg(self.fig_original, self.tab_original)
        self.canvas_original.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Signal échantillonné
        self.fig_sampled = Figure(figsize=(6, 4), dpi=100)
        self.ax_sampled = self.fig_sampled.add_subplot(111)
        self.canvas_sampled = FigureCanvasTkAgg(self.fig_sampled, self.tab_sampled)
        self.canvas_sampled.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Signal quantifié
        self.fig_quantized = Figure(figsize=(6, 4), dpi=100)
        self.ax_quantized = self.fig_quantized.add_subplot(111)
        self.canvas_quantized = FigureCanvasTkAgg(self.fig_quantized, self.tab_quantized)
        self.canvas_quantized.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Codage binaire
        self.fig_binary = Figure(figsize=(6, 4), dpi=100)
        self.ax_binary = self.fig_binary.add_subplot(111)
        self.canvas_binary = FigureCanvasTkAgg(self.fig_binary, self.tab_binary)
        self.canvas_binary.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Texte pour l'affichage binaire
        self.binary_text = tk.Text(self.tab_binary, wrap=tk.NONE)
        self.binary_text.pack(fill=tk.BOTH, expand=True)
        
    def update_plots(self, signal, sampled_signal, quantized_signal, binary_data, sampling_freq, bits):
        """Met à jour tous les graphiques"""
        self.plot_original(signal)
        self.plot_sampled(signal, sampled_signal, sampling_freq)
        self.plot_quantized(sampled_signal, quantized_signal, bits)
        self.plot_binary(binary_data, quantized_signal['time'])
        
    def plot_original(self, signal):
        """Affiche le signal original"""
        self.ax_original.clear()
        self.ax_original.plot(signal['time'], signal['amplitude'], 'b-')
        self.ax_original.set_title('Signal Analogique Original')
        self.ax_original.set_xlabel('Temps (s)')
        self.ax_original.set_ylabel('Amplitude')
        self.ax_original.grid(True)
        self.canvas_original.draw()
        
    def plot_sampled(self, signal, sampled_signal, sampling_freq):
        """Affiche le signal échantillonné"""
        self.ax_sampled.clear()
        
        # Signal original en fond
        self.ax_sampled.plot(signal['time'], signal['amplitude'], 'b-', alpha=0.3)
        
        # Points d'échantillonnage
        self.ax_sampled.stem(
            sampled_signal['time'], 
            sampled_signal['amplitude'], 
            linefmt='r-', 
            markerfmt='ro', 
            basefmt=' '
        )
        
        self.ax_sampled.set_title(f'Signal Échantillonné (fₛ = {sampling_freq} Hz)')
        self.ax_sampled.set_xlabel('Temps (s)')
        self.ax_sampled.set_ylabel('Amplitude')
        self.ax_sampled.grid(True)
        self.canvas_sampled.draw()
        
    def plot_quantized(self, sampled_signal, quantized_signal, bits):
        """Affiche le signal quantifié"""
        self.ax_quantized.clear()
        
        # Signal échantillonné en fond
        self.ax_quantized.stem(
            sampled_signal['time'], 
            sampled_signal['amplitude'], 
            linefmt='b-', 
            markerfmt='bo', 
            basefmt=' ',
            label='Avant quantification'
        )
        
        # Signal quantifié
        self.ax_quantized.step(
            quantized_signal['time'], 
            quantized_signal['amplitude'], 
            'r-', 
            where='post',
            label='Après quantification'
        )
        
        self.ax_quantized.set_title(f'Signal Quantifié ({bits} bits, {2**bits} niveaux)')
        self.ax_quantized.set_xlabel('Temps (s)')
        self.ax_quantized.set_ylabel('Amplitude')
        self.ax_quantized.grid(True)
        self.ax_quantized.legend()
        self.canvas_quantized.draw()
        
    def plot_binary(self, binary_data, time_points):
        """Affiche le codage binaire"""
        self.ax_binary.clear()
        
        # Affichage des bits sous forme de matrice
        if len(binary_data) > 0:
            bits = len(binary_data[0])
            matrix = np.array([[int(bit) for bit in word] for word in binary_data])
            
            self.ax_binary.imshow(
                matrix.T, 
                cmap='binary', 
                aspect='auto', 
                interpolation='none',
                extent=[0, len(binary_data), 0, bits]
            )
            
            self.ax_binary.set_title('Codage Binaire')
            self.ax_binary.set_xlabel('Échantillon')
            self.ax_binary.set_ylabel('Bit')
            self.ax_binary.set_yticks(range(bits))
            self.ax_binary.set_yticklabels([f'Bit {i}' for i in range(bits-1, -1, -1)])
            self.canvas_binary.draw()
        
        # Affichage textuel
        self.binary_text.delete(1.0, tk.END)
        for t, word in zip(time_points, binary_data):
            self.binary_text.insert(tk.END, f"t = {t:.3f}s: {word}\n")