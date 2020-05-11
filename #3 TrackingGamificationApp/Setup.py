def initialize_category():
    import pandas as pd
    v_topic = ""
    v_categories = pd.read_csv('PythonCategories.csv')

    #Start index counting at 1 to let participants choose an appropriate number
    v_categories.index += 1 
    print(v_categories.head(int(len(v_categories)-1)))
    while True:
        try:
            inp_area = input("Which area did you practise: ")
            #we choose "len(df)-1" to dynamically increase the number
            #in case there will be more cantons in future
            if int(inp_area) in range(0, len(v_categories)):
                #short name canton will be returned
                v_topic = v_categories.loc[int(inp_area),"PythonTopic"]
                break;
            else:
                print('This area does not exist')
        except:
            #we choose "len(df)-1" as the maximum amount of cantons,
            #in case the number of cantons will change in future
            print("Please enter an area no. between 1-"+str(len(v_categories)-1))    
    return v_topic


print(initialize_category())