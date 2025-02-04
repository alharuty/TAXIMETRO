import datetime

is_waiting = False
is_driving = True



def taximetro():
    base = int(3.50) #tarifa base
    taxi_is_waiting = float(0.02) #por segundo
    taxi_is_driving = float(0.05) #por segundo

    total_drived_total = 0
    total_waited_total = 0
    print("Bienvenido, porfavor ingrese los datos solicitados...")

    actual_time = datetime.datetime.now()
    starting_at = actual_time
    started_time = actual_time.strftime('%H:%M:%S')

    print(f"Hora de entrada: {started_time}\n")

    selection = input("Actualmente estás conduciendo, escribe W cuando estés esperando: ")

    while True:

        if selection == "W":
            is_driving = False
            drived_time = datetime.datetime.now()
            print(f"El tiempo conducido fue: {drived_time}\n")
            total = drived_time - starting_at
            total_seconds = total.total_seconds()
            total_drived_total = total_drived_total + total_seconds
            print(f"El tiempo conducido fue: {total_seconds:.2f} segundos")
            selection = input("Actualmente estás esperando, escribe D cuando estés conduciendo, o Q para salir:  ")

        elif selection == "D":
            is_driving = True
            waited_time = datetime.datetime.now()
            print(f"El tiempo esperado fue: {waited_time}\n")
            total_waited = waited_time - drived_time
            waited_total_seconds = total_waited.total_seconds()
            total_waited_total = total_waited_total + waited_total_seconds
            print(f"El tiempo esperado fue: {waited_total_seconds:.2f} segundos")
            selection = input("Actualmente estás conduciendo, escribe W cuando estés esperando, o Q para salir: ")

        elif selection == "Q":
            print(f"El tiemp esperado fue: {total_waited_total:.2f} y el tiempo conducido fue: {total_drived_total:.2f}")
            break

        else:
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


# TODO:
    # corregir el tiempo antes de Q, porque ahora no se está sumando, se queda el aire

# import datetime

# def taximetro():
#     base = 3.50  # tarifa base
#     taxi_is_waiting = 0.02  # por segundo
#     taxi_is_driving = 0.05  # por segundo

#     total_drived_total = 0
#     total_waited_total = 0

#     print("Bienvenido, por favor ingrese los datos solicitados...")

#     actual_time = datetime.datetime.now()
#     starting_at = actual_time
#     started_time = actual_time.strftime('%H:%M:%S')

#     print(f"Hora de entrada: {started_time}\n")

#     is_driving = True  # Inicializamos como conduciendo
#     drived_time = starting_at  # El primer tiempo de conducción es la hora de inicio
#     waited_time = None  # El tiempo de espera inicialmente es None

#     selection = input("Actualmente estás conduciendo, escribe W cuando estés esperando: ")

#     while True:
#         if selection == "W" and is_driving:
#             is_driving = False
#             drived_time = datetime.datetime.now()
#             print(f"El tiempo conducido fue: {drived_time - starting_at}\n")
#             total_seconds = (drived_time - starting_at).total_seconds()
#             total_drived_total += total_seconds
#             print(f"El tiempo conducido fue: {total_seconds:.2f} segundos")
#             selection = input("Actualmente estás esperando, escribe D cuando estés conduciendo, o Q para salir: ")

#         elif selection == "D" and not is_driving:
#             is_driving = True
#             waited_time = datetime.datetime.now()
#             print(f"El tiempo esperando fue: {waited_time - drived_time}\n")
#             total_waited = (waited_time - drived_time).total_seconds()
#             total_waited_total += total_waited
#             print(f"El tiempo esperado fue: {total_waited:.2f} segundos")
#             selection = input("Actualmente estás conduciendo, escribe W cuando estés esperando, o Q para salir: ")

#         elif selection == "Q":
#             # Si estamos esperando, calculamos el tiempo que ha pasado desde que comenzamos a esperar
#             if not is_driving and waited_time is not None:
#                 waited_time = datetime.datetime.now()
#                 total_waited = (waited_time - drived_time).total_seconds()
#                 total_waited_total += total_waited

#             # Si estamos conduciendo, calculamos el tiempo que ha pasado desde que comenzamos a conducir
#             if is_driving and drived_time is not None:
#                 drived_time = datetime.datetime.now()
#                 total_drived = (drived_time - starting_at).total_seconds()
#                 total_drived_total += total_drived

#             print(f"El tiempo total esperado fue: {total_waited_total:.2f} segundos.")
#             print(f"El tiempo total conducido fue: {total_drived_total:.2f} segundos.")
#             print("¡Gracias por usar el taxímetro!")
#             break  # Sale del bucle

#         else:
#             print("Entrada no válida, por favor ingresa 'W', 'D' o 'Q'.")
#             selection = input("Actualmente estás conduciendo, escribe W cuando estés esperando, o Q para salir: ")

# taximetro()
