import datetime
import logging
from logging_config import setup_logging

setup_logging()

format_time = lambda seconds: f"{int(seconds // 60)} min {seconds % 60:.0f} seg." if seconds >= 60 else f"{seconds:.0f} seg."

def taximetro():

    print("\nBienvenido al TAXÍMETRO. Para empezar el viaje, seleccione la tarifa deseada:\n")
    print("A = Tarifa diurna. (tarifa base: 3.50€)")
    print("B = Tarifa nocturna. (tarifa base: 4.50€)")
    
    # si ingresamos un valor incorrecto, entramos en bucle hasta que sea correcto y ya seguimos con el codigo
    while True:
        select_fee = input("\nEscriba A ó B. (Q para salir): ")
        if select_fee == "A":
            base = 3.50
            break
        elif select_fee == "B":
            base = 4.50
            break
        elif select_fee == "Q":
            print("\nGracias por usar el Taxímetro. Adios")
            return
        else:
            logging.error(f'Selección inválida en select_fee: {select_fee}.')
            print("No ha seleccionado una opción correcta. Inténtelo de nuevo. (A, B ó Q)")

    print("-----------------------------------------")
    taxi_is_waiting = 0.02
    taxi_is_driving = 0.05
    km_price = 1

    total_drived_total = 0 
    total_waited_total = 0

    while True:
        print(f"\nVa a empezar el trayecto con la tarifa base: {base}€.")
        question = input("\nC: Empezar CONDUCIENDO.\nE: Empezar ESPERANDO\nQ: Salir del trayecto\n\nEliga la opción deseada: ")
        print("-----------------------------------------\n")
        if question == "C":
            is_driving = True
            break
        elif question == "E":
            is_driving = False
            break
        elif question == "Q":
            print("Gracias por usar el Taxímetro. Adios\n")
            return
        else:
            logging.error(f'Selección inválida en question: {question} => Opciones válidas: C, E ó Q.')
            print("No ha seleccionado ninguna opción correcta. Inténtelo de nuevo.")

    starting_at = datetime.datetime.now()
    started_time = starting_at.strftime('%H:%M:%S')

    print(f"El trayecto ha empezado. Hora de entrada: {started_time}\n")
    
    last_time = starting_at  # guarda el tiempo del último cambio de estado

    while True:
        if is_driving == True:
            selection = input("Actualmente estás CONDUCIENDO, escribe E cuando estés esperando, o F para finalizar: ")
        else:
            selection = input("Actualmente estás ESPERANDO, escribe C cuando estés conduciendo, o F para finalizar: ")

        current_time = datetime.datetime.now()
        elapsed_time = (current_time - last_time).total_seconds()  # tiempo transcurrido desde el último cambio

        if selection == "E" and is_driving:
            total_drived_total += elapsed_time
            is_driving = False
            last_time = current_time

        elif selection == "C" and not is_driving:
            total_waited_total += elapsed_time
            is_driving = True
            last_time = current_time

        elif selection == "F":
            if is_driving:
                total_drived_total += elapsed_time
            else:
                total_waited_total += elapsed_time

            km = input("Ingrese los kilómetros del trayecto: ")
            if km.isnumeric():
                km = float(km)
                total_km_price = km * km_price
            elif km.isalpha():
                print("Porfavor ingresa un número.")
            else:
                print("Porfavor intentelo de nuevo: ")

            print("\n-----------------------------------------")

            total_drived_price =  total_drived_total * taxi_is_driving
            total_waited_price = total_waited_total * taxi_is_waiting
            total_total_price = total_drived_price + total_waited_price

            print(f"Tarifa base: {base}€")
            print(f"Precio total trayectoria: {total_total_price:.2f}€")
            print(f"Precio total de kms: {total_km_price}€")

            total_cost = base + (total_drived_total * taxi_is_driving) + (total_waited_total * taxi_is_waiting) + total_km_price
            mensaje = f"Precio total del viaje: {total_cost:.2f}€"
            borde = "-" * (len(mensaje) + 2)

            print("\n╭" + borde + "╮")
            print(f"│ {mensaje} │")
            print("╰" + borde + "╯")
            print("------------------------------------------")
            while True:
                # Lógica del viaje...
                answer = input("Quiere volver a empezar un viaje? (S ó N): ")
                if answer == "S":
                    taximetro()
                elif answer == "N":
                    print("\nGracias por usar el Taxímetro. Adios")
                    return


        else:
            logging.error(f'Entrada no válida. Entradas aceptadas: D, E, F.')
            print("Entrada no válida, por favor ingresa 'C', 'E' o 'F'.")

taximetro()