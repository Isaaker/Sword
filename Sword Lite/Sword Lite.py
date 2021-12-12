#import
import random 
import time
import webbrowser
print ("        SWORD LITE      ")
print ("  Powered By: Phyton 3")
print ("      ©Isaac Hernán")
#characters
characters10 = ("QWERTYUIOPASDFGHJKLZXCVBNM#@¡!+-_.,=&%$/*:;ªº")
characters9 = ("#@¡!+-_.,=&%$/*:;ªºasdfghjklqwertyuiopzxcvbnm")
characters8 = ("#@¡!+-_.,=&%$/*:;ªº1234567890")
characters7 = ("QWERTYUIOPASDFGHJKLZXCVBNM1234567890")
characters6 = ("asdfghjklqwertyuiopzxcvbnm1234567890")
characters5 = ("asdfghjklñqwertyuiopzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
characters4 = ("asdfghjklqwertyuiopzxcvbnm")
characters3 = ("QWERTYUIOPASDFGHJKLZXCVBNM")
characters2 = ("1234567890")
characters1 = ("#@¡!+-_.,=&%$/*:;ªº")
unificado = ("asdfghjklñqwertyuiopzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890#@¡!+-_.,=&%$/*:;ªº")
#Language
while True:
    time.sleep (2)
    print ("A. English")
    print ("B. Español")
    language = input ("Choose a language / Elije un Idioma ")
    if language == ("a"):
        print ("You have chosen English")
        print ("                                                      ")
        nombre = input ("Your name please ")
        if nombre == ("Sword"):
            print ("Hey, that's my name too!!!")
        if nombre == ("Isaaker"):
            print ("Hello Father")
        else:
            print ("Welcome:")
            print (nombre)
        while True:
            #Start Menu opciones
            print (" ")
            print ("A.What are you?")
            print ("B.Version")
            print ("C.Credits")
            print ("D.Create password")
            print ("E.Report an error o make a issue")
            print ("F.Exit")
            print ("?.Help")
            userName = input ("Choose an option ")
            print (" ")
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
                    webbrowser.open(
        'https://github.com/Isaaker/Sword'
    )
                if help1 == ("c"):
                    print ("A browser window will open shortly.")
                    webbrowser.open(
        'https://github.com/Isaaker/Sword/blob/main/LICENSE.txt'
    )
                if help1 == ("d"):
                    print ("To create a password you must go to the respective menu (read Instructions for Use) then it will ask you if you want a PIN which is the same as what you use to unlock the phone or a Normal Password which is what you use for example to unlock a computer and then it will ask you a few more questions and... Done")
                if help1 == ("e"):
                    print ("A browser window will open shortly.")
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
                webbrowser.open("https://github.com/Isaaker/Sword/issues/new")
            #Creditos    
            if userName == "c":
                print ("Author:Isaaker, Powered by: Phyton 3, Stored at: GitHub, Under License: Creative Commons Attribution-ShareAlike 4.0 International Public License.")
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
                    print("A. Generate password (All character types are used)")
                    print("B. Advanced Settings (You can select which characters you want to use)")
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
                        print ("A.Only letters")
                        print ("B.Uppercase only")
                        print ("C.Capital letters and letters")
                        print ("D.Letters and Numbers")
                        print ("E.Capitalization and Numbers")
                        print ("F.Special characters only")
                        print ("G.Letters and Characters")
                        print ("H.Capitalization and Characters")
                        print ("I.Numbers and Characters")
                        print ("J.Exit")
                        print ("TO USE ONLY NUMBERS USE THE PIN OPTION")
                        avanzado = input ("")
                        if avanzado == ("a"):
                           for p in range(cantidad):
                            contraseña = ""
                            for c in range(longitud):
                                contraseña += random.choice(characters4)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Name:")
                            print (nombre)
                            print ("Password:")
                            print (contraseña)
                        if avanzado == ("b"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters3)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Name:")
                            print (nombre)
                            print ("Password:")
                            print (contraseña)
                        if avanzado == ("c"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters5)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Name:")
                            print (nombre)
                            print ("Password:")
                            print (contraseña)
                        if avanzado == ("d"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters6)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Name:")
                            print (nombre)
                            print ("Password:")
                            print (contraseña)
                        if avanzado == ("e"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters7)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Name:")
                            print (nombre)
                            print ("Password:")
                            print (contraseña)
                        if avanzado == ("f"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters1)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Nombre:")
                            print (nombre)
                            print ("Contraseña:")
                            print (contraseña)
                        if avanzado == ("g"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters9)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Name:")
                            print (nombre)
                            print ("Password:")
                            print (contraseña)
                        if avanzado == ("i"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters8)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Name:")
                            print (nombre)
                            print ("Password:")
                            print (contraseña)
                        if avanzado == ("h"):
                            for p in range(cantidad):
                             for c in range(longitud):
                                 contraseña += random.choice(characters10)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Name:")
                            print (nombre)
                            print ("Password:")
                            print (contraseña)
                        if avanzado == ("j"):
                            break
                    #Asistant
                    print ("---------")
                    time.sleep (4)
                    print (nombre)
                    print ("your password(s) are listed above")
                    time.sleep(4)
                    #Start / End
            if userName == ("f"):
                print ("Thank you for using our program")
                print ("Sword Lite")
                exit()
    if language == ("b"):
        #Español
        print ("Has elejido Español")
        print ("                                                      ")
        nombre = input ("Su nombre por favor ")
        if nombre == ("Sword"):
            print ("¡¡¡Oye pues yo tambien me llamo asi!!!")
        if nombre == ("Isaaker"):
            print ("Hola padre")
        else:
            print ("Bienvenid@a:")
            print (nombre)
        while True:
            #Start Menu opciones
            print (" ")
            print ("A.¿Que eres?")
            print ("B.Version")
            print ("C.Creditos")
            print ("D.Crear contraseña")
            print ("E.Informar de un fallo o crear una sugerencia")
            print ("F.Salir")
            print ("?(Ayuda)")
            userName = input ("Elije una opcion ")
            print (" ")
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
                print ("E.Ver la pagina oficial de Sword")
                print ("F.Salir")
                time.sleep (2)
                help1 = input ("¿En que te puedo ayudar? ")
                if help1 == ("a"):
                    print ("                                                                                                                                              ")
                    print ("Instrucciones de uso de Sword 1.3:")
                    print ("Para Comenzar Sword le preguntara su idioma, despues su nombre por razones puramente de personalizacion, una vez que lo obtenga le mostrara un  menu con letras delante SOLO DEBE TECLEAR LA LETRA aunque se encuentre en mayusculas tecle la letra en minusculas. Despues de obtener sus seleccion le llevara a su eleccion,  siendo el caso de Crear Contraseña a otro menu (Leer Articulo de Ayuda sobre: Crear Contraseñas).")
                if help1 == ("b"):
                    print ("En breve se abrira una ventana del navegador")
                    webbrowser.open(
        'https://github.com/Isaaker/Sword'
    )
                if help1 == ("c"):
                    print ("En breve se abrira una ventana del navegador")
                    webbrowser.open(
        'https://github.com/Isaaker/Sword/blob/main/LICENSE.txt'
    )
                if help1 == ("d"):
                    print ("Para Crear una contraseña debes dirigirte al respectivo menu (leer Instrucciones de Uso) despues le preguntara si desea un PIN que es igual que lo que usa para desbloquear el telefono o una Contraseña Normal que es lo que usas por ejemplo para desbloquear un ordenador y despues te realizara unas cuantas preguntas mas y... Listo!")
                if help1 == ("e"):
                    print ("En breve se abrira una ventana del navegador")
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
                webbrowser.open("https://github.com/Isaaker/Sword/issues/new")
            #Creditos    
            if userName == "c":
                print ("Autor: Isaac Hernán, Powered: Phyton 3, Almacenado en: GitHub, Bajo licencia: Creative Commons Attribution-ShareAlike 4.0 International Public License.")
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
                    print("A. Generar contraseña (Se utilizaran todos los tipos de caracteres)")
                    print("B. Ajustes advanzados (Puede seleccionar los caracteres que desea utilizar)")
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
                        print ("A.Solo letras")
                        print ("B.Solo Mayusculas")
                        print ("C.Mayusculas y letras")
                        print ("D.Letras y Numeros")
                        print ("E.Mayusculas y Números")
                        print ("F.Solo Caracteres especiales")
                        print ("G.Letras y Caracteres")
                        print ("H.Mayusculas y Caracteres")
                        print ("I.Numeros y Caracteres")
                        print ("J.Salir")
                        print ("PARA USAR SOLO NUMEROS USA LA OPCION PIN")
                        avanzado = input ("")
                        if avanzado == ("a"):
                           for p in range(cantidad):
                            contraseña = ""
                            for c in range(longitud):
                                contraseña += random.choice(characters4)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Nombre:")
                            print (nombre)
                            print ("Contraseña:")
                            print (contraseña)
                        if avanzado == ("b"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters3)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Nombre:")
                            print (nombre)
                            print ("Contraseña:")
                            print (contraseña)
                        if avanzado == ("c"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters5)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Nombre:")
                            print (nombre)
                            print ("Contraseña:")
                            print (contraseña)
                        if avanzado == ("d"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters6)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Nombre:")
                            print (nombre)
                            print ("Contraseña:")
                            print (contraseña)
                        if avanzado == ("e"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters7)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Nombre:")
                            print (nombre)
                            print ("Contraseña:")
                            print (contraseña)
                        if avanzado == ("f"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters1)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Nombre:")
                            print (nombre)
                            print ("Contraseña:")
                            print (contraseña)
                        if avanzado == ("g"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters9)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Nombre:")
                            print (nombre)
                            print ("Contraseña:")
                            print (contraseña)
                        if avanzado == ("i"):
                            for p in range(cantidad):
                             contraseña = ""
                             for c in range(longitud):
                                 contraseña += random.choice(characters8)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Nombre:")
                            print (nombre)
                            print ("Contraseña:")
                            print (contraseña)
                        if avanzado == ("h"):
                            for p in range(cantidad):
                             for c in range(longitud):
                                 contraseña += random.choice(characters10)
                            print ("--------")
                            #Delivery
                            print ("----------")
                            print ("Nombre:")
                            print (nombre)
                            print ("Contraseña:")
                            print (contraseña)
                        if avanzado == ("j"):
                            break
            if userName == ("f"):
                print ("Gracias por usar nuestro programa")
                print ("Sword Lite")
                exit()
#End
