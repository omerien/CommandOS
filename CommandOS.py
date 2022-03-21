# -*- coding: utf-8 -*-
#UTF8
#CommandOS by omerien
#This script does not follow the rule "We are all consentant adults" and there are many verifications in the script 
#Maybe because its programmer is a kid ?
#Anyway, enjoy the script !
import os         #
import math       # Importing a few modules...
import random     #
_asklanguage = True                #
_askcommand = True                 #
#_askos = True                      #
CONST_goldennumber = 1.618033989   #
lang = ""                          # Setting some variables for the future...
math_result = ""                   # (Some variables are defined directly into the script)
_mathcontinue = True               #
_mathexecute = False               #
_mathexecuted = False              #
_mathhadanerror = False            #
_math0 = False                     #            
def tip():
    tip_randint1 = random.randrange(1, 11, 1)                              
    if tip_randint1 == 10:                                                 
        tip_randint2 = random.randrange(1, 5, 1)                           
        if tip_randint2 == 1:                                              
            if lang == "fr" or lang == "FR":                               
                print("Tip : N'oubliez pas de mettre ce script à jour !")
            elif lang == "en" or lang == "EN":                             
                print("Tip : Don't forget to update your script !")        
        elif tip_randint2 == 2:                                              
            if lang == "fr" or lang == "FR":                               
                print("Tip : Je suis un Tip ! Je peux vous donner quelques infos utiles dans l'utilisation de CommandOS ! (J'apparais une fois sur 10 !)")
            elif lang == "en" or lang == "EN":                               
                print("Tip : I am a tip ! I can give you some useful informations about CommandOS ! (I appear one time per 10 !)")
        elif tip_randint2 == 3:
            if lang == "fr" or lang == "FR":                               
                print("Tip : Vous pouvez utiliser les opérateurs suivants dans la commande math : +, -, X, / et \"carre\"")
            elif lang == "en" or lang == "EN":                               
                print("Tip : You can use the following operators in the math command : +, -, X, / et \"square\"")
        elif tip_randint2 == 4:
            if lang == "fr" or lang == "FR":                               
                print("Tip : La documentation sera disponible à l'adresse github.com/omerien/CommandOS/blob/master/DOCS_FR.md")
            elif lang == "en" or lang == "EN":                               
                print("Tip : The documentation will be available at the web adress github.com/omerien/CommandOS/blob/master/DOCS_EN.md")
