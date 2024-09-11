import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calcular_diferenca():
    try:
        data_fornecida = datetime.strptime(entry_data.get(), '%d/%m/%Y')
        data_atual = datetime.now()
        
        diferenca = relativedelta(data_atual, data_fornecida)
        
        resultado = f"{diferenca.years} anos, {diferenca.months} meses e {diferenca.days} dias"
        label_resultado.config(text=f"Resultado: {resultado}", bg="yellow", font=('Arial', 14, 'bold'))
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido. Use o formato DD/MM/AAAA.")

# Configuração da janela principal
root = tk.Tk()
root.title("Bookings")
root.geometry("450x200")
root.config(bg="lightgrey")

# Criação dos widgets
label_data = tk.Label(root, text="Digite o ano de nascimento:", font=('Arial', 14), bg="lightgrey")
label_data.pack(pady=10)

entry_data = tk.Entry(root, font=('Arial', 14), width=15)
entry_data.pack()

botao_calcular = tk.Button(root, text="Calcular", font=('Arial', 12), command=calcular_diferenca)
botao_calcular.pack(pady=10)

label_resultado = tk.Label(root, text="", font=('Arial', 14), bg="lightgrey")
label_resultado.pack(pady=10)

# Iniciar o loop da interface
root.mainloop()
