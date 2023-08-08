#'PROYECTO FINAL - Introducción a la programación con Python'
#'Tec. Espíndola Florencia'
#'----------------------------------------------------------------------------'
import datetime
import random
nomLocal = "💵 Q U I N I E L A 💴\nS I E M P R E  S A L E"

'**********FUNCIONES**********'
#'Funcion del menú principal 👇'
def mostrarMenuPrincipal():
    print('')
    print(f'{nomLocal}')

    menu_principal = [
        ("1", "Quiniela 🍀"),
        ("2", "Quini 6 🤞"),
        ("3", "Comprobar apuesta ✅"),
        ("4", "Arqueo de caja 💲"),
        ("5", "Salir ❌")
    ]

    while True:
        print('\nPor favor, elegí la opción deseada 🤗\n')

        for opcion, descripcion in menu_principal:
            print(f'* {opcion} - {descripcion}')

        option = obtenerOpcion()

        if option == 1:
            Quiniela()
        elif option == 2:
            Quini6()
        elif option == 3:
            cargaGanador()
        elif option == 4:
            arqueoCaja()
        elif option == 5:
            print("\n**************************************")
            print("¿Desea salir?\n1- SI\n2- NO")
            if opcionSiNo() == True:
                print("Salida exitosa 😁")
                break
        else:
            print("\n⚠ ¡ATENCIÓN! El número ingresado no corresponde a las opciones del menú, ingrese nuevamente.")

#'Función para pedir la opción elegida por el usuario y validarla'
def obtenerOpcion():
    while True:
        try:
            print("\n**************************************")
            opcionMP = int(input("Ingresá el número:👉 "))
            if opcionMP in range(1, 6):
                return opcionMP
            else:
                print("\n¡ATENCIÓN! Opción inválida 🤦‍♀️ Intente nuevamente...")
        except ValueError:
            print("\n¡ATENCIÓN! Debe ingresar un número válido.")

#'Función que se utilizará en las preguntas de SI y NO'
def opcionSiNo():
    while True:
        try:
            optionOut = int(input("Ingrese la opción que corresponda (1 o 2): "))
            if optionOut == 1:
                return True
            elif optionOut == 2:
                return False
            else:
                print("¡ATENCIÓN! La opción es inválida 🤦‍♀️")
        except ValueError:
            print("¡ATENCIÓN! El número ingresado debe ser entero. Unicamente el 1 o el 2.")

#Función para solicitar el importe a apostar.
def obtenerImporte():
    while True:
        try:
            print("\n**************************************")
            importe = float(input("Ingrese el importe que quiere apostar 💵\nRecordá que el monto mínimo a apostar es $4.00: "))
            return importe
        except ValueError:
            print("¡ATENCIÓN! El importe debe ser un número válido.")

#Función para solicitar el dni y validación de datos
def pideDni():
    while True:
        try:
            print("\n**************************************")
            dni = int(input("Ingresá el DNI del apostador:👉 "))
            if len(str(dni)) == 8 :
                return dni
            else:
                print("Error: El dni tiene una longitud incorrecta. Volve a ingresar")
        except ValueError:
            print("Error: Debes ingresar un número entero para el DNI.")

#Procedimiento para guardar los datos en un txt. despues me servirá para comparar el número ganador
def guardarDatostxt(datos, nombretxt):
     try:
         with open(nombretxt, "a") as archivo:
             for registro in datos:
                 linea = "/".join([str(valor) for valor in registro.values()])
                 archivo.write(linea + "\n")
     except Exception as e:
        print(f"Error al guardar los datos en el archivo: {e}")

