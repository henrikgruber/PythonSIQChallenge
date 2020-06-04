# pandas is being used for dataframes (loading all data from survey results)
import pandas

def write_results(p_person,p_category,p_confidence,p_date):
    df_write = pandas.DataFrame({'\n\nPerson': [p_person],
                       'Category': [p_category],
                       'Confidence': [p_confidence],
                       'Date': [p_date]})
    df_write.to_csv('tracking_results.csv', mode='a', header=False,index=False)
    return

def motivational_booster():
    print("")
    print("")
    print("Keep up the good work")
    print("")
    print("")
    print("")
    print("           ___________                ")
    print("          '._==_==_=_.'               ")
    print("          .-\:      /-.               ")
    print("         | (|:.     |) |              ")
    print("          '-|:.     |-'               ")
    print("            \::.    /                 ")
    print("             '::. .'                  ")
    print("               ) (                    ")
    print("             _.'_'._                  ")
    print("")
    print("")
    return
