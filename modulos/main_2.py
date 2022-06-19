from tkinter import *
from tkinter import ttk
import pandas as pd


def cuerpo_2(windows):
    windows.geometry("820x600")
    windows.resizable(0, 0)
    windows.title("Visualización de Datos")

    def getApuntes():
        fp = pd.read_excel("./libro_registro.xlsx", sheet_name="APUNTES")
        for _ in range(len(fp.index.values)):
            tabla_visual.insert('', 'end', value=tuple(fp.iloc[_, [0, 1]].values))

    def getRecordatorio():
        fp = pd.read_excel("./libro_registro.xlsx", sheet_name="RECORDATORIO")
        for _ in range(len(fp.index.values)):
            tabla_visual.insert('', 'end', value=tuple(fp.iloc[_, [0, 1]].values))

    def clear():
        tabla_visual.delete(*tabla_visual.get_children())

    def remove_item():  # Modo BETA
        selected_items = tabla_visual.selection()
        for selected_item in selected_items:
            tabla_visual.delete(selected_item)

    # Visualizar informacion de hoja "Apuntes"
    apuntes_button = Button(windows, text="Visualizar Apuntes", command=lambda: [clear(), getApuntes()])
    apuntes_button.grid(row=1, column=0)

    # Visualizar informacion de hoja "Recordatorios"
    recordatorios_button = Button(windows, text="Visualizar Recordatorios",
                                  command=lambda: [clear(), getRecordatorio()])
    recordatorios_button.grid(row=1, column=1)

    # TABLA
    columns = ("Fecha", "Información")
    tabla_visual = ttk.Treeview(windows, show="headings", columns=columns, height=27)

    # "SCROLLBAR" EN TABLA
    barra_lateral = Scrollbar(windows, orient="vertical", command=tabla_visual.yview)
    barra_lateral.place(x=799, y=25, height=539 + 30)
    tabla_visual.configure(yscrollcommand=barra_lateral.set)

    tabla_visual.column("Fecha", width=398, anchor='center')
    tabla_visual.column("Información", width=398, anchor='center')

    tabla_visual.heading("Fecha", text="Fecha")
    tabla_visual.heading("Información", text="Dato")

    tabla_visual.grid(row=2, column=0, columnspan=3)

    # BOTON PARA BORRAR DATOS (MODO BETA)
    eliminar_button = Button(windows, text='Eliminar (BETA)', command=remove_item)
    eliminar_button.grid(row=1, column=2)
