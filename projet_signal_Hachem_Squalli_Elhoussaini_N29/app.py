import tkinter as tk
from tkinter import ttk
from signal_generator import SignalGenerator
from sampling import Sampler
from quantization import Quantizer
from binary_encoding import BinaryEncoder
from plots import PlotManager

class CANApplication:
    def __init__(self, master):
        self.master = master
        master.title("Convertisseur Analogique-Numérique")
        master.geometry("1200x800")
        
        # Configuration du style
        self.style = ttk.Style()
        self.style.configure('TFrame', padding=6)
        self.style.configure('TButton', padding=6)
        self.style.configure('TLabel', padding=6, font=('Helvetica', 10))
        self.style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))
        
        self.create_widgets()
        self.init_components()
        
    def create_widgets(self):
        """Crée l'interface utilisateur"""
        # Frame principal
        self.main_frame = ttk.Frame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Panneau de contrôle
        self.control_frame = ttk.LabelFrame(self.main_frame, text="Paramètres", padding=10)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Zone d'affichage
        self.display_frame = ttk.Frame(self.main_frame)
        self.display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Création des onglets
        self.notebook = ttk.Notebook(self.display_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        self.tab_original = ttk.Frame(self.notebook)
        self.tab_sampled = ttk.Frame(self.notebook)
        self.tab_quantized = ttk.Frame(self.notebook)
        self.tab_binary = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_original, text="Signal Original")
        self.notebook.add(self.tab_sampled, text="Signal Échantillonné")
        self.notebook.add(self.tab_quantized, text="Signal Quantifié")
        self.notebook.add(self.tab_binary, text="Codage Binaire")
        
        # Ajout des contrôles
        self.add_signal_controls()
        self.add_sampling_controls()
        self.add_quantization_controls()
        
        # Bouton de traitement
        self.process_btn = ttk.Button(
            self.control_frame, 
            text="Traiter le signal", 
            command=self.process_signal
        )
        self.process_btn.pack(pady=10)
    
    def init_components(self):
        """Initialise les composants de traitement"""
        self.signal_gen = SignalGenerator()
        self.sampler = Sampler()
        self.quantizer = Quantizer()
        self.binary_encoder = BinaryEncoder()
        self.plot_manager = PlotManager(
            self.tab_original, 
            self.tab_sampled, 
            self.tab_quantized, 
            self.tab_binary
        )
    
    def add_signal_controls(self):
        """Ajoute les contrôles pour la génération du signal"""
        frame = ttk.LabelFrame(self.control_frame, text="Génération du Signal", padding=10)
        frame.pack(fill=tk.X, pady=5)
        
        # Type de signal
        ttk.Label(frame, text="Type de signal:").pack(anchor=tk.W)
        self.signal_type = tk.StringVar(value="sinusoidal")
        types = ["sinusoidal", "cosinus", "carré", "triangulaire"]
        for t in types:
            ttk.Radiobutton(frame, text=t, variable=self.signal_type, value=t).pack(anchor=tk.W)
        
        # Amplitude
        ttk.Label(frame, text="Amplitude:").pack(anchor=tk.W)
        self.amplitude = tk.DoubleVar(value=1.0)
        ttk.Entry(frame, textvariable=self.amplitude).pack(fill=tk.X)
        
        # Fréquence
        ttk.Label(frame, text="Fréquence (Hz):").pack(anchor=tk.W)
        self.frequency = tk.DoubleVar(value=1.0)
        ttk.Entry(frame, textvariable=self.frequency).pack(fill=tk.X)
        
        # Durée
        ttk.Label(frame, text="Durée (s):").pack(anchor=tk.W)
        self.duration = tk.DoubleVar(value=1.0)
        ttk.Entry(frame, textvariable=self.duration).pack(fill=tk.X)
    
    def add_sampling_controls(self):
        """Ajoute les contrôles pour l'échantillonnage"""
        frame = ttk.LabelFrame(self.control_frame, text="Échantillonnage", padding=10)
        frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame, text="Fréq. échantillonnage (Hz):").pack(anchor=tk.W)
        self.sampling_freq = tk.DoubleVar(value=10.0)
        ttk.Entry(frame, textvariable=self.sampling_freq).pack(fill=tk.X)
    
    def add_quantization_controls(self):
        """Ajoute les contrôles pour la quantification"""
        frame = ttk.LabelFrame(self.control_frame, text="Quantification", padding=10)
        frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame, text="Nombre de bits:").pack(anchor=tk.W)
        self.bits = tk.IntVar(value=8)
        ttk.Entry(frame, textvariable=self.bits).pack(fill=tk.X)
    
    def process_signal(self):
        """Traite le signal selon les paramètres"""
        try:
            # Génération du signal
            signal = self.signal_gen.generate(
                signal_type=self.signal_type.get(),
                amplitude=self.amplitude.get(),
                frequency=self.frequency.get(),
                duration=self.duration.get()
            )
            
            # Échantillonnage
            sampled_signal = self.sampler.sample(
                signal, 
                self.sampling_freq.get(), 
                self.duration.get()
            )
            
            # Quantification
            quantized_signal = self.quantizer.quantize(
                sampled_signal, 
                self.bits.get()
            )
            
            # Codage binaire
            binary_data = self.binary_encoder.encode(quantized_signal, self.bits.get())
            
            # Affichage
            self.plot_manager.update_plots(
                signal, 
                sampled_signal, 
                quantized_signal, 
                binary_data,
                self.sampling_freq.get(),
                self.bits.get()
            )
            
        except Exception as e:
            tk.messagebox.showerror("Erreur", f"Une erreur est survenue: {str(e)}")