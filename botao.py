import tkinter as tk

def mostrar_aviso(texto):
    janela = tk.Tk()
    janela.title("Aviso de Tarefa")
    janela.geometry("400x100")
    janela.configure(bg="#0077cc")  

    frame = tk.Frame(janela, bg="#ffff00", padx=20, pady=20)  
    
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    label = tk.Label(frame, text=texto, font=("Arial", 12, "bold"), bg="#ffff00", fg="#000")
    label.pack()

    janela.mainloop()

mostrar_aviso("🔔 A tarefa 'Entregar relatório' vence em 1 dia!")
