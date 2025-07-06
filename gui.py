import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from utils import load_crypto_data
from predictor import train_and_predict

class CryptoAgentApp:
    def __init__(self, master):
        self.master = master
        master.title("Crypto Trading Agent")
        master.geometry("540x440")
        
        self.data = None
        self.mode = tk.StringVar(value='strategist')
        
        tk.Button(master, text="Load CSV", command=self.load_data).pack(pady=10)
        
        tk.Label(master, text="Mode:").pack()
        tk.Radiobutton(master, text="Strategist", variable=self.mode, value='strategist').pack()
        tk.Radiobutton(master, text="Risk-taker", variable=self.mode, value='risk-taker').pack()
        
        tk.Button(master, text="Predict", command=self.predict).pack(pady=10)
        
        self.status_label = tk.Label(master, text="")
        self.status_label.pack()
        
        self.canvas_frame = tk.Frame(master)
        self.canvas_frame.pack(expand=True, fill=tk.BOTH)

    def load_data(self):
        filepath = filedialog.askopenfilename(title="Select CSV File")
        if not filepath:
            return
        try:
            self.data = load_crypto_data(filepath)
            self.status_label.config(text=f"Loaded {len(self.data)} data points")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def predict(self):
        if self.data is None or len(self.data) < 15:
            from tkinter import messagebox
            messagebox.showwarning("No data", "Please, load CSV with price history with at least 15 days")
            return

        mode = self.mode.get()
        preds = train_and_predict(self.data.values, mode=mode, predict_steps=7)
        
        # Відображення графіка з прозорістю
        import matplotlib.pyplot as plt
        import numpy as np

        fig, ax = plt.subplots(figsize=(6, 4), dpi=90)
        x_real = np.arange(len(self.data))
        x_pred = np.arange(len(self.data), len(self.data) + 7)
        
        ax.plot(x_real, self.data, label="History", color="blue")
        
        for i in range(len(preds)):
            alpha = 0.3 + 0.7 * (1 - i / max(1, (len(preds)-1)))
            if i == 0:
                x_vals = [x_real[-1], x_pred[0]]
                y_vals = [self.data.values[-1], preds[0]]
            else:
                x_vals = [x_pred[i-1], x_pred[i]]
                y_vals = [preds[i-1], preds[i]]
            ax.plot(x_vals, y_vals, color="orange", alpha=alpha, linewidth=3)
        
        ax.scatter(x_pred, preds, color="orange", alpha=0.3, label="Прогноз")
        ax.legend()
        ax.set_title(f"Crypto Trading Agent: mode {mode.capitalize()}")
        ax.set_xlabel("Day")
        ax.set_ylabel("Price")
        ax.grid(True)
    
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill='both')
        plt.close(fig)

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoAgentApp(root)
    root.mainloop()