from tkinter import *
from tkinter import messagebox
import datetime

class Taximetro:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxímetro de Alla")
        self.root.geometry("600x400")

        self.setup()
    
    def setup(self):

        self.day_base = 3.50
        self.night_base = 4.50

        self.is_driving = False
        self.start_time = None
        self.last_time = None
        self.total_drived_total = 0
        self.total_waited_total = 0
        
        self.waiting_price = 0.02
        self.driving_price = 0.05

        # creamos frame dentro de la ventana principal
        self.my_frame = Frame(self.root, width=600, height=400)
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

        self.label_status.config(text=f"Tarifa base seleccionada: {self.tarifa_base}€\n")
        self.buttons_frame.pack_forget()


        self.label_question = Label(self.root, text="¿Listo para iniciar el viaje?")
        self.label_question.pack()

        self.start_trip = Button(self.root, text="Empezar", command=self.start_trip)
        self.start_trip.pack()

    def start_trip(self):
        self.start_trip.pack_forget()
        self.label_question.pack_forget()

        self.label_status2 = Label(self.root, text="Seleccione una acción para iniciar el taxímetro.")
        self.label_status2.pack()

        self.status_buttons_frame = Frame(self.root)
        self.status_buttons_frame.pack()

        self.start_driving = Button(self.status_buttons_frame, text="Conducir", command=self.driving)
        self.start_driving.pack(side="left")

        self.start_waiting = Button(self.status_buttons_frame, text="Esperar", command=self.waiting)
        self.start_waiting.pack(side="left")


        self.finish_button = Button(self.root, text="Finalizar viaje", command=self.finish_trip)
        self.finish_button.pack()

    def driving(self):
        current_time = datetime.datetime.now()

        # Iniciar tiempo solo si es la primera vez que se presiona
        if self.start_time is None:
            self.start_time = current_time
            self.label_start_time = Label(self.root, text=f"Hora de inicio del trayecto: {self.start_time.strftime('%H:%M:%S')}", font=("Arial", 10, "bold"))
            self.label_start_time.pack()

        elapsed_time = 0
        if not self.is_driving and self.last_time is not None:
            elapsed_time = (current_time - self.last_time).total_seconds()
            self.total_waited_total += elapsed_time  # Sumar tiempo de espera
        
        self.last_time = current_time
        self.is_driving = True
        self.label_status2.config(text="Usted está conduciendo.")


    def waiting(self):
        current_time = datetime.datetime.now()

        # Iniciar tiempo solo si es la primera vez que se presiona
        if self.start_time is None:
            self.start_time = current_time
            self.label_start_time = Label(self.root, text=f"Hora de inicio del trayecto: {self.start_time.strftime('%H:%M:%S')}", font=("Arial", 10, "bold"))
            self.label_start_time.pack()
        
        elapsed_time = 0
        if self.is_driving and self.last_time is not None:
            elapsed_time = (current_time - self.last_time).total_seconds()
            self.total_drived_total += elapsed_time  # Sumar tiempo de conducción

        self.last_time = current_time
        self.is_driving = False
        self.label_status2.config(text="Usted está esperando.")

    def finish_trip(self):
        current_time = datetime.datetime.now()

        # Asegurar que se cuenta el último periodo de conducción o espera
        if self.last_time is not None:
            elapsed_time = (current_time - self.last_time).total_seconds()
            if self.is_driving:
                self.total_drived_total += elapsed_time
            else:
                self.total_waited_total += elapsed_time

        total_price = self.tarifa_base + (self.total_drived_total * self.driving_price) + (self.total_waited_total * self.waiting_price)
        total_price = round(total_price, 2)

        self.start_driving.pack_forget()
        self.start_waiting.pack_forget()
        self.finish_button.pack_forget()
        self.label_status2.pack_forget()
        self.label_status.pack_forget()

        Label(self.root, text=f"RESUMEN DEL VIAJE\n---------------------------------\n", font=("Arial", 12, "bold")).pack()
        Label(self.root, text=f"Tarifa base seleccionada: {self.tarifa_base}€\n", bg="#a6df9a").pack()
        Label(self.root, text=f"Tiempo total conducido: {self.total_drived_total:.2f}\nTiempo total esperado: {self.total_waited_total:.2f}\n").pack()
        Label(self.root, text=f"Precio total del viaje: {total_price:.2f}€", font=("Arial", 12, "bold")).pack()

        # Botón para reiniciar
        Button(self.root, text="Reiniciar", command=self.restart_app).pack(pady=5)

    def restart_app(self):
        for widget in self.root.winfo_children():
            widget.destroy()  # Eliminar todos los widgets antes de resetear
        self.setup()

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
