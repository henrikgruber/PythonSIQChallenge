from tkinter import *

#.pack() Funktion -> Zeile wird Mittig dargestellt 
#global Funktion -> um die Variable in anderen Funktionen auch aufrufen zu können

#Funktion nur für den Test der Gui angelegt - muss mit tatsächlicher Funktion ersetzt werden
def register_person(): 
    print("Registration started")
    user = username.get()
    pw = username.get()
    print("REGISTRATION - Username:" + user + " Password:" + pw)
  
#Funktion nur für den Test der Gui angelegt - muss mit tatsächlicher Funktion ersetzt werden
def login_person(): 
    print("Login started")
    user= username.get()
    pw = username.get()
    print("LOGIN - Username:" + user + " Password:" + pw)


# Funktion für den Aufruf des Registrierungs Screens, die tatsächliche Registerierung erfolgt in einer andern Funktion 
def register():
    #screen settings
    register_screen = Toplevel(main_screen)
    register_screen.title("Learn Tracking App Registration")
    register_screen.geometry('300x250')
    register_screen.configure(bg='white')
    
    global username 
    global password 
    global username_entry
    global password_entry
    
    #Variablen deklarieren
    username = StringVar()
    password = StringVar()
    
    #Eingabefelder/Buttons, muss immer den entsprechenden Screen hier angeben, sonst wird alles im Main Screen angezeigt 
    titel = Label (register_screen, text = "Registration", fg = "white", bg = 'steel blue', height = "2", width = "40", font='Opensans').pack()
    Label (register_screen, text = " ", bg = 'white').pack() #Abstandzeile
    Label (register_screen, text = "Username:", bg = 'white', font=('bold', 10)).pack()
    username_entry = Entry (register_screen, bg = "ivory2", textvariable = username).pack() 
    Label (register_screen, text = "Password:", bg = 'white', font=('bold', 10)).pack()
    password_entry = Entry (register_screen, bg = "ivory2", textvariable = password).pack()
    Label (register_screen, text = " ", bg = 'white').pack() #Abstandzeile
    #Aufrufen der tatsächlichen Registrierungs Funktion mit dem Button 
    register_btn = Button (register_screen, text = "Register", height = "1", width = "14", bg ='white', borderwidth = 1, command = register_person).pack()
   

def login():
    login_screen = Toplevel(main_screen)
    login_screen.title("Learn Tracking App Login")
    login_screen.geometry('300x250')
    login_screen.configure(bg='white')
    
    global username 
    global password 
    global username_entry
    global password_entry
    
    #Variablen deklarieren
    username = StringVar() #muss dann entsprechend der Benutzernamen generierung hier umgeschrieben werden
    password = StringVar() #muss dann entsprechend der Passwort generierung hier umgeschrieben werden
    
    #Eingabefelder/Buttons, muss immer den entsprechenden Screen hier angeben, sonst wird alles im Main Screen angezeigt 
    titel = Label (login_screen, text = "LOGIN", fg = "white", bg = 'steel blue', height = "2", width = "40", font='Opensans').pack()
    Label (login_screen, text = " ", bg = 'white').pack() #Abstandzeile
    Label (login_screen, text = "Username:", bg = 'white', font=('bold', 10)).pack()
    username_entry = Entry (login_screen, bg = "ivory2", textvariable = username).pack() 
    Label (login_screen, text = "Password:", bg = 'white', font=('bold', 10)).pack()
    password_entry = Entry (login_screen, bg = "ivory2", textvariable = password).pack()
    Label (login_screen, text = " ", bg = 'white').pack() #Abstandzeile
    login_btn = Button (login_screen, text = "Login", height = "1", width = "14", bg ='white', borderwidth = 1, command = login_person).pack()

    
def app_main():
    #command = Zuordnen der Funktion zum Button    
    global main_screen #um den screen von einer anderen funktion aufrufen zu können
    main_screen = Tk()
    Label (text = " ", bg = 'white').pack() #Abstandzeile
    main_screen.title('Learn Tracking App') #Maskentitel
    main_screen.geometry('350x250') #Maskengröße
    main_screen.configure(bg='white')
    titel = Label (text = "Learn Tracking App", bg = 'white', font='Opensans').pack() #Überschrift
    Label (text = " ", bg = 'white').pack() #Abstandzeile
    login_btn = Button (text = "Login", height = "2", width = "20", bg = 'white', borderwidth = 1, command = login).pack()
    Label (text = " ", bg = 'white').pack() #Abstandzeile
    register_btn = Button (text = "Register", height = "2", width = "20", bg ='white', borderwidth = 1, command = register).pack()
    main_screen.mainloop()

app_main()

