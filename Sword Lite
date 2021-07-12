print ("SWORD 1.3")
#import
import random 
import time
#characters
characters4 = ("asdfghjklñqwertyuiopzxcvbnm")
characters3 = ("QWERTYUIOPASDFGHJKLÑZXCVBNM")
characters2 = ("1234567890")
characters1 = ("#@¡!+-_.,=&%$/*:;ªº")
#Language
time.sleep (2)
print ("a. English")
print ("b. Español")
language = input ("Choose a language / Elije un Idioma ")
if language == ("a"):
    print ("You have chosen English")
    print ("Language not avaible")
if language == ("b"):
    #Español
    print ("Has elejido Español")
    while True:
        #Name
        print ("                                                      ")
        nombre = input ("Su nombre por favor ")
        if nombre == ("Sword"):
            print ("¡¡¡Oye pues yo tambien me llamo asi!!!")
        else:
            print ("Bienvenid@a:")
            print (nombre)
            #Start Menu opciones
        print ("A.¿Que eres?")
        print ("B.Crear contraseña")
        print ("C.Creditos")
        print ("D.Version")
        print ("E.Informar de un fallo")
        print ("?(Ayuda)")
        userName = input ("Elije una opcion ")
        #¿Que eres?
        if userName == ("?"):
            print ("Hola Bienvenido a el portal de Ayuda")
            time.sleep (1)
            print ("Aqui podras encontrar informacion importante acerca de este programa")
            time.sleep (1)
            print ("------------------------------")
            print ("A.Instrucciones de Uso")
            print ("B.Consultar Codigo Fuente")
            print ("C.Consultar la licencia")
            print ("D.Crear Contraseñas")
            print ("E.Salir")
            time.sleep (2)
            help1 = input ("¿En que te puedo ayudar? ")
            if help1 == ("a"):
                print ("                                                                                                                                              ")
                print ("Instrucciones de uso de Sword 1.3:")
                print ("Para Comenzar Sword le preguntara su idioma, despues su nombre por razones puramente de personalizacion, una vez que lo obtenga le mostrara un  menu con letras delante SOLO DEBE TECLEAR LA LETRA aunque se encuentre en mayusculas tecle la letra en minusculas. Despues de obtener sus seleccion le llevara a su eleccion,  siendo el caso de Crear Contraseña a otro menu (Leer Articulo de Ayuda sobre: Crear Contraseñas).")
            if help1 == ("b"):
                print ("Para consultar el codigo fuente dirigete a: https://github.com/Isaaker/Sword")
            if help1 == ("c"):
                print ("Para consultar la licencia dirigete a: https://github.com/Isaaker/Sword/blob/main/LICENSE.txt")
            if help1 == ("d"):
                print ("Para Crear una contraseña debes dirigirte al respectivo menu (leer Instrucciones de Uso) despues le preguntara si desea un PIN que es igual que lo que usa para desbloquear el telefono o una Contraseña Normal que es lo que usas por ejemplo para desbloquear un ordenador y despues te realizara unas cuantas preguntas mas y... Listo!")
            if help1 == ("e"):
                       print ("Cerrando...")
                       time.sleep (2)
        if userName == "a":
            print ("Soy un programa llamado Sword que se usa para generar contraseñas seguras")
            time.sleep(4)
        #Version
        if userName == "b":
            print ("Actualmente se encuentra en la version 1.3 de Sword,Version Española")
        #ERRORES
        if userName == "e":
            print ("Para informar de un ERROR puede hacerlo en el siguiente correo electronico:hernan.marti.isaac@gmail.com o en la cuenta  de GitHub:Isaaker.Gracias de antemano por tu colaboracion")
        #Creditos    
        if userName == "c":
            print ("Author:Isaaker/Programado con una:Raspberry Pi 400/Usando:Thonny Python IDE/Version 1.3 Sword")
            print ("Para ver la licencia del programa dirigete a: https://github.com/Isaaker/Sword/blob/main/LICENSE.txt")
            time.sleep(10)
        #Creador de Contraseñas
        if userName == "d":
            #Preference
            print ("A.PIN")
            print ("B.Contraseña normal")
            tipo = input ("Elije")
            if tipo == ("a"):
                #Leght
                longitud = input ("¿Longitud de la Contraseña, por favor?")
                #Quantity
                cantidad = input ("¿Cuantas contraseñas deseas?")
                cantidad = int(cantidad)
                longitud = int(longitud)
                    #Crete
                for p in range(cantidad):
                    contraseña = ""
                    for c in range(longitud):
                        contraseña += random.choice(caracteres2)
                        #Delivery
                    print ("----------")
                    print ("Nombre:")
                    print (nombre)
                    print ("Contraseña:")
                    print (contraseña)
                #Asistant
                print ("---------")
                print (nombre)
                print ("tus contraseña o contraseñas estan listas mas arriba")
                time.sleep(4)
                print ("Gracias por usar nuestro programa")
                time.sleep(4)
            if tipo ==  ("b"):
                #Length
                longitud = input ("¿Longitud de la Contraseña, por favor?")
                #Quantity
                cantidad = input ("¿Cuantas contraseñas deseas?")
                cantidad = int(cantidad)
                longitud = int(longitud)
                    #Create
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
                        #Delivery
                    print ("----------")
                    print ("Nombre:")
                    print (nombre)
                    print ("Contraseña:")
                    print (contraseña)
                #Asistant
                print ("---------")
                time.sleep (4)
                print (nombre)
                print ("tus contraseña o contraseñas estan listas mas arriba")
                time.sleep(4)
                print ("Gracias por usar nuestro programa")
                time.sleep(4)
        #Start / End
        print ("                                                                                                                                                                                                             ")
        print ("Indique A para apagar el programa, de lo contrario indique B.")
        reiniciar = input ("Elija: A.Salir o B.Continuar ")
        #Exit
        if reiniciar == ("a"):
            print ("Hasta luego")
            break
        #Reboot
        if reiniciar == ("b"):
            print ("Se reiniciara en breve...")
            time.sleep (5)
#End
print ("Sword 1.3")