#Procedimiento para la primera opción del menú principal: Quiniela
def Quiniela():
    print("\n**************************************")
    print("\n🍀 Q U I N I E L A 🍀")
    dni = pideDni()
    print("\n¿Qué número te gustaría apostar? 🍀")
    while True:
        try: 
            nroQuiniela = int(input("Recuerde que puede ser de 2, 3 o 4 cifras únicamente: "))
            longNro = len(str(nroQuiniela))
            if longNro == 2 or longNro == 3 or longNro == 4: #El número tiene 2, 3, 4 cifras?
                print("\n**************************************")
                print(f'\nEstás por apostar el número {nroQuiniela} ¿Deseas confirmarlo?\n1-Si\n2-No')
                if opcionSiNo() == True:
                    while True:
                        importe = obtenerImporte()
                        if importe >= 4.00: 
                            #El importe es mayor de $4? No solicitaba el ejercicio pero 
                            # investigando sobre quiniela, descubrí que existe un mínimo.
                            print("\n**************************************")
                            print(f'\nEstás por apostar ${importe} ¿Deseas confirmarlo?\n1-Si\n2-No')
                            if opcionSiNo() == True:
                                fechaHora = datetime.datetime.now()
                                cpte = random.randint(1000, 9999) 
                                print("\n**************************************")
                                print(f"\n✨ APUESTA REALIZADA CON ÉXITO ✨\n👉 Apostó ${importe} al número {nroQuiniela}\n")
                                print("**************************************")
                                imprimirCpteQuiniela(nomLocal, fechaHora, cpte, dni, importe, nroQuiniela)
                                return
                        else:
                            print("\n⚠ ¡Atención! El importe debe ser mayor o igual a $4.00\nIngrese otra cifra..")
                else:
                    print("\n**************************************")
                    print("\n¿Qué número te gustaría apostar? 🍀")
            else: 
                print("\n**************************************")
                print("\n⚠ ¡Atención! No es posible utilizar este número para apostar.\nIngrese otro..")
                print("\n**************************************")
        except ValueError:
            print("\n**************************************")
            print("\n¡ATENCIÓN! Debe ingresar un número válido.")

#Procedimiento para imprimir el comprobante de quiniela y guardado en archivo txt
def imprimirCpteQuiniela(nombreQuiniela, fechayhora, cpte, dni, total, apuesta):
    #Imprime comprobante
    print("------ Ticket Comprobante ------\n")
    print(nombreQuiniela)
    print("\nFecha y Hora de la apuesta: ", fechayhora.strftime("%Y-%m-%d %H:%M:%S")) #Con la función strftime puedo ver la fecha correctamente
    print("Número de Comprobante: ", cpte)
    print("DNI del Apostador: ", dni)
    print("Cifra Apostada: ", apuesta)
    print("Total Apostado: ", round(total,2))
    print("-------------------------------")

    #Diccionario para guardar los datos en un txt
    datosTxt = [ {
        "Fecha y Hora": fechayhora.strftime("%Y-%m-%d %H:%M:%S"),
        "Número de Comprobante": cpte,
        "DNI del Apostador": dni,
        "Cifra Apostada": apuesta,
        "Total Apostado": round(total,2)
    }]
        
    #Guardamos el registro en un archivo txt para posterior comparación con la opción 3
    guardarDatostxt(datosTxt, "Quiniela")

#Procedimiento para la opción 2 de Quini6
def Quini6():
    print("\n**************************************")
    print("\n🤞 Q U I N I  6 🤞")
    dni = pideDni()
    print("\n**************************************")
    print ("Tenés que apostar 6️⃣ números. ¿Te gustaría que fuesen al azar? \n\n1-Si\n2-No\n")
    
    if opcionSiNo() == True:
        #Al azar 
        while True:
            print("\n**************************************")
            print("Los números serán escogidos al azar. ¡Que tengas mucha suerte! 🙌")
            listaNrosAzar = random.sample(range(0, 46), 6)  #Se selecciona 6 números al azar con la funcion sample de la libreria random
            print(f"Tu lista de números es {listaNrosAzar}. ¿Estás de acuerdo? \n\n1-Si\n2-No\n")
            if opcionSiNo() == True:
                while True:
                    importe = obtenerImporte()
                    if importe >= 4.00: 
                        print(f'\nEstás por apostar ${importe} ¿Deseas confirmarlo?\n1-Si\n2-No')
                        if opcionSiNo() == True:
                            fechaHora = datetime.datetime.now()
                            cpte = random.randint(1000, 9999) 
                            imprimirCpteQuini6(nomLocal,fechaHora,cpte, dni, importe, listaNrosAzar)
                            return
                    else:
                        print("\n⚠ ¡Atención! El importe debe ser mayor o igual a $4.00\nIngrese otra cifra..")
            else:   
                print("\n**************************************")
    else :
        # Manualmente
        print("\n**************************************")
        print("¡Que tengas mucha suerte! 🙌")
        while True:
            try:
                numeros = []
                #El while carga la lista
                while len(numeros) < 6:
                        num = int(input(f"Ingresá el {len(numeros)+1}° número entre 0 y 45: "))
                        if 00 <= num <= 45:
                            numeros.append(num)
                        else:
                            print("\n**************************************")
                            print("\nEl número ingresado no se encuentra en el intervalo indicado. Por favor, intente de nuevo...")
                print("\n**************************************")
                print(f"Los números son {numeros}. ¿Confirmás la lista?\n1-Si\n2-No\n")
                if opcionSiNo() == True:
                    while True:    
                        importe = obtenerImporte()
                        if importe >= 4.00: 
                            print("\n**************************************")
                            print(f'\nEstás por apostar ${importe} ¿Deseas confirmarlo?\n1-Si\n2-No')
                            if opcionSiNo() == True:
                                fechaHora = datetime.datetime.now()
                                cpte = random.randint(1000, 9999) 
                                imprimirCpteQuini6(nomLocal,fechaHora,cpte, dni, importe, numeros)
                                return
                        else:
                            print("\n**************************************")
                            print("\n⚠ ¡Atención! El importe debe ser mayor o igual a $4.00\nIngrese otra cifra..")
            except ValueError :
                print("\n**************************************")
                print("\n¡ATENCIÓN! Debe ingresar un NÚMERO válido.")
    
