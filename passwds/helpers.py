import random,string


def password_generator(minu,maj,chiffres,speciaux,nbreCaractere):
    password_gen =''
    print("Debut Valeurs : {} {} {} {}".format(minu,maj,chiffres,speciaux))
    #LETTRES - CHIFFRES - SPECIAUX 1
    if minu == 'True' and maj == 'True' and chiffres == 'True' and speciaux == 'True':
        print("CAS 1")
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
        print("Valeurs : {} {} {} {}".format(minu,maj,chiffres,speciaux))
    #LETTRES ET CHIFFRES 2
    elif minu == 'True' and maj == 'True' and chiffres == 'True' and speciaux == 'False':
         print("CAS 2")
         password_characters = string.ascii_letters + string.digits
         password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
    #LETTRES (MINUSCULES ET MAJUSCULES) 3
    elif minu == 'True' and maj == 'True' and chiffres == 'False' and speciaux == 'False':
        print("CAS 3")
        password_characters = string.ascii_letters
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
    #LETTRES MINUSCULES 4
    elif minu == 'True' and maj == 'False' and chiffres == 'False' and speciaux == 'False':
        print("CAS 4")
        password_characters = string.ascii_lowercase
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
    #LETTRES MINUSCULES ET CHIFFRES 5
    elif minu == 'True' and maj == 'False' and chiffres == 'True' and speciaux == 'False':
        print("CAS 5")
        password_characters = string.ascii_lowercase + string.digits
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
    #LETTRES MINUSCULES - CHIFFRES - SPECIAUX 6
    elif minu == 'True' and maj == 'False' and chiffres == 'True' and speciaux == 'True':
        print("CAS 6")
        password_characters = string.ascii_lowercase + string.digits + string.punctuation
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
     #CHIFFRES - SPECIAUX 7
    elif minu == 'False' and maj == 'False' and chiffres == 'True' and speciaux == 'True':
        print("CAS 7")
        password_characters = string.punctuation + string.digits
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
     #LETTRES MINUSCULES ET SPECIAUX 8
    elif minu == 'True' and maj == 'False' and chiffres == 'False' and speciaux == 'True':
        print("CAS 8")
        password_characters = string.ascii_lowercase + string.punctuation
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
    #LETTRES MAJUSCULES 9
    elif minu == 'False' and maj == 'True' and chiffres == 'False' and speciaux == 'False':
        print("CAS 9")
        password_characters = string.ascii_uppercase
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
     #LETTRES MAJUSCULES ET SPECIAUX 10
    elif minu == 'False' and maj == 'True' and chiffres == 'False' and speciaux == 'True':
        print("CAS 10")
        password_characters = string.ascii_uppercase + string.punctuation
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
   #LETTRES MAJUSCULES - CHIFFRES - SPECIAUX 11
    elif minu == 'False' and maj == 'True' and chiffres == 'True' and speciaux == 'True':
        print("CAS 11")
        password_characters = string.ascii_uppercase + string.digits + string.punctuation
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
     #LETTRES MAJUSCULES ET CHIFFRES 12
    elif minu == 'False' and maj == 'True' and chiffres == 'True' and speciaux == 'False':
        print("CAS 12")
        password_characters = string.ascii_uppercase + string.digits
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
     #CHIFFRES 13
    elif minu == 'False' and maj == 'False' and chiffres == 'True' and speciaux == 'False':
        print("CAS 13")
        password_characters = string.digits
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
     #SPECIAUX 14
    elif minu == 'False' and maj == 'False' and chiffres == 'False' and speciaux == 'True':
        print("CAS 14")
        password_characters = string.punctuation
        password_gen = ''.join(random.choice(password_characters) for i in range(nbreCaractere))
    else :
        print("E Valeurs : {} {} {} {}".format(minu,maj,chiffres,speciaux))


    return password_gen