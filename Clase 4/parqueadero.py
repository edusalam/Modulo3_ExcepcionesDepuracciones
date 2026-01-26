import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class Vehiculo:
    def __init__(self, placa, hora_entrada):
        self.placa = placa
        self.hora_entrada = hora_entrada

    def calcular_tiempo(self):
        hora_salida = datetime.datetime.now()
        print(hora_salida)
        tiempo_total = hora_salida - self.hora_entrada
        return tiempo_total.total_seconds() / 60
    
class ParqueaderoApp:
    def __init__(self,root):
        self.root = root  #la ventana de interface
        self.root.title('control de parqueo')
        self.root.geometry('500x400')

        self.vehiculos = {}

        #entrada dee la placa
        tk.Label(root, text='placa vehiculo: ').pack(pady=5)
        self.entry_placa = tk.Entry() #el entry carga las cajas de texto
        self.entry_placa.pack(pady=5)
        
        #BOTONES
        tk.Button(root, text='registro de entrada', command=self.registro_entrada).pack(pady=5)
        tk.Button(root, text='registro de salida', command='registro_entrada').pack(pady=5)

        #TABLAS DE VEHICULOS
        self.tree = ttk.Treeview(root, columns=('placa','hora de entrada'), show='headings')
        self.tree.heading('placa', text='placa')
        self.tree.heading('hora de entrada', text='hora de entrada')
        self.tree.pack(pady=10, fill='both',expand=True) #EXPANDE LA INTERFACE
    
    def registro_entrada(self):
        placa = self.entry_placa.get().upper() #el upper guarda de una sola manera
        print(placa)
        if placa and placa not in self.vehiculos:
            hora_actual = datetime.datetime.now().strftime('%H:%M:%S')
            self.vehiculos[placa] = Vehiculo(placa, datetime.datetime.now())

            self.tree.insert('', 'end', iid=placa, values=(placa, hora_actual))



root = tk.Tk()
app = ParqueaderoApp(root)
root.mainloop()


        