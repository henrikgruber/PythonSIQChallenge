
def initialize_category():
    import pandas as pd
    v_topic = ""
    v_categories = pd.read_csv('PythonCategories.csv')
    

    #Start index counting at 1 to let participants choose an appropriate number
    v_categories.index += 1 
    # Warum wird Accenture Specific hier rausgenommen?
    print(v_categories.head(int(len(v_categories)-1)))
    while True:
        try:
            inp_area = input("Which area did you practise: ")
            #we choose "len(df)-1" to dynamically increase the number
            #in case there will be more cantons in future
            # 0 wurde rausgenommen, erfüllt diese einen zweck?
            if int(inp_area) in range(len(v_categories)):
                #short name canton will be returned
                v_topic = v_categories.loc[int(inp_area),"PythonTopic"]
                break;
            else:
                #Warum springt er hier nicht bei 0 rein
                print('This area does not exist')
        except:
            #we choose "len(df)-1" as the maximum amount of cantons,
            #in case the number of cantons will change in future
            print("Please enter an area no. between 1-"+str(len(v_categories)-1))
    return v_topic

#upper() wandelt Kleinbuchstaben in Großbuchstaben um
def initialize_person():
    return input("Please enter your Name: ").upper()

def initialize_confidence():
    v_confidence = 0
    print("Please enter your confidence on a scale from 1 (oh oh) to 4 (great)")
    #skip the header row
    while True:
        try:
            v_confidence = input()
            if int(v_confidence) in range(1, 5):
                break;
            else:
                print('Please try again. Enter a number between 1-4')
        except:
            print("You did not enter a number. Please enter 1-4")
    return v_confidence
