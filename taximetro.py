import datetime

def taximetro():
    print("Bienvenido al TAXÍMETRO. Para empezar el viaje, seleccione la tarifa deseada:")
    print("A = Tarifa diurna.")
    print("B = Tarifa nocturna.")
    print("-----------------\n")

    select_fee = input("Escriba A ó B: ")

    if select_fee == "A":
        base = 3.50
    elif select_fee == "B":
        base = 4.50
    else:
        print("No ha seleccionado una opción correcta.")
        select_fee = input("Escriba A ó B: ")

    taxi_is_waiting = 0.02  # Tarifa por segundo esperando
    taxi_is_driving = 0.05  # Tarifa por segundo conduciendo

    total_drived_total = 0 
    total_waited_total = 0

    while True:
        question = input("Quiere empezar el trayecto? (S ó N): ")
        print("-----------------\n")
        if question == "S":
            is_driving = True
            break
        elif question == "N":
            is_driving = False
            break
        else:
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

            print(f"Tiempo total esperado: {total_waited_total:.2f} segundos\n")
            print(f"Tiempo total conducido: {total_drived_total:.2f} segundos\n")

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
            print("Entrada no válida, por favor ingresa 'W', 'D' o 'Q'.")

taximetro()


#TODO:
    # Corregir: cuando ingresamos un valor incorrecto en la linea 17, después no calcula correctamente el importe total, como que no coge bien la tarifa base


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