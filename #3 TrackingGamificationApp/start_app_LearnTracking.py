
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



v_initialize_category = Setup.initialize_category()

# (3) Perform the actual survey. Question by question.
#   Parameter "inp_survey[2]" stands for the survey which has been chosen
write_points = survey.take_survey(inp_survey[2])

# (4) Show the grade, healthy or suggestion for medical support.
#   In case the health result is poor, doctor suggestions from the appropriate
#   canton are being shown.
#   Parameter "inp_survey[0]" stands for the participants' canton
survey.final_result(write_points,inp_survey[0])


# (5) Survey results are being written persistantly into a file
#   calls to results.py due to: writing the results into a file, 
#   creating diagrams for the participants
import results
#   Parameter "inp_survey[0]" = canton, "inp_survey[1]" = age of 
#   the participant, "inp_survey[2]" = Survey taken
#   write_point = amount of points accumulated in this survey
results.write_survey_results(inp_survey[0],inp_survey[1],inp_survey[2],write_points)

# (6) Plot statistical results via diagrams
results.create_diagrams()
