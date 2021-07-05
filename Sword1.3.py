#import
import random 
import time
#Bucle
while True:
#Nombre
    print ("SWORD 1.3")
    print ("                                                      ")
    nombre = input ("Su nombre, por favor.No escriba ningun espacio delante.Se usa puramente para personalizacion:")
    if nombre == ("Administrator"):
        print ("Hello,Administrator")
        id = input ("I need your ID")
        while id == ("Piscina de Entropia"):
            contraseña1 = input ("I need your password")
            while contraseña1 == ("M/W7Z6#cU_1Q"):
                print ("This is the information to you we need")
                print ("©piscinadeentropia.es 2021/Author:Isaaker/Programado con una:Raspberry Pi 400/Usando:Thonny Python IDE/Version 1.3 Sword")
                print ("This program inclued this modules: Random and time")
                print ("And this ERROR codes:104= La informacion introducida no es correcta o no es la esperada And this:109 Se ha acabado el Bucle de forma inesperada")
                print ("Use Ctrl+tecla c for exit")
                print ("-------")
                time.sleep (5)
                break
                time.sleep (4)
            else:
                print ("This is  not correct")
        while id == ("Developer"):
            contraseña2 = input ("I need your password")
            while contraseña2 == ("m%YM%mBep7:f"):
                print ("This is the information to you we need")
                print ("©Piscinadeentropia.es 2021/Author:Isaaker/Programado con una:Raspberry Pi 400/Usando:Thonny Python IDE/Version 1.3 Sword")
                print ("This program inclued this modules: Random , time ,datetime and timeit")
                print ("And this ERROR codes:104= La informacion introducida no es correcta o no es la esperada And this:109 Se ha acabado el Bucle de forma inesperada")
                print ("Use Ctrl+tecla c for exit")
                print ("-------")
                time.sleep (5)
                break
                time.sleep (4)
            else:
                print ("This is  not correct")
    if nombre == ("Sword"):
        print ("¡¡¡Oye pues yo tambien me llamo asi!!!")
    else:
        print ("Bienvenid@a:")
        print (nombre)
        #Definicion de los caracteres
        caracteres4 = ("asdfghjklñqwertyuiopzxcvbnm")
        caracteres3 = ("QWERTYUIOPASDFGHJKLÑZXCVBNM")
        caracteres2 = ("1234567890")
        caracteres1 = ("#@¡!+-_.,=&%$/*:;ªº")
        #Start Menu opciones
        print ("A.¿Que eres?")
        print ("B.Crear contraseña")
        print ("C.Creditos")
        print ("D.Version")
        print ("E.Informar de un fallo")
        print ("?(Ayuda)")
        userName = input ("Elije una opcion")
        #¿Que eres?
        if userName == ("?"):
            print ("Hola Bienvenido a el portal de Ayuda")
            time.sleep (1)
            print ("Aqui podras encontrar informacion importante acerca de este programa")
            time.sleep (1)
            print ("------------------------------")
            print ("A.Instrucciones de Uso")
            print ("B.Consultar Manual")
            print ("C.Acceder al portal de Tecnico/Administrador")
            print ("D.Crear Contraseñas")
            print ("E.Salir")
            time.sleep (2)
            help1 = input ("¿En que te puedo ayudar?")
            if help1 == ("a"):
                print ("                                                                                                                                              ")
                print ("Instrucciones de uso de Sword 1.3:")
                print ("Para Comenzar Sword le preguntara su nombre por razones puramente de personalizacion, una vez que lo obtenga le mostrara un  menu con letras delante SOLO DEBE TECLEAR LA LETRA aunque se encuentre en mayusculas tecle la letra en minusculas. Despues de obtener sus seleccion le llevara a su eleccion,  siendo el caso de Crear Contraseña a otro menu (Leer Articulo de Ayuda sobre: Crear Contraseñas).")
            if help1 == ("b"):
                print ("Para consultar el Manual completo busque un archivo llamado SwordManual1_3 incluido en el zip descargado, si no lo encuentra vuelva a descargar el zip")
            if help1 == ("c"):
                print ("Para acceder al portl Tecnico/Administrativo necesitara  una ID este portal es solo para el uso de la empresa pero si se solicita cabe la posibilidad de que se conceda el acceso")
            if help1 == ("d"):
                print ("Para Crear una contraseña debes dirigirte al respectivo menu (leer Instrucciones de Uso) despues le preguntara si desea un PIN que es igual que lo que usa para desbloquear el telefono o una Contraseña Normal que es lo que usas por ejemplo para desbloquear un ordenador y desppues te realizara unas cuantas preguntas mas y... Listo!")
            if help1 == ("e"):
                       print ("Cerrando...")
                       time.sleep (2)
            print ("Si necesitas mas ayuda Contacta con: DARK SISTEMYS o LAKPAD TECHNOLOGIES ambas compañias de Planasa s.a Group")
            time.sleep(2)
        if userName == "a":
            print ("Soy un programa llamado Sword que se usa para generar contraseñas seguras")
            time.sleep(4)
        #Version
        if userName == "b":
            print ("Actualmente se encuentra en la version 1.3 de Sword,Version Española")
        #ERRORES
        if userName == "e":
            print ("Para informar de un ERROR debera contactar con DARK SISTEMYS O LAKPAD TECCHNOLOGIES.Puede hacerlo en el siguiente correo electronico:hernan.marti.isaac@gmail.com o en la cuenta  de GitHub:Isaaker.Gracias de antemano por tu colaboracion")
        #Creditos    
        if userName == "c":
            print ("©Piscinadeentropia.es 2021/Author:Isaaker/Programado con una:Raspberry Pi 400/Usando:Thonny Python IDE/Version 1.3 Sword")
            print ("Para ver la licencia del programa dirigete a: https://github.com/Isaaker/Sword/blob/main/LICENSE.txt")
            time.sleep(10)
        #Creador de Contraseñas
                #Preferencias de la contraseña
        if userName == "d":
            print ("A.PIN")
            print ("B.Contraseña normal")
            tipo = input ("Elije")
            if tipo == ("a"):
                 #Longitud
                longitud = input ("¿Longitud de la Contraseña, por favor?")
                #Cantidad
                cantidad = input ("¿Cuantas contraseñas deseas?")
                cantidad = int(cantidad)
                longitud = int(longitud)
                    #Creacion
                for p in range(cantidad):
                    contraseña = ""
                    for c in range(longitud):
                        contraseña += random.choice(caracteres2)
                        #Entrega
                    print ("----------")
                    print ("Nombre:")
                    print (nombre)
                    print ("Contraseña:")
                    print (contraseña)
                #Asistente
                print ("---------")
                print (nombre)
                print ("tus contraseña o contraseñas estan listas mas arriba")
                time.sleep(4)
                print ("Gracias por usar nuestro programa")
                time.sleep(4)
            if tipo ==  ("b"):
                #Longitud
                longitud = input ("¿Longitud de la Contraseña, por favor?")
                #Cantidad
                cantidad = input ("¿Cuantas contraseñas deseas?")
                cantidad = int(cantidad)
                longitud = int(longitud)
                    #Creacion
                for p in range(cantidad):
                    contraseña = ""
                    for c in range(longitud):
                        caracteres_numericos = input ("¿Quieres caracteres numericos?")
                        if caracteres_numericos == ("Si"):
                            contraseña += random.choice(caracteres2)   
                        caracteres_letras1 = input ("¿Quieres letras mayusculas?")
                        if caracteres_letras1 == ("Si"):
                            contraseña += random.choice(caracteres3)
                        caracteres_letras2 = input ("¿Quiere letras minusculas?")
                        if caracteres_letras2 == ("Si"):
                            contraseña += random.choice(caracteres4)
                        caracteres = input ("¿Quieres Caracteres especiales?")
                        if caracteres == ("Si"):
                            contraseña += random.choice(caracteres1)
                        print ("Si ha solicitado mas contraseñas el proceso se repetira")
                        print ("--------")
                        #Entrega
                    print ("----------")
                    print ("Nombre:")
                    print (nombre)
                    print ("Contraseña:")
                    print (contraseña)
                #Asistente
                print ("---------")
                time.sleep (4)
                print (nombre)
                print ("tus contraseña o contraseñas estan listas mas arriba")
                time.sleep(4)
                print ("Gracias por usar nuestro programa")
                time.sleep(4)
        #Asistente de inicio/fin
    print ("                                                                                                                                                                                                             ")
    print ("Indique salir para que el programa no se reinicie, en el caso de que lo quiera volver a usar escriba Continuar.")
    reiniciar = input ("Elija: A.Salir o B.Continuar")
    #Salida
    if reiniciar == ("a"):
        print ("Hasta luego")
        break
    #Reinicio
    if reiniciar == ("b"):
        print ("Se reiniciara en breve...")
        time.sleep (5)
print ("Posible ERROR 109")
#Final del programa
