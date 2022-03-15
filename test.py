from form import Form
from menu import Menu
from view import View


# View(title= "Bienvenue au jeu d'échec", content= "Gérer les joueurs").show()
# Menu(title= "Bienvenue au chess manager version 1.0", 
#       options= ["Gérer les joueurs","Gérer les tournois", "Gérer les matchs"]).show()

print(Form(title="Gérer les joueurs",
           fields=[("Nom", "Last_name"),
                   ("Prénom", "First_name"),
                   ("Date de naissance", "Birth_date")]).show())