#while _askos:
#    useros = input("What is your OS ? (Mac OS, Windows or Linux) : ")
#    if useros == "Windows" or useros == "Mac OS" or useros == "Linux":
#        _askos = False
#    else:
#        print("Invalid OS.")
while _asklanguage:    #...and here we go !
    lang = input("What is your language code ? (FR or EN) : ")
    if lang == "FR" or lang == "fr":
        _asklanguage = False
        _askcommand = True
        print("Bienvenue à CommandOS (1.0) !")
        while _askcommand:
            command = input("Écrivez une commande (tapez aide pour avoir la liste des commandes) : ")
            if command == "help" or command == "aide" or command == "list":
                tip()
                print("Liste des commandes :")
                print("aide : Tu sais ce que ça fait :)")
                print("credits : Montre les crédits (logique)")
                print("language : Permet de changer de language")
                print("math : Exécute des opérations")
                print("date/temps (en construction) : montre la date et l'heure")
                print("quitter/fermer : quitte le script")
            elif command == "math":
                _math0 = False
                _mathcontinue = True
                _mathexecute = False
                _mathhadanerror = False
                _mathwithresult = False
                tip()
                #if math_result != "":
                #    math_result = float(math_result)
                math_param1 = input("Quel est le premier paramètre ? (mettez les chiffres à virgules avec des points !) : ")
                if math_param1 == "pi":
                    math_param1 = math.pi
                elif math_param1 == "nombredor" or math_param1 == "nombrdor" or math_param1 == "goldennumber":
                    math_param1 = CONST_goldennumber
                #elif math_param1 == "X" or math_param1 == "*" or math_param1 == "-" or math_param1 == "/" or math_param1 == "÷" or math_param1 == "+" or math_param1 == "²" or math_param1 == "carre" or math_param1 == "square":
                #    if math_result != "":
                #        math_operator = math_param1
                #        math_param1 = math_result
                #        _mathexecute = True
                #    else:
                #        _mathcontinue = False
                else:
                    try:
                        math_param1 = float(math_param1)
                    except:
                        _mathcontinue = False
                if _mathcontinue == True:
                    math_operator = input("Quel est le second paramètre ? : ")
                    if math_operator == "X" or math_operator == "*":
                        math_operator = "*"
                    elif math_operator == "-":
                        math_operator = "-"
                    elif math_operator == "/" or math_operator == "÷":
                        math_operator = "/"
                    elif math_operator == "+":
                        math_operator = "+"
                    elif math_operator == "²" or math_operator == "carre" or math_operator == "square":
                        math_operator = "*"
                        math_param2 = math_param1
                        _mathexecute = True
                    else:
                        _mathcontinue = False
                else:
                    print("Hmm. Tu n'as pas mit un nombre. Qu'est-ce que tu penserais que cela ferait, stupido !")
                    _mathhadanerror = True
                if _mathcontinue == True and _mathexecute == False:
                    math_param2 = input("Quel est le troisième paramètre ? (mettez  les nombres à virgule avec des points !) : ")
                    if math_param2 == "pi":
                        math_param2 = math.pi
                        _mathexecute = True
                    elif math_param2 == "nombredor" or math_param2 == "nombrdor" or  math_param2 == "goldennumber":
                        math_param2 = CONST_goldennumber
                        _mathexecute = True
                    else:
                        try:
                            math_param2 = float(math_param2)
                        except:
                           _mathcontinue = False
                elif _mathhadanerror == False and _mathcontinue == False:
                     print("Hmm. Tu n'as pas mit un opérateur correct. Qu'est-ce que tu pensais que cela ferait, stupido !")
                     _mathhadanerror = True
                if _mathcontinue == True:
                    _mathexecute = True
                if _mathexecute == True:
                    if math_operator == "*":
                        math_result = math_param1 * math_param2
                    elif math_operator == "+":
                        math_result = math_param1 + math_param2
                    elif math_operator == "-":
                        math_result = math_param1 - math_param2
                    elif math_operator == "/":
                        if math_param1 == 0:    
                            print("Bien essayé, mais il y a des vérifications !")
                            _math0 = True
                        else:
                            math_result = math_param1 / math_param2
                    if _math0 == False:
                        print("Le résultat de l'opération ", math_param1, math_operator, math_param2, " est ", math_result, ".")
                elif _mathexecute == False and _mathhadanerror == False:
                    print("Hmm. Tu n'as pas mit un nombre. Qu'est-ce que tu penserais que cela ferait, stupido !")
            elif command == "credits":
                tip()
                print("CommandOS 1.0 par omerien.")
                print("Vous êtes libre d'inclure ce script ou une version modifiée dans votre code, tant que cette commande (credits) ou que mon pseudo est inclus et intact dans le script.")
                print("Enjoy !")
            elif command == "language" or command == "lang":
                tip()
                _asklanguage = True
                _askcommand = False
            elif command == "date" or command == "time" or command == "temps":
                tip()
                print("Commande en construction... :)")
            elif command == "exit" or command == "quit" or command == "quitter" or command == "fermer":
                tip()
                print("Fermeture du script...")
                _askcommand = False
            else:
                tip()
                print("Cette commande n'existe pas ou n'est pas implémentée. Essayez de mettre à jour le script !")
    elif lang == "EN" or lang == "en":
        _asklanguage = False
        _askcommand = True
        print("Welcome to CommandOS (1.0) !")
        while _askcommand:
            command = input("Write a command (write help for a list of commands) : ")
            if command == "help" or command == "list":
                tip()
                print("List of commands :")
                print("help : You know what it does :)")
                print("credits : Show the credits (makes sense)")
                print("language : Allow you to change language")
                print("math : Execute operations")
                print("date/time (in construction) : show the date")
                print("exit/quit : exit the script")
            elif command == "math":
                _math0 = False
                _mathcontinue = True
                _mathexecute = False
                _mathhadanerror = False
                tip()
                math_param1 = input("What is the first parameter ? : ")
                if math_param1 == "pi":
                    math_param1 = math.pi
                elif math_param1 == "goldennumber":
                    math_param1 = CONST_goldennumber
                else:
                    try:
                        math_param1 = float(math_param1)
                    except:
                        _mathcontinue = False
                if _mathcontinue == True:
                    math_operator = input("What is the second parameter ? : ")
                    if math_operator == "X" or math_operator == "*":
                        math_operator = "*"
                    elif math_operator == "-":
                        math_operator = "-"
                    elif math_operator == "/" or math_operator == "÷":
                        math_operator = "/"
                    elif math_operator == "+":
                        math_operator = "+"
                    elif math_operator == "² or math_operator == "square":
                        math_operator = "*"
                        math_param2 = math_param1
                        _mathexecute = True
                    else:
                        _mathcontinue = False
                else:
                    print("Hmm. You didn't put a number. What did you think it would do, stupid !")
                    _mathhadanerror = True
                if _mathcontinue == True and _mathexecute == False:
                    math_param2 = input("What is the third parameter ? : ")
                    if math_param2 == "pi":
                        math_param2 = math.pi
                        _mathexecute = True
                    elif math_param2 == "goldennumber":
                        math_param2 = CONST_goldennumber
                        _mathexecute = True
                    else:
                        try:
                            math_param2 = float(math_param2)
                        except:
                           _mathcontinue = False
                elif _mathhadanerror == False and _mathcontinue == False:
                     print("Hmm. You didn't put a valid operator. What did you think it would do, stupid !")
                     _mathhadanerror = True
                if _mathcontinue == True:
                    _mathexecute = True
                if _mathexecute == True:
                    if math_operator == "*":
                        math_result = math_param1 * math_param2
                    elif math_operator == "+":
                        math_result = math_param1 + math_param2
                    elif math_operator == "-":
                        math_result = math_param1 - math_param2
                    elif math_operator == "/":
                        if math_param1 == 0:    
                            print("Nice try, but there is verifications !")
                            _math0 = True
                        else:
                            math_result = math_param1 / math_param2
                    if _math0 == False:
                        print("The result of the operation ", math_param1, math_operator, math_param2, " is ", math_result, ".")
                elif _mathexecute == False and _mathhadanerror == False:
                    print("Hmm. You didn't put a number. What did you think it would do, stupid !")
            elif command == "credits":
                tip()
                print("CommandOS 1.0 by omerien.")
                print("You have authorization to put this script or a modified version in your code, as long as this command (credits) or my pseudo is included and intact in the script.")
                print("Enjoy !")
            elif command == "language" or command == "lang":
                tip()
                _asklanguage = True
                _askcommand = False
            elif command == "date" or command == "time":
                tip()
                print("Building this command... :)")
            elif command == "exit" or command == "quit":
                tip()
                print("Exiting the script...")
                _askcommand = False
            else:
                tip()
                print("This command doesn't exist or isn't implemented right now. Try updating the script !")
    elif lang == "exit":
        _asklanguage = False
        print("Exiting the script...")
    else:
        print("Seems this is an invalid language code. Try again.")
print("Successfully exited the script !")
os.system("pause") #For Windows. STUPID, WINDOWS !
