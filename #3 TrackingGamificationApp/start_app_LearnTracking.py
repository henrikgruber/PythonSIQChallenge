
#calls to survey.py due to: initialization, survey taking, 
#   evaluation of results 
import survey

#contains a tuple, consisting of (v_which_canton, v_age, inp_survey)
global inp_survey



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
v_category = setup.initialize_person()
v_confidence = setup.initialize_confidence()
v_category = Setup.initialize_category()


# (3) write results
setup.write_results(p_person,v_category,p_confidence,p_date):

# (6) Plot statistical results via diagrams
results.create_diagrams()
