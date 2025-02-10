from tkinter import *
from tkinter import messagebox

# my_program = Tk()

# my_program.title("Taxímetro de Alla")

# my_program.geometry("600x300")

# my_frame = Frame(my_program, width=600, height=300, bg="black")
# my_frame.pack()

# Label(my_frame, text="BIENVENIDO AL TAXÍMETRO.\n Para empezar el viaje debe seleccionar la tarifa base (diurna o nocturna)", fg="green", font=(18), bg="black").pack(expand=True)

class Taximetro:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxímetro de Alla")
        self.root.geometry("600x300")

        self.day_base = 3.50
        self.night_base = 4.50

        self.is_driving = False
        self.start_time = None
        self.last_time = None
        self.total_drived_total = 0
        self.total_waited_total = 0
        
        self.taxi_is_waiting = 0.02
        self.taxi_is_driving = 0.05

        # creamos frame dentro de la ventana principal
        self.my_frame = Frame(self.root, width=600, height=300)
        self.my_frame.pack()

        # mensaje de bienvenida
        Label(self.my_frame, text="BIENVENIDO AL TAXÍMETRO.\nPara empezar el viaje debe seleccionar la tarifa base (diurna o nocturna):",
            fg="green", font=("Arial", 10), pady=10, padx=20).pack(expand=True)

        # Crear otro frame para los botones y usar pack()
        self.buttons_frame = Frame(self.root)
        self.buttons_frame.pack()

        self.btn_day = Button(self.buttons_frame, text="Tarifa diurna (3.50€)", command=lambda: self.selected_base(self.day_base))
        self.btn_day.pack(side="left")

        self.btn_night = Button(self.buttons_frame, text="Tarifa nocturna (4.50€)", command=lambda: self.selected_base(self.night_base))
        self.btn_night.pack(side="left")

        # boton cerrar programa
        self.close_app = Button(self.root, text="Cerrar taxímetro", command=self.close_app)
        self.close_app.pack()

        self.label_status = Label(self.root, text="Estado: Esperando selección de tarifa", fg="black")
        self.label_status.pack(pady=10)

    def selected_base(self, base):
        self.tarifa_base = base
        self.label_status.config(text=f"Tarifa seleccionada: {self.tarifa_base}\nListo para iniciar el viaje.")
        self.btn_day.pack_forget()
        self.btn_night.pack_forget()
        self.buttons_frame.pack_forget()

        self.start_driving = Button(self.root, text="Conducir", command=self.driving)
        self.start_driving.pack()

        self.start_waiting = Button(self.root, text="Esperar", command=self.driving)
        self.start_waiting.pack()

    def driving(self):
        self.label_status.config(text="Usted está conduciendo.")

    def waiting(self):
        self.label_status.config(text="Usted está esperando.")



    def close_app(self):
        # preguntamos si está seguro de que quiere salir
        #response = messagebox.askyesno("Confirmar salida", "¿Estás seguro de que quieres salir?")
        
        #if response:  # si la respuesta es Sí
            #self.root.destroy()  # Cierra la ventana y termina el programa
        self.root.destroy()

# Ejecutar la aplicación
if __name__ == "__main__":
    root = Tk()
    app = Taximetro(root)
    root.mainloop()



# NOTAS
# 1. En un mismo class, no se puede usar grid y pack a la vez, hay que elegir uno