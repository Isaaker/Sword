print ("SWORD Lite")
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
        print ("B.Create password")
        print ("C.Credits")
        print ("D.Version")
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
            print ("E.Exit")
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
            tipo = input ("Choose")
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
                        contraseña += random.choice(caracteres2)
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
                longitud = input ("Password length, please?")
                #Quantity
                cantidad = input ("How many passwords do you want?")
                cantidad = int(cantidad)
                longitud = int(longitud)
                    #Create
                for p in range(cantidad):
                    contraseña = ""
                    for c in range(longitud):
                        caracteres_numericos = input ("Do you want numeric characters?")
                        if caracteres_numericos == ("Yes"):
                            contraseña += random.choice(caracteres2)   
                        caracteres_letras1 = input ("Do you want capital letters?")
                        if caracteres_letras1 == ("Yes"):
                            contraseña += random.choice(caracteres3)
                        caracteres_letras2 = input ("Do you want lowercase letters?")
                        if caracteres_letras2 == ("Yes"):
                            contraseña += random.choice(caracteres4)
                        caracteres = input ("Do you want special characters?")
                        if caracteres == ("Yes"):
                            contraseña += random.choice(caracteres1)
                        print ("If you have requested more passwords the process will be repeated.")
                        print ("--------")
                        #Delivery
                    print ("----------")
                    print ("Name:")
                    print (nombre)
                    print ("Password:")
                    print (contraseña)
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
