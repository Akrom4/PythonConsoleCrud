from models.DatabaseManager import DatabaseManager
from models.Orders import Orders
from models.Clients import Clients
from models.LineOrders import LineOrders
from models.Products import Products
import json
# Main Program

if __name__ == '__main__':
    dbManager = None
    connection = None
    # Main loop, press Q to exit program
    while True:
        print('****** Base de données store ******')
        action = input("Choississez une option\n"
			"1 - Se connecter à la base de données\n"
			"2 - Se déconnecter de la base de données\n"
			"3 - Créer un enregistrement dans une table\n"
			"4 - Lire tous les enregistrements d\'une table et afficher leur contenu\n"
			"5 - Lire un enregistrement d'une table et afficher son contenu\n"
			"6 - Mettre à jour un enregistrement d'une table\n"
			"7 - Détruire un enregistrement d'une table\n"
            "Q - Quitter\n"
			"Veuillez saisir un chiffre entre 1 et 7\n"
        ).strip()

        # Quit
        
        if action.upper() == 'Q':
            if dbManager is not None:
                dbManager.close()
                print("Déconnexion de la base de données. Au revoir!")
            break
		
        # Connect to the database
        
        if action == '1':
            dbManager = DatabaseManager("localhost","root","","store2")
            connection = dbManager.getConnection()
            if connection.is_connected():
                dbName = connection.database
                print(f"Connexion à la base {dbName} réussie")
            else:
                print("Échec de la connexion à la base de données.")
        
        # Disconnect from the database

        elif action == '2' and connection is not None: 
            dbManager.close()
            dbManager = None
            connection = None  
            print("Déconnecté de la base de données.")
        elif action == '2' and connection is None: 
            print("Aucune base de données n'est connectée.")
        
        # CRUD actions
        
        elif action in ['3', '4', '5', '6', '7']:

            # Table selection

            if connection is not None and connection.is_connected():
                tableMapping = {
				'1': Clients,
				'2': Orders,
				'3': Products,
				'4': LineOrders
			    }
			
                tableChoice = input("Choississez une table\n"
                "1 - Clients\n"
                "2 - Orders\n"
                "3 - Products\n"
                "4 - LineOrders\n"
                "Veuillez saisir un chiffre entre 1 et 4\n")
                
                tableClass = tableMapping.get(tableChoice)

                # Object instanciation

                if tableClass:
                    tableInstance = tableClass(connection)

                    # Create a new record in a table

                    if action == '3':
                        tableInstance.create()

                    # Read and display all the data from a table

                    if action == '4':
                        results = tableInstance.readAll()
                        objList = []
                        for row in results:
                            print(row)
                            objList.append(tableInstance.toObject(row))
                        for instance in objList:
                            print(instance)                         

                    # Read and display a single record from a table

                    if action == '5':
                        tableInstance.read()

                    # Update a record

                    if action == '6':
                        tableInstance.update()
                    
                    # Delete a record

                    if action == '7':
                        tableInstance.delete()
                else:
                    print("Table sélectionnée invalide\n")
            else:
                print("Vous n\'êtes pas connecté à la base de données\n")