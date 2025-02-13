import datetime
import logging
from logging_config import setup_logging

setup_logging()

# def format_time(seconds):
#     minutes = int(seconds // 60)  # obtenemos los minutos
#     remaining_seconds = seconds % 60  # obtenemos los segundos restantes
#     return f"{minutes} minutos {remaining_seconds:.0f} segundos" if minutes > 0 else f"{seconds:.0f} segundos"


# format_time(seconds) convertido a función lambda, es como un operador ternario de javascript => condición ? expresión_si_verdadero : expresión_si_falso;
format_time = lambda seconds: f"{int(seconds // 60)} minutos {seconds % 60:.0f} segundos." if seconds >= 60 else f"{seconds:.0f} segundos."


def taximetro():

    print("Bienvenido al TAXÍMETRO. Para empezar el viaje, seleccione la tarifa deseada:")
    print("A = Tarifa diurna. (tarifa base: 3.50€)")
    print("B = Tarifa nocturna. (tarifa base: 4.50€)")
    print("-----------------\n")

    # si ingresamos un valor incorrecto, entramos en bucle hasta que sea correcto y ya seguimos con el codigo
    while True:
        select_fee = input("Escriba A ó B. (Q para salir): ")
        if select_fee == "A":
            base = 3.50
            break
        elif select_fee == "B":
            base = 4.50
            break
        elif select_fee == "Q":
            print("Gracias por usar el Taxímetro. Adios")
            return
        else:
            logging.error(f'Selección inválida en select_fee: {select_fee}.')
            print("No ha seleccionado una opción correcta. Inténtelo de nuevo.")

    taxi_is_waiting = 0.02  # Tarifa por segundo esperando
    taxi_is_driving = 0.05  # Tarifa por segundo conduciendo

    total_drived_total = 0 
    total_waited_total = 0

    while True:
        question = input("Quiere empezar el trayecto? (S ó N) (Q para salir): ")
        print("-----------------\n")
        if question == "S":
            is_driving = True
            break
        elif question == "N":
            is_driving = False
            break
        elif question == "Q":
            print("Gracias por usar el Taxímetro. Adios")
            return
        else:
            logging.error(f'Selección inválida en question: {question} => Opciones válidas: S ó N.')
            print("No ha seleccionado ninguna opción correcta. Inténtelo de nuevo.")

    starting_at = datetime.datetime.now() #usamos el método datetime para averiguar la hora actual
    started_time = starting_at.strftime('%H:%M:%S') # cambiamos de formato fecha a string

    print(f"El trayecto ha empezado. Hora de entrada: {started_time}\n")
    
    last_time = starting_at  # Guarda el tiempo del último cambio de estado

    while True:
        if is_driving == True:
            selection = input("Actualmente estás CONDUCIENDO, escribe W cuando estés esperando, o Q para salir: ")
        else:
            selection = input("Actualmente estás ESPERANDO, escribe D cuando estés conduciendo, o Q para salir: ")

        current_time = datetime.datetime.now()
        elapsed_time = (current_time - last_time).total_seconds()  # Tiempo transcurrido desde el último cambio

        if selection == "W" and is_driving:
            total_drived_total += elapsed_time
            if total_drived_total >= 60:
                print(f"Tiempo total conducido: {format_time(total_drived_total)}\n\n")
            else:
                print(f"Tiempo total conducido: {total_drived_total:.2f} segundos\n\n")

            is_driving = False
            last_time = current_time  # Guardar el momento en que empezó a esperar

        elif selection == "D" and not is_driving:
            total_waited_total += elapsed_time
            print(f"Tiempo total esperado: {total_waited_total:.2f} segundos\n\n")
            is_driving = True
            last_time = current_time  # Guardar el momento en que empezó a conducir

        elif selection == "Q":
            if is_driving:
                total_drived_total += elapsed_time
            else:
                total_waited_total += elapsed_time

            print(f"Tiempo total esperado: {format_time(total_waited_total)}\n")
            print(f"Tiempo total conducido: {format_time(total_drived_total)}\n")

            # Cálculo del costo final
            total_cost = base + (total_drived_total * taxi_is_driving) + (total_waited_total * taxi_is_waiting)
            print(f"Precio total del viaje: {total_cost:.2f}€\n")
            print("------------------------------------------")
            answer = input("Quiere volver a empezar un viaje? (S ó N): ")
            if answer == "S":
                taximetro()
            else:
                print("Gracias por usar el Taxímetro. Adios")
                break

        else:
            logging.error(f'Entrada no válida. Entradas aceptadas: W, D, Q.')
            print("Entrada no válida, por favor ingresa 'W', 'D' o 'Q'.")

taximetro()



# El funcionamiento del taxímetro: 
# Cuando inicializamos el taxímetro empieza a contar y tiene en cuenta que se ha empezado a conducir, es decir, se empieza a contar tiempo conducido nada mas entrar en el taxi
# Cada vez que cambiemos de W a D, se cuenta el tiempo pasado y lo suma al temporizador correspondiente. 

# usamos el método .datetime.now() de la dependencia datetime para contar los segundos transcurridos
# usamos el método .total_seconds() para pasar de formato fecha a segundos

# usamos el formato :.2f para especificar que el número dado es un flotante y que queremos mostrar 2 decimales:
    # : : Indica que a continuación se proporcionará una especificación de formato.
    # .2 : Significa que se debe mostrar el número con dos decimales.
    # f: Especifica que el número debe ser tratado como un número flotante (es decir, un número con decimales).ç



#FUENTES:
    # traer hora actual: https://www.codigopiton.com/como-obtener-la-hora-actual-en-python/#:~:text=Para%20obtener%20la%20hora%20actual,se%20utiliza%20la%20funci%C3%B3n%20strftime%20.
    # ¿Qué es el logging? https://atareao.es/pyldora/tus-logs-en-python-de-forma-eficiente/#:~:text=El%20logging%20en%20Python%20es,diagnosticar%20problemas%20en%20tiempo%20real.
    # ¿Qué es GUI, interfaz gráfica, usamos Tkinter?: https://www.youtube.com/watch?v=hTUJC8HsC2I