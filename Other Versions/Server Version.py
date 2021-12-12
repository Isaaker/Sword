# To download, wpget https://raw.githubusercontent.com/Isaaker/Sword/main/Server%20Version
#import
import random 
import time
print ("        SWORD LITE      ")
print ("  Powered By: Phyton 3")
print ("      ©Isaac Hernán")
#characters
characters4 = ("asdfghjklñqwertyuiopzxcvbnm")
characters3 = ("QWERTYUIOPASDFGHJKLÑZXCVBNM")
characters2 = ("1234567890")
characters1 = ("#@¡!+-_.,=&%$/*:;ªº")
unificado = ("asdfghjklñqwertyuiopzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890#@¡!+-_.,=&%$/*:;ªº")
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
print ("F.Exit")
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
        print ("See the source code at: https://github.com/Isaaker/Sword")
    if help1 == ("c"):
        print ("Se license at: https://github.com/Isaaker/Sword/blob/main/LICENSE.txt")
    if help1 == ("d"):
        print ("To create a password you must go to the respective menu (read Instructions for Use) then it will ask you if you want a PIN which is the same as what you use to unlock the phone or a Normal Password which is what you use for example to unlock a computer and then it will ask you a few more questions and... Done")
    if help1 == ("e"):
        print ("See te oficial page in: https://piscinadeentropia.es/Sword")
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
        #Create
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
    if tipo == ("b"):
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
if userName == ("f"):
    exit()
#End
print ("Sword Lite")

