#CommandOS by omerien
#This script does not follow the rule "We are all consentant adults" and there are many verifications in the script 
#Maybe because its programmer is a kid ?
#Anyway, enjoy the script !
import os         #
import math       # Importing a few modules...
import random     #
_asklanguage = True                #
_askcommand = True                 #
_askos = True                      #
CONST_goldennumber = 1.618033989   #
lang = ""                          # Setting some variables for the future...
math_result = ""                   # (Some variables are defined in the script)
_mathcontinue = True               #
_mathexecute = False               #
_mathexecuted = False              #
_mathhadanerror = False            #
_math0 = False                     #
def tip():
    tip_randint1 = random.randrange(1, 11, 1)                              
    if tip_randint1 == 10:                                                 
        tip_randint2 = random.randrange(1, 3, 1)                           
        if tip_randint2 == 1:                                              
            if lang == "fr" or lang == "FR":                               
                print("Tip : N'oubliez pas de mettre ce script à jour !")
            elif lang == "en" or lang == "EN":                             
                print("Tip : Don't forget to update your script !")        
        if tip_randint2 == 2:                                              
            if lang == "fr" or lang == "FR":                               
                print("Tip : Je suis un Tip ! Je peux vous donner quelques infos utiles dans l'utilisation de CommandOS ! (J'apparais une fois sur 10 !)")
            elif lang == "en" or lang == "EN":                               
                print("Tip : I am a tip ! I can give you some useful informations about CommandOS ! (I appear one time per 10 !)")
while _askos:
    useros = input("What is your OS ? (Mac OS, Windows or Linux) : ")
    if useros == "Windows" or useros == "Mac OS" or useros == "Linux":
        _askos = False
    else:
        print("Invalid OS.")
