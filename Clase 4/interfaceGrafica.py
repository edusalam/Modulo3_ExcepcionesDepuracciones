#tkinter, libreria de python, interfaces graficas
#importante se tiene que definir dos cosas: 1. el titulo
import tkinter as tk

# PRIMER EJERCICIO
def convertir():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        resultado.config(text=f'resultado: {fahrenheit:.2f}°F')
    except:
        resultado.config(text='ingrese un numero valido')

#configuracion de la ventana
root = tk.Tk()
root.title('Conversor de temperatura')
root.geometry('300x200')

#widgets
tk.Label(root, text='ingrese temperatura en c:').pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text='convertir', command=convertir).pack(pady=5)
resultado = tk.Label(root,text='resultado: ')
resultado.pack(pady=5)

root.mainloop()

