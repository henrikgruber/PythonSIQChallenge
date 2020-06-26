from tkinter import *

#.pack() Funktion -> Zeile wird Mittig dargestellt 
#global Funktion -> um die Variable in anderen Funktionen auch aufrufen zu können

#Funktion nur für den Test der Gui angelegt - muss mit tatsächlicher Funktion ersetzt werden
def register_person(): 
    print("Registration started")
    user = username.get()
    pw = username.get()
    print("REGISTRATION - Username: " + user + " Password:" + pw)
  
#Funktion nur für den Test der Gui angelegt - muss mit tatsächlicher Funktion ersetzt werden
def login_person(): 
    print("Login started")
    user= username.get()
    pw = username.get()
    print("LOGIN - Username: " + user + " Password:" + pw)


# Funktion für den Aufruf des Registrierungs Screens, die tatsächliche Registerierung erfolgt in einer andern Funktion 
def register():
    #screen settings
    register_screen = Toplevel(main_screen)
    register_screen.title("Learn Tracking App Registration")
    register_screen.geometry('300x250')
    
    global username 
    global password 
    global username_entry
    global password_entry
    
    #Variablen deklarieren
    username = StringVar()
    password = StringVar()
    
    #Eingabefelder/Buttons, muss immer den entsprechenden Screen hier angeben, sonst wird alles im Main Screen angezeigt 
    Label (register_screen, text = " ").pack() #Abstandzeile
    Label (register_screen, text = "Username:", font=('bold', 10)).pack()
    username_entry = Entry (register_screen, textvariable = username).pack() 
    Label (register_screen, text = "Password:", font=('bold', 10)).pack()
    password_entry = Entry (register_screen, textvariable = password).pack()
    Label (register_screen, text = " ").pack() #Abstandzeile
    #Aufrufen der tatsächlichen Registrierungs Funktion mit dem Button 
    register_btn = Button (register_screen, text = "Register", command = register_person).pack()
   

def login():
    login_screen = Toplevel(main_screen)
    login_screen.title("Learn Tracking App Login")
    login_screen.geometry('300x250')
    
    global username 
    global password 
    global username_entry
    global password_entry
    
    #Variablen deklarieren
    username = StringVar() #muss dann entsprechend der Benutzernamen generierung hier umgeschrieben werden
    password = StringVar() #muss dann entsprechend der Passwort generierung hier umgeschrieben werden
    
    #Eingabefelder/Buttons, muss immer den entsprechenden Screen hier angeben, sonst wird alles im Main Screen angezeigt 
    Label (login_screen, text = " ").pack() #Abstandzeile
    Label (login_screen, text = "Username:", font=('bold', 10)).pack()
    username_entry = Entry (login_screen, textvariable = username).pack() 
    Label (login_screen, text = "Password:", font=('bold', 10)).pack()
    password_entry = Entry (login_screen, textvariable = password).pack()
    Label (login_screen, text = " ").pack() #Abstandzeile
    login_btn = Button (login_screen, text = "Login", command = login_person).pack()

    
def app_main():
    #command = Zuordnen der Funktion zum Button
    global main_screen #um den screen von einer anderen funktion aufrufen zu können
    main_screen = Tk()
    Label (text = " ").pack() #Abstandzeile
    main_screen.title('Learn Tracking App') #Maskentitel
    main_screen.geometry('300x250') #Maskengröße
    titel = Label (text = "Learn Tracking App", font=('bold', 10)).pack() #Überschrift
    Label (text = " ").pack() #Abstandzeile
    login_btn = Button (text = "Login", height = "2", width = "30", command = login).pack()
    Label (text = " ").pack() #Abstandzeile
    register_btn = Button (text = "Register", height = "2", width = "30", command = register).pack()
    main_screen.mainloop()

app_main()

