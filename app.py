import tkinter as tk
from tkinter import messagebox

def verificar_bissexto():
    try:
        ano = int(entry_ano.get())
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            messagebox.showinfo("Resultado", f"{ano} é um ano bissexto.")
        else:
            messagebox.showinfo("Resultado", f"{ano} não é um ano bissexto.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criando interface gráfica
janela = tk.Tk()
janela.title("Verificador de Ano Bissexto")

tk.Label(janela, text="Digite um ano:").pack(pady=5)
entry_ano = tk.Entry(janela)
entry_ano.pack(pady=5)

tk.Button(janela, text="Verificar", command=verificar_bissexto).pack(pady=10)
janela.mainloop()
