from tkinter import *
from tkinter import ttk
from modulos import excel
from tkcalendar import DateEntry
from tkinter import messagebox as msb


def cuerpo(windows):
    windows.geometry("370x370")
    windows.resizable(0, 0)
    windows.title("Ingreso de Datos")

    # Limpiar lo que se ingreso en la casilla
    def clearTextInput():
        cuerpo_text.delete("1.0", "end")

    def getDato():
        fecha = cal.get_date()
        texto = cuerpo_text.get("1.0", "end-1c")
        lista = []

        if texto == '':
            msb.showerror('Campo Vacio!', 'Verifique que todos los campos estan con información')
        elif tipo_combobox.get() == '':
            msb.showerror('Error en "Tipo de Ingreso"!', 'Favor seleccionar un "Tipo de Ingreso"')
        elif texto[0] == '=' or texto[0] == '+' or texto[0] == '-' or texto[0] == '/' or texto[0] == '*':
            msb.showerror('OIE NO', 'Ese simbolo de inicio, no esta permitido')

        else:
            if tipo_combobox.get() == "Apunte":
                lista.append(fecha)
                lista.append(texto)
                # Ingresar funcion de excel
                excel.func_apunte(lista)
                clearTextInput()  # Limpia la casilla luego de guardar
                msb.showinfo('Felicidades!', 'Su "Apunte" a sido ingresado satisfactoriamente')

            elif tipo_combobox.get() == "Recordatorio":
                lista.append(fecha)
                lista.append(texto)
                # Ingresar funcion de excel
                excel.func_recordatorio(lista)
                clearTextInput()  # Limpia la casilla luego de guardar
                msb.showinfo('Felicidades!', 'Su "Recordatorio" a sido ingresado satisfactoriamente')

    def grab_date():
        cal.get_date()

    # CASILLA CON MENU DESPLEGABLE DE 2 OPCIONES
    tipo_label = Label(windows, text="Tipo de Ingreso")
    tipo_label.grid(row=2, column=1)

    tipo_combobox = ttk.Combobox(windows, width=17, state='readonly', values=["Apunte", "Recordatorio"])
    tipo_combobox.grid(row=2, column=2)
    tipo_combobox.bind("<<ComboboxSelected>>", lambda _: text_label.config(text=f'Ingrese el "{tipo_combobox.get()}"'))

    # CALENDARIO DESPLEGABLE
    cal_label = Label(windows, text='Seleccione la Fecha')
    cal_label.grid(row=4, column=1)

    cal = DateEntry(windows, state='readonly', locale='spa', date_pattern='dd/mm/y')
    cal.config(headersbackground='#364c55', foreground='#000', background='#fff', headersforeground='#fff',
               locale='spa')
    cal.grid(row=4, column=2)

    # CASILLA GRANDE PARA ESCRIBIR
    text_label = Label(windows)  # El nombre no varia segun la opcion seleccionada.
    text_label.grid(row=6, column=1, columnspan=2)

    cuerpo_text = Text(windows)
    cuerpo_text.grid(row=7, column=1, columnspan=2)
    cuerpo_text.config(width=40, heigh=10, padx=15, pady=15)

    # BOTON REGISTRO / SALIR
    registrar_button = Button(windows, text="Registrar", command=lambda: [getDato(), grab_date()])
    registrar_button.grid(row=9, column=1, columnspan=2)

    # ESPACIOS
    Label(windows).grid(row=1)
    Label(windows).grid(row=3)
    Label(windows).grid(row=5)
    Label(windows).grid(row=8)
    Label(windows).grid(column=0)
