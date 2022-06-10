"""
Fonction qui renvoie le nom du énième mois de l'année
passé en argument.
"""

def nom_mois(n):
    mois = ["Janvier",
            "Février",
            "Mars",
            "Avril",
            "Mai",
            "Juin",
            "Juillet",
            "Août",
            "Septembre",
            "Octobre",
            "Novembre",
            "Décembre"]
    for i in mois:
        if mois.index(i) == n - 1:  # n - 1, car on part de l'index 0
            return i                # l'index de janvier = 0

print(nom_mois(4))

"""
La fonction retourne : Avril
"""

# ****** AUTRE METHODE ******

def nom_mois(n):
    mois = ["Janvier",
            "Février",
            "Mars",
            "Avril",
            "Mai",
            "Juin",
            "Juillet",
            "Août",
            "Septembre",
            "Octobre",
            "Novembre",
            "Décembre"]
    return mois[n - 1]     # les index commencent à 0

print(nom_mois(4))

"""
La fonction retourne : Avril
"""