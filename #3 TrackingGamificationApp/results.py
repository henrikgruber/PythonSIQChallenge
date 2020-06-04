# pandas is being used for dataframes (loading all data from survey results)
import pandas


# matplotlib is neccesary for creating statistical diagrams based on former surveys
import matplotlib.pyplot as plt

# squarify is necessary for creating a treemap diagram
# import squarify as sq

def write_results(p_person,p_category,p_confidence,p_date):
    df_write = pandas.DataFrame({'\n\nPerson': [p_person],
                       'Category': [p_category],
                       'Confidence': [p_confidence],
                       'Date': [p_date]})
    df_write.to_csv('tracking_results.csv', mode='a', header=False,index=False)
    return



"""
def create_diagrams():
    tracking_results = pandas.read_csv('tracking_results.csv')
    
    print("")
    print("")
    print("Additionally, you'll find some diagrams about our stored data.")
    print("")
    
        
# part 2 - Creating a treemap to show distribution 
    results_grouped = tracking_results.groupby("Category", as_index=False)["Confidence"].sum()
    sq.plot(sizes=results_grouped['Confidence'], label=results_grouped['Category'], alpha=.8 )
    # Hiding axis
    plt.axis('off')
    # Set labels
    plt.title("Confidence per Category")
    #View the plot
    plt.show()

# part 3 - piechart 
    #grouped by surveys, build the sum
    results_by_area = tracking_results.groupby("Category", as_index=False)["Confidence"].count()
    # sum the instances of A (position 0) and B (position 1)
    A_results = results_by_area.loc[0,"Confidence"]
    B_results = results_by_area.loc[1,"Confidence"]
    # put them into a list called proportions
    proportions = [A_results, B_results]    

    plt.pie(
        # using proportions
        proportions,

        # with the labels being names
        labels = ['A', 'B'],

        # with no shadows
        shadow = False,

        # with colors
        colors = ['blue','red'],

        # with one slide exploded out
        explode = (0.15 , 0),

        # with the start angle at 90%
        startangle = 90,

        # with the percent listed as a fraction
        autopct = '%1.1f%%'
        )

    # View the plot drop above
    plt.axis('equal')
    # Set labels
    plt.title("Points achieved in areas")
    # View the plot
    plt.tight_layout()
    plt.show()
    
    return
"""

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