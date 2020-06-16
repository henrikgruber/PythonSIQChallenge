import setup
import results
import datetime
import import_modules

import_modules.auto_install()


# (1) Welcome to the App
#   http://asciiflow.com/ has been used to create the ascii-pics

print("")
print("")
print("")
print("         Welcome to the our Progress Tracking App")
print("")
print("                   ,++./,+.")
print("                  / #      \ ")
print("                 +          +")
print("                  \        /")
print("                   `._,._,'")
print("")
print("")
print("+------------------------------------------------------+")
print("| EXPLANATION                                          |")
print("| * Choose a Name                                      |")
print("| * choose an area you just practised                  |")
print("| * choose how confident you were about your task      |")
print("|                                                      |")
print("| --> results will be stored for your tracking <--     |")
print("|                                                      |")
print("+------------------------------------------------------+")
print("")      
input("Let us start. Hit any key. ")


# (1) initialize all data
v_person = setup.initialize_person()
v_category = setup.initialize_category()
v_confidence = setup.initialize_confidence()


# (3) write results
results.write_results(v_person,v_category,v_confidence,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

# (6) Plot statistical results via diagrams
results.create_diagrams()

# (7) motivational booster
results.motivational_booster()