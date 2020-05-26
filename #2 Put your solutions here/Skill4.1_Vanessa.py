#Write a Python program to delete an existing item from the array

liste = [1, 3, 5, 7, 9, 11]
print("This is the list: ", liste)
x = int(input("Which entry (position) do you want to delete: ")) - 1

del(liste[x])
print("This is the new list: ", liste)
