from tkinter import *
from modulos import make_excel
# from PIL import Image, ImageTk


windows = Tk()
windows.geometry("299x412")
windows.resizable(0, 0)
windows.title("Ventana Principal")

# Verificando si el archivo excel existe, sino, lo crea
make_excel.check()


def registro():
    from modulos import main
    ventana_registro = Toplevel(windows)
    main.cuerpo(ventana_registro)
    insert_button.config(state='disable')  # Deshabilitando el boton cuando se presione

    def on_close():
        ventana_registro.destroy()
        insert_button.config(state='normal')  # Habilita el boton

    ventana_registro.protocol("WM_DELETE_WINDOW", on_close)  # Habilitando el boton cuando se cierra la ventana


def visualizacion():
    from modulos import main_2
    ventana_visualizar = Toplevel(windows)
    main_2.cuerpo_2(ventana_visualizar)
    visual_button.config(state='disable')

    def on_close():
        ventana_visualizar.destroy()
        visual_button.config(state='normal')

    ventana_visualizar.protocol("WM_DELETE_WINDOW", on_close)


# Frame del fondo de pantalla

# Boton para ingresar Datos al Excel
insert_button = Button(windows, text="Ingresar Datos", command=registro)
insert_button.config(bg="olivedrab1")
insert_button.place(x=90, y=40, width=120, height=40)

# Boton para visualizar los Datos en el Excel
visual_button = Button(windows, text="Visualizar Datos", command=visualizacion)
visual_button.config(bg="seagreen1")
visual_button.place(x=90, y=260, width=120, height=40)

# Boton salir
close_button = Button(windows, text='Cerrar', command=quit)
close_button.place(x=90, y=345, width=120, height=40)

# Informacion del creador
derechos = Label(windows, text="Made in Pedro version 2.0 / All rights reserved © 2021")
derechos.place(x=5, y=390, width=300, height=20)

windows.mainloop()


"""
# Frame del fondo de pantalla
frame_img = Frame(windows)
img = Image.open("./wallpaper.jpg")
render = ImageTk.PhotoImage(img)
frame_img.place(height=412, width=299)
Label(frame_img, image=render).grid()
"""