#Password generator 


from random import randint
import string

def listNumeric():
    lst = list(string.ascii_letters)
    lst += list(string.digits)
    return(lst)

sizePassword = int(input("Veuillez saisir la taille du password: "))
tblpassword = []
lst_global = listNumeric()

def process_password():
    password = ""
    for i in range(sizePassword):
        letter = randint(0, len(lst_global)-1)
        tblpassword.append(lst_global[letter])

    for j in range(len(tblpassword)):
        password += tblpassword[j]
    return print(password)

process_password()

