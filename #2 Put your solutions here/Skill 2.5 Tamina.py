#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
#Sample Output:

#Input your First Name : 
#Dany                                       
#Input your Last Name : 
#Boon                                        
#Hello  Boon Dany    

first = str (input("Please insert your first name: "))
last = input("Please insert your last name: ")
message = "Hello " + last +" " + first
print (message)

