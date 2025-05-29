from app import CANApplication
import tkinter as tk

def main():
    root = tk.Tk()
    app = CANApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()