#Procedimiento para imprimir el comprobante de la apuesta por Quini6 y guardado en archivo txt
def imprimirCpteQuini6(nombreQuiniela, fechayhora, cpte, dni, total, apuesta):
    print("\n**************************************\n")
    print("------ Ticket Comprobante ------\n")
    print(nombreQuiniela)
    print("\nFecha y Hora de la apuesta: ", fechayhora.strftime("%Y-%m-%d %H:%M:%S")) #Con la función strftime puedo ver la fecha correctamente
    print("Número de Comprobante: ", cpte)
    print("DNI del Apostador: ", dni)
    print("Cifra Apostada: ", apuesta)
    print("Total Apostado: ", round(total,2))
    print("-------------------------------")

    #Diccionario para guardar los datos en un txt
    datosTxt = [ {
        "Fecha y Hora": fechayhora.strftime("%Y-%m-%d %H:%M:%S"),
        "Número de Comprobante": cpte,
        "DNI del Apostador": dni,
        "Cifra Apostada": apuesta,
        "Total Apostado": round(total,2)
    }]
        
    #Guardamos el registro en un archivo txt para posterior comparación con la opción 3
    guardarDatostxt(datosTxt, "Quini6")

#Procedimiento para realizar la carga del ganador con las validaciones correspondientes según el tipo de sorteo
def cargaGanador():
    print("\n**************************************")
    print("🥇 C O M P R O B A C I Ó N 🥇\n")
    print("¿De que sorteo querés ingresar el número Ganador? \n1-🍀 Quiniela \n2-🤞 Quini 6")
    if opcionSiNo() == True:
        #Quiniela
        while True:
            try:
                print("\n**************************************")
                nroGanador = int(input("🏆 Ingrese el número ganador: "))
                longNro = len(str(nroGanador))
                if longNro == 2 or longNro == 3 or longNro == 4:
                    print("\n**************************************")
                    print(f"Carga correcta. El número ganador es {nroGanador}")
                    resultadosArchivo = leerDatos("Quiniela")
                    if not resultadosArchivo:
                       print("No se encontraron registros de apuestas.")
                       return
                    comparaApuestasQuiniela(resultadosArchivo, nroGanador)
                    return
                else:
                    print("¡ATENCIÓN! El número ganador debe tener 2, 3 o 4 cifras.")
            except ValueError:
                print("¡ATENCIÓN! Debe ingresar un número válido.") 
    else:
        #Quini6
        ganadores = []
        print("\n**************************************")
        while len(ganadores) < 6:
                    num = int(input(f"Ingresá el {len(ganadores)+1}° número ganador entre 0 y 45: "))
                    if 00 <= num <= 45:
                        ganadores.append(num)
                    else:
                        print("El número ingresado no se encuentra en el intervalo indicado. Por favor, intente de nuevo...\n ")
        print(f"Carga correcta. Los números ganadores son {ganadores}")
        resultadosArchivo = leerDatos("Quini6")
        if not resultadosArchivo:
            print("No se encontraron registros de apuestas.")
            return
        comparaApuestasQuini6(resultadosArchivo, ganadores)

#Función para leer los datos de cada archivo txt y encontrar el ganador (si es que hay)
def leerDatos(nombre_archivo):
    datos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                valores = linea.strip().split("/")
                registro = {
                    "Fecha y Hora": valores[0],
                    "Número de Comprobante": valores[1],
                    "DNI del Apostador": valores[2],
                    "Cifra Apostada": valores[3],
                    "Total Apostado": valores[4]
                }
                datos.append(registro)
        return datos
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        return []
    except Exception as e:
        print(f"Error al leer los datos desde el archivo: {e}")
        return []