while _asklanguage:    #...and here we go !
    lang = input("What is your language code ? (FR or EN) : ")
    if lang == "FR" or lang == "fr":
        _asklanguage = False
        _askcommand = True
        print("Bienvenue à CommandOS beta (b1.5) !")
        while _askcommand:
            command = input("Écrivez une commande (tapez aide pour avoir la liste des commandes) : ")
            if command == "help" or command == "aide" or command == "list":
                tip()
                print("Liste des commandes :")
                print("aide : Tu sais ce que ça fait :)")
                print("credits : Montre les crédits (logique)")
                print("language : Permet de changer de language")
                print("math (en construction) : Exécute des opérations")
                print("date/temps (en construction) : montre la date et l'heure")
                print("quitter/fermer : quitte le script")
            elif command == "math":
                _math0 = False
                _mathcontinue = True
                _mathexecute = False
                _mathexecuted = False
                _mathhadanerror = False
                tip()
                math_input_param1 = input("Quel est le premier paramètre ? (mettez les chiffres à virgules avec des points !) : ")
                if math_input_param1 == "pi":
                    math_param1 = math.pi
                elif math_input_param1 == "nombredor" or math_input_param1 == "nombrdor" or math_input_param1 == "goldennumber":
                    math_param1 = CONST_goldennumber
                else:
                    try:
                        try:
                            if int(math_input_param1):
                                _mathcontinue = True
                                math_param1 = math_input_param1
                        except:
                            if float(math_input_param1):
                                _mathcontinue = True
                                math_param1 = math_input_param1
                    except:
                        _mathcontinue = False
                if _mathcontinue == True:
                    math_input_param2 = input("Quel est le second paramètre ? : ")
                    if math_input_param2 == "X" or math_input_param2 == "*":
                        math_param2 = "*"
                    elif math_input_param2 == "-":
                        math_param2 = "-"
                    elif math_input_param2 == "/" or math_input_param2 == "÷":
                        math_param2 = "/"
                    elif math_input_param2 == "+":
                        math_param2 = "+"
                    elif math_input_param2 == "²" or math_input_param2 == "carre" or math_input_param2 == "square":
                        math_param2 = "*"
                        math_param3 = math_param1
                        _mathexecute = True
                    elif math_input_param2 == "puissance" or math_input_param2 == "power" or math_input_param2 == "^":
                        math_param2 = "^"
                    else:
                        _mathcontinue = False
                else:
                    print("Hmm. Tu n'as pas mit un nombre. Qu'est-ce que tu penserais que cela ferait, stupido !")
                    _mathhadanerror = True
                if _mathcontinue == True and _mathexecute == False:
                    math_input_param3 = input("Quel est le troisième paramètre ? (mettez  les nombres à virgule avec des points !) : ")
                    if math_input_param3 == "pi":
                        math_param3 = math.pi
                        _mathexecute = True
                    elif math_input_param1 == "nombredor" or math_input_param1 == "nombrdor" or  math_input_param3 == "goldennumber":
                        math_param3 = CONST_goldennumber
                        _mathexecute = True
                    else:
                        try:
                            try:
                                if int(math_input_param3):
                                    _mathexecute = True
                                    math_param3 = math_input_param3
                            except:
                                if float(math_input_param3):
                                    _mathexecute = True
                                    math_param3 = math_input_param3
                        except:
                            _mathcontinue = False
                elif _mathhadanerror == False and _mathcontinue == False:
                     print("Hmm. Tu n'as pas mit un opérateur correct. Qu'est-ce que tu pensais que cela ferait, stupido !")
                     _mathhadanerror = True
                if _mathexecute == True and _mathexecuted == False:
                    if math_param2 == "*":
                        math_result = math_param1 * math_param3
                    elif math_param2 == "+":
                        math_result = math_param1 + math_param3
                    elif math_param2 == "-":
                        math_result = math_param1 - math_param3
                    elif math_param2 == "/":
                        if math_param1 == 0:
                            print("Bien essayé, mais il y a des vérifications !")
                            _math0 = True
                        else:
                            math_result = math_param1 / math_param3
                    if _math0 == False:
                        print("Le résultat de l'opération", math_param1 + math_param2 + math_param3, "est", math_result, ".")
                elif _mathexecute == False and _mathhadanerror == False and _mathexecuted == False:
                    print("Hmm. Tu n'as pas mit un nombre. Qu'est-ce que tu penserais que cela ferait, stupido !")
            elif command == "credits":
                tip()
                print("CommandOS b1.5 par omerien.")
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
        print("Welcome to CommandOS beta (b1.5) !")
        while _askcommand:
            command = input("Write a command (write help for a list of commands) : ")
            if command == "help" or command == "list":
                tip()
                print("List of commands :")
                print("help : You know what it does :)")
                print("credits : Show the credits (logic)")
                print("language : Allow you to change language")
                print("math (in construction) : Execute operations")
                print("date/time (in construction) : show the date")
                print("exit/quit : exit the script")
            elif command == "math":
                _math0 = False
                _mathcontinue = True
                _mathexecute = False
                _mathexecuted = False
                tip()
                math_input_param1 = input("What is the first parameter ? : ")
                if math_input_param1 == "pi":
                    math_param1 = math.pi
                elif math_input_param1 == "goldennumber":
                    math_param1 = CONST_goldennumber
                else:
                    if isinstance(math_input_param1, float) == True or isinstance(math_input_param1, int) == True:
                        _mathcontinue = True
                        math_param1 = math_input_param1
                    else:
                        _mathcontinue = False
                if _mathcontinue == True:
                    math_input_param2 = input("What is the second parameter ? : ")
                    if math_input_param2 == "X" or math_input_param2 == "*":
                        math_param2 = "*"
                        print(math_param2)
                    elif math_input_param2 == "-":
                        math_param2 = "-"
                    elif math_input_param2 == "/" or math_input_param2 == "÷":
                        math_param2 = "/"
                    elif math_input_param2 == "+":
                        math_param2 = "+"
                    elif math_input_param2 == "²" or math_input_param2 == "square":
                        math_param2 = "*"
                        math_param3 = math_param1
                        _mathexecute = True
                    elif math_input_param2 == "power" or math_input_param2 == "^":
                        math_param2 = "^"
                    else:
                        _mathcontinue = False
                else:
                    print("Hmm. You didn't put a number. What did you think it would do, stupid !")
                    _mathhadanerror = True
                if _mathcontinue == True and _mathexecute == False:
                    math_input_param3 = input("What is the third parameter ? : ")
                    if math_input_param3 == "pi":
                        math_param3 = math.pi
                        _mathexecute = True
                    elif math_input_param3 == "nombredor" or math_input_param3 == "nombrdor":
                        math_param3 = CONST_goldennumber
                        _mathexecute = True
                    else:
                        if isinstance(math_input_param3, float) == True or isinstance(math_input_param3, int) == True:
                            _mathexecute = True
                            math_param3 = math_input_param3
                elif _mathhadanerror == False and _mathcontinue == False and _mathexecute == False:
                     print("Hmm.You didn't put a valid operator. What did you think it would do, stupid !")
                     _mathhadanerror = True
                if _mathexecute == True and _mathexecuted == False and _mathhadanerror == False:
                    if math_param2 == "*":
                        math_result = math_param1 * math_param3
                    elif math_param2 == "+":
                        math_result = math_param1 + math_param3
                    elif math_param2 == "-":
                        math_result = math_param1 - math_param3
                    elif math_param2 == "/":
                        if math_param1 == 0:
                            print("Nice try, but there is verifications !")
                            _math0 = True
                        else:
                            math_result = math_param1 / math_param3
                    if _math0 == False:
                        print(f"The result of the operation math_param1 math_param2 math_param3 is math_result")
                elif _mathhadanerror == False and _mathexecute == False and _mathexecuted == False:
                    print("Hmm. You didn't put a number. What did you think it would do, stupid !")
            elif command == "credits":
                tip()
                print("CommandOS b1.5 by omerien.")
                print("You are authorized to put this script or a modified version in your code, as long as this command (credits) or my pseudo is included and intact in the script.")
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
