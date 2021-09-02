print ("SWORD Lite")
#import
import random 
import time
import webbrowser
#characters
characters4 = ("asdfghjklñqwertyuiopzxcvbnm")
characters3 = ("QWERTYUIOPASDFGHJKLÑZXCVBNM")
characters2 = ("1234567890")
characters1 = ("#@¡!+-_.,=&%$/*:;ªº")
unificado = ("asdfghjklñqwertyuiopzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890#@¡!+-_.,=&%$/*:;ªº")
#Language
time.sleep (2)
print ("a. English")
print ("b. Español")
language = input ("Choose a language / Elije un Idioma ")
if language == ("a"):
    print ("You have chosen English")
    while True:
        #Name
        print ("                                                      ")
        nombre = input ("Your name please ")
        if nombre == ("Sword"):
            print ("Hey, that's my name too!!!")
        else:
            print ("Welcome:")
            print (nombre)
            #Start Menu opciones
        print ("A.What are you?")
        print ("B.Version")
        print ("C.Credits")
        print ("D.Create password")
        print ("E.Report an error")
        print ("?.Help")
        userName = input ("Choose an option ")
        #¿Que eres?
        if userName == ("?"):
            print ("Welcome to the Help Portal")
            time.sleep (1)
            print ("Here you can find important information about this program.")
            time.sleep (1)
            print ("------------------------------")
            print ("A.Instructions for Use")
            print ("B.Consult Source Code")
            print ("C.Consult the license")
            print ("D.Create Passwords")
            print ("E.Visit Sword's official website")
            print ("F.Exit")
            time.sleep (2)
            help1 = input ("How can I help you? ")
            if help1 == ("a"):
                print ("                                                                                                                                              ")
                print ("Instructions for use Sword:")
                print ("To start Sword will ask you for your language, then your name for purely personalization reasons, once you get it it will show you a menu with letters in front of it, you ONLY MUST TYPE THE LETTER even if it is in upper case type the letter in lower case. After getting your selection it will take you to your choice, being the case of Create Password to another menu (Read Help Article on: Create Passwords).")
            if help1 == ("b"):
                print ("To consult the source code go to: https://github.com/Isaaker/Sword")
            if help1 == ("c"):
                print ("To consult the license go to: https://github.com/Isaaker/Sword/blob/main/LICENSE.txt")
            if help1 == ("d"):
                print ("To create a password you must go to the respective menu (read Instructions for Use) then it will ask you if you want a PIN which is the same as what you use to unlock the phone or a Normal Password which is what you use for example to unlock a computer and then it will ask you a few more questions and... Done")
            if help1 == ("e"):
                webbrowser.open(
    'https://piscinadeentropia.es/Sword'
)
            if help1 == ("f"):
                       print ("Closing...")
                       time.sleep (2)
        if userName == "a":
            print ("I am a program called Sword that is used to generate secure passwords.")
            time.sleep(4)
        #Version
        if userName == "b":
            print ("You are currently in the Lite version of Sword")
        #ERRORES
        if userName == "e":
            print ("To report an ERROR you can do it in the following email electronico:hernan.marti.isaac@gmail.com or in the GitHub account:Isaaker. Thanks in advance for your collaboration")
        #Creditos    
        if userName == "c":
            print ("Author:Isaaker/Programmed with a:Raspberry Pi 400/Using:Thonny Python IDE/Version Lite de Sword")
            print ("To see the program license go to: https://github.com/Isaaker/Sword/blob/main/LICENSE.txt")
            time.sleep(10)
        #Creador de Contraseñas
        if userName == "d":
            #Preference
            print ("A.PIN")
            print ("B.Password")
            tipo = input ("Choose ")
            if tipo == ("a"):
                #Leght
                longitud = input ("Password length, please?")
                #Quantity
                cantidad = input ("How many passwords do you want?")
                cantidad = int(cantidad)
                longitud = int(longitud)
                    #Crete
                for p in range(cantidad):
                    contraseña = ""
                    for c in range(longitud):
                        contraseña += random.choice(characters2)
                        #Delivery
                    print ("----------")
                    print ("Name:")
                    print (nombre)
                    print ("Password:")
                    print (contraseña)
                #Asistant
                print ("---------")
                print (nombre)
                print ("your password(s) are listed above")
                time.sleep(4)
                print ("Thank you for using our program")
                time.sleep(4)
            if tipo ==  ("b"):
                #Length
                longitud = input ("Password length, please? ")
                #Quantity
                cantidad = input ("How many passwords do you want? ")
                cantidad = int(cantidad)
                longitud = int(longitud)
                print("A. Generate password")
                print("B. Advanced Settings")
                creatormenu = input ("")
                    #Create
                if creatormenu == ("a"):
                    for p in range(cantidad):
                        contraseña = ""
                        for c in range(longitud):
                            contraseña += random.choice(unificado)
                        print ("If you have requested more passwords the process will be repeated.")
                        print ("--------")
                        #Delivery
                        print ("----------")
                        print ("Name:")
                        print (nombre)
                        print ("Password:")
                        print (contraseña)
                if creatormenu == ("b"):
                    print ("Not available")
                    time.sleep (2000)
                #Asistant
                print ("---------")
                time.sleep (4)
                print (nombre)
                print ("your password(s) are listed above")
                time.sleep(4)
                print ("Thank you for using our program")
                time.sleep(4)
        #Start / End
        print ("                                                                                                                                                                                                             ")
        print ("Indicate A to turn off the program, otherwise indicate B.")
        reiniciar = input ("Choose: A.Exit or B.Continue ")
        #Exit
        if reiniciar == ("a"):
            print ("See you later")
            break
        #Reboot
        if reiniciar == ("b"):
            print ("It will be restarted shortly...")
            time.sleep (5)
        else:
            break
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
        print ("B.Version")
        print ("C.Creditos")
        print ("D.Crear contraseña")
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
            print ("E. Ver la pagina oficial de Sword")
            print ("F.Salir")
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
                webbrowser.open(
    'https://piscinadeentropia.es/Sword'
)

            if help1 == ("f"):
                print ("Cerrando...")
                time.sleep (2)
            
                
        if userName == "a":
            print ("Soy un programa llamado Sword que se usa para generar contraseñas seguras")
            time.sleep(4)
        #Version
        if userName == "b":
            print ("Actualmente se encuentra en la version Lite de Sword")
        #ERRORES
        if userName == "e":
            print ("Para informar de un ERROR puede hacerlo en el siguiente correo electronico:hernan.marti.isaac@gmail.com o en la cuenta  de GitHub:Isaaker.Gracias de antemano por tu colaboracion")
        #Creditos    
        if userName == "c":
            print ("Author:Isaaker/Programado con una:Raspberry Pi 400/Usando:Thonny Python IDE/Version Lite de Sword")
            print ("Para ver la licencia del programa dirigete a: https://github.com/Isaaker/Sword/blob/main/LICENSE.txt")
            time.sleep(10)
        #Creador de Contraseñas
        if userName == "d":
            #Preference
            print ("A.PIN")
            print ("B.Contraseña normal")
            tipo = input ("Elije ")
            if tipo == ("a"):
                #Leght
                longitud = input ("¿Longitud de la contraseña?")
                #Quantity
                cantidad = input ("¿Cuantas contraseñas necesitas?")
                cantidad = int(cantidad)
                longitud = int(longitud)
                    #Crete
                for p in range(cantidad):
                    contraseña = ""
                    for c in range(longitud):
                        contraseña += random.choice(characters2)
                        #Delivery
                    print ("----------")
                    print ("Nombre:")
                    print (nombre)
                    print ("Contraseña:")
                    print (contraseña)
                #Asistant
                print ("---------")
                print (nombre)
                print ("Tus contraseñas las podras encontrar debajo")
                time.sleep(4)
                print ("Gracias por usar nuestro programa")
                time.sleep(4)
            if tipo ==  ("b"):
                #Length
                longitud = input ("¿Longitud de la contraseña? ")
                #Quantity
                cantidad = input ("¿Cuantas contraseñas necesitas? ")
                cantidad = int(cantidad)
                longitud = int(longitud)
                print("A. Generar contraseña")
                print("B. Ajustes advanzados")
                creatormenu = input ("")
                    #Create
                if creatormenu == ("a"):
                    for p in range(cantidad):
                        contraseña = ""
                        for c in range(longitud):
                            contraseña += random.choice(unificado)
                        print ("--------")
                        #Delivery
                        print ("----------")
                        print ("Nombre:")
                        print (nombre)
                        print ("Contraseña:")
                        print (contraseña)
                if creatormenu == ("b"):
                    print ("No disponible")
                    time.sleep (2000)
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
        else:
            break
#End
print ("Sword Lite")