#Procedimiento para comparar el número ganador con los números que se obtienen del archivo QUINIELA
def comparaApuestasQuiniela(datos, nroGanador):
   ganadores = []
   for registro in datos:
        cifra_apostada = registro["Cifra Apostada"]
        #Se utiliza la función eval para convertir la variable en una lista ya que sino no funciona la posterior comparación
        if int(cifra_apostada) == nroGanador:
            ganadores.append(registro)  

   if not ganadores:
        print("\n**************************************")
        print(f"😔 No hay ganadores con el número {nroGanador}.")
   else:
        print("\n**************************************\n")
        print(f"🎉¡Tenemos {len(ganadores)} ganador(es) con el número {nroGanador}!🎊")
        print("\n**************************************")
        for ganador in ganadores:
            print("Número de Comprobante:", ganador["Número de Comprobante"])
            print("DNI del Apostador:", ganador["DNI del Apostador"])
            print("Fecha y Hora de la apuesta:", ganador["Fecha y Hora"])
            print("Cifra Apostada:", ganador["Cifra Apostada"])
            print("Total Apostado:", ganador["Total Apostado"])
            print("------------------------")

#Procedimiento para comparar el número ganador con los números que se obtienen del archivo QUINI6
def comparaApuestasQuini6(datos, nroGanador):
   ganadores = []
   for registro in datos:
        cifra_apostada = registro["Cifra Apostada"]
        cifra_apostada = eval(cifra_apostada)  
        #Se utiliza la función eval para convertir la variable en una lista ya que sino no funciona la posterior comparación
        if set(cifra_apostada) == set(nroGanador):
            ganadores.append(registro)  

   if not ganadores:
        print("\n**************************************")
        print(f"😔 No hay ganadores con el número {nroGanador}.")
   else:
        print("\n**************************************\n")
        print(f"🎉¡Tenemos {len(ganadores)} ganador(es) con el número {nroGanador}!🎊")
        print("\n**************************************")
        for ganador in ganadores:
            print("Número de Comprobante:", ganador["Número de Comprobante"])
            print("DNI del Apostador:", ganador["DNI del Apostador"])
            print("Fecha y Hora de la apuesta:", ganador["Fecha y Hora"])
            print("Cifra Apostada:", ganador["Cifra Apostada"])
            print("Total Apostado:", ganador["Total Apostado"])
            print("------------------------")

#Procedimiento para realizar el arqueo de caja y obtener los número requeridos en el ejercicio
def arqueoCaja():
    print("\n**************************************")
    print("\n💵 A R Q U E O  D E  C A J A 💵")
    #Busca los datos de todos los registros del archivo Quiniela
    fechaHoy = datetime.datetime.now()
    resultadosQuiniela = leerDatos("Quiniela")
    if not resultadosQuiniela:
        print("No se encontraron registros de apuestas para el sorteo de Quiniela.")
        return
    
    #Busca los datos de todos los registros del archivo Quini6
    resultadosQuini6 = leerDatos("Quini6")
    if not resultadosQuini6:
        print("No se encontraron registros de apuestas para el sorteo de Quini6.")
        return

    totalPorDia = totalRecaudado(resultadosQuiniela, resultadosQuini6, fechaHoy)
    print("\n**************************************")
    print(f"💸 El importe total recaudado en el día {fechaHoy.strftime('%d-%m-%Y')} es de $ {totalPorDia}")

    totalNeto = round(recaudacionNeta(totalPorDia))
    print("**************************************")
    print(f"Las ganancias totales que obtuvo 💵 QUINIELA - SIEMPRE SALE 💵 en el día {fechaHoy.strftime('%d-%m-%Y')} es de $ {totalNeto} ")
    print("**************************************")

#Función que lee el contenido de los diccionarios previamente creados y realiza una comparacion de fechas para
#corroborar que las apuestas sean del día, y acumula el total en una variable
def totalRecaudado(datosQuiniela, datosQuini6, fechaTotalR):
    importeTotal = 0 
    for registro in datosQuiniela:
        fechaRegistros= registro.get("Fecha y Hora").split()[0]
        if fechaTotalR.strftime('%Y-%m-%d') == fechaRegistros:
            importeTotal += float(registro.get("Total Apostado",0))

    for registro in datosQuini6 :
        fechaRegistros= registro.get("Fecha y Hora").split()[0]
        if fechaTotalR.strftime('%Y-%m-%d') == fechaRegistros:
            importeTotal += float(registro.get("Total Apostado",0))

    return importeTotal

#Función que obtiene la retención del estado
def recaudacionNeta(totalRecaudado):
    retencion = round(totalRecaudado * 0.47)
    print("**************************************")
    print(f"🧾 La retención que realiza el estado (47%) es un total de $ {retencion}")
    totalNeto = totalRecaudado - retencion
    return totalNeto

#Módulo único y principal
if __name__ == "__main__":
    mostrarMenuPrincipal()


