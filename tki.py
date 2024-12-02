import tkinter as tk 
from tkinter  import ttk
from Clase import TarifaEstacionamiento


def calcularTarifaHora():
   horas=0.0
   minutos=0.0
   try:
      total= float(input_minutos.get())
      etiqueta_total.config(text=f"Total a pagar:{total}")
   except ValueError as ve:
      etiqueta_error_minutos.config(text=f"Introduce un numero ")

      #Crear un objeto de la clase
      totalPagar = TarifaEstacionamiento
      etiqueta_total.config(text=f"El total a pagar es: {totalPagar.calcularTarifaHora(horas,minutos)}")

   try:
      total= float(input_horas.get())
      etiqueta_total.config(text=f"Total a pagar:{total}")
   except ValueError as ve:
      etiqueta_error_horas.config(text=f"Introduce un numero ")
      


ventana =tk.Tk()
ventana.title ("Tarifa de estacionamiento")
ventana.config(width=500, height=400)

etiqueta_minutos = ttk.Label(text="Introduce las horas")
etiqueta_minutos.place(x=10, y=10)
etiqueta_horas = ttk.Label(text="Introduce los minutos")
etiqueta_horas.place(x=10, y=40)

#Etiquetas para los errores
etiqueta_error_minutos = ttk.Label(text="-")
etiqueta_error_minutos.place(x=275, y=10)
etiqueta_error_horas = ttk.Label(text="-")
etiqueta_error_horas.place(x=275, y=40)


input_minutos=ttk.Entry()
input_minutos.place(x=175, y=10, width=90)
input_horas=ttk.Entry()
input_horas.place(x=175, y=40, width=90)


boton_calcular =ttk.Button(text="Calcular", command=calcularTarifaHora)
boton_calcular.place(x=100, y=80)

etiqueta_total = ttk.Label(text="El total a pagar es: ")
etiqueta_total.place(x=10, y=130)


ventana.mainloop()
