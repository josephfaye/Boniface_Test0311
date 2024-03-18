def lire_csv(nom_fichier):
    contacts = []
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            contact = ligne.strip().split(',')
            contacts.append(contact)
    return contacts

def ecrire_csv(nom_fichier, contacts):
    with open(nom_fichier, 'w') as fichier:
        for contact in contacts:
            ligne = ','.join(contact) + '\n'
            fichier.write(ligne)

contacts = [
    ["Jean Dupont", "123-456-7890", "jean.dupont@example.com"],
    ["Marie Martin", "234-567-8901", "marie.martin@example.com"],
    ["Pierre Durand", "345-678-9012", "pierre.durand@example.com"],
    ["Sophie Lambert", "456-789-0123", "sophie.lambert@example.com"],
    ["Luc Moreau", "567-890-1234", "luc.moreau@example.com"],
    ["Julie Leclerc", "678-901-2345", "julie.leclerc@example.com"],
    ["Thomas Lefevre", "789-012-3456", "thomas.lefevre@example.com"],
    ["Emma Dubois", "890-123-4567", "emma.dubois@example.com"],
    ["Nicolas Girard", "901-234-5678", "nicolas.girard@example.com"],
    ["Camille Rousseau", "012-345-6789", "camille.rousseau@example.com"]
]

ecrire_csv("contacts.csv", contacts)

#pour lire des donnees a partir d'un fichier CSV
nouveaux_contacts = lire_csv("contacts.csv")
print("Contacts lus a partir du fichier CSV :")
for contact in nouveaux_contacts:
      print(contact[0].ljust(20), contact[1].rjust(15), contact[2].rjust(30))
 

donnees_meteo = [
    ['2024-01-01', 'Paris', 5, 9, 15],
    ['2024-01-02', 'Paris', 19, 5, 14],
    ['2024-01-03', 'Paris', 7, -5, 13],
    ['2024-01-04', 'Paris', 22, 5, 15],
    ['2024-01-05', 'Paris', 2, 2, 20],
    ['2024-01-06', 'Paris', -1, -2, 20],
    ['2024-01-07', 'Paris', 5, 6, 15],
    ['2024-01-08', 'Paris', 4, -4, 9],
    ['2024-01-09', 'Paris', 5, 5, 3],
    ['2024-01-10', 'Paris', 31, 30, 17],
    ['2024-01-01', 'Lyon', 32, 5, 8],
    ['2024-01-02', 'Lyon', 0, -2, 20],
    ['2024-01-03', 'Lyon', 22, 4, 1],
    ['2024-01-04', 'Lyon', 26, -10, 8],
    ['2024-01-05', 'Lyon', 16, 7, 6],
    ['2024-01-06', 'Lyon', 11, 2, 11],
    ['2024-01-07', 'Lyon', 10, 23, 20],
    ['2024-01-08', 'Lyon', 3, 7, 8],
    ['2024-01-09', 'Lyon', 34, 24, 17],
    ['2024-01-10', 'Lyon', -3, 25, 11]
]

def filtrer_ville_lyon(donnees):
    for enregistrement in donnees:
        if enregistrement[1] == "Lyon":
            print(enregistrement)
            

def filtrer_entre_dates(donnees, date_debut, date_fin):
    for enregistrement in donnees:
        if date_debut <= enregistrement[0] <= date_fin:
            print(enregistrement)
            
def moyenne_precipitations_lyon(donnees):
    total_precipitations = 0
    nombre_jours = 0
    
    for jour in donnees:
        if jour[1] == 'Lyon':
            total_precipitations += jour[4]
            nombre_jours += 1
    
    moyenne = total_precipitations / nombre_jours if nombre_jours else 0
    print(moyenne)

# Sous-programme qui filtre les données météo d'une ville
def filtrer_ville(donnees):
    ville = input("Entrez le nom de la ville : ")
    for enregistrement in donnees:
        if enregistrement[1].lower() == ville.lower():
            print(enregistrement)

# Sous-programme qui filtre les données météo d'une ville durant une période
def filtrer_entre_dates_et_ville(donnees, date_debut, date_fin, ville):
    for enregistrement in donnees:
        if (date_debut <= enregistrement[0] <= date_fin) and (enregistrement[1].lower() == ville.lower()):
            print(enregistrement)

def sous_programme_1():
    print("Filtrer les données météo par ville.")
    ville = input("Entrez le nom de la ville : ")
    filtrer_ville(donnees_meteo)

def sous_programme_2():
    print("Filtrer les données météo par date.")
    date_debut = input("Entrez la date de début (AAAA-MM-JJ) : ")
    date_fin = input("Entrez la date de fin (AAAA-MM-JJ) : ")
    filtrer_entre_dates(donnees_meteo, date_debut, date_fin)

def sous_programme_3():
    print("Filtrer les données météo par ville et par date.")
    ville = input("Entrez le nom de la ville : ")
    date_debut = input("Entrez la date de début (AAAA-MM-JJ) : ")
    date_fin = input("Entrez la date de fin (AAAA-MM-JJ) : ")
    filtrer_entre_dates_et_ville(donnees_meteo, date_debut, date_fin, ville)

def sous_programme_4():
    print("Calculer la moyenne des précipitations à Lyon.")
    moyenne_precipitations_lyon(donnees_meteo)

def sous_programme_5():
    print("Afficher les données météo complètes.")
    for enregistrement in donnees_meteo:
        print(enregistrement)

def afficher_menu():
    print("\nMenu du programme:")
    print("1. Filtrer les données météo par ville.")
    print("2. Filtrer les données météo par date.")
    print("3. Filtrer les données météo par ville et par date.")
    print("4. Calculer la moyenne des précipitations à Lyon.")
    print("5. Afficher les données météo complètes.")
    print("6. Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Entrez votre choix (1-6): ")
        
        if choix == '1':
            sous_programme_1()
        elif choix == '2':
            sous_programme_2()
        elif choix == '3':
            sous_programme_3()
        elif choix == '4':
            sous_programme_4()
        elif choix == '5':
            sous_programme_5()
        elif choix == '6':
            print("Fin du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

main()
