from .DataBase import DataBase

class Orders(DataBase):
    def __init__(self, connection):
        super().__init__(connection)
        self.tableName = "orders"

    def create(self):
        data = {
            "Date": input("Date (YYYY-MM-DD) : "),
            "ClientId": int(input("Id du client : "))
        }
        self.createRecord(data)

    def read(self):
        recordId = int(input("Entrez l'identifiant de la commande à afficher : "))
        self.readLine(recordId)

    def delete(self):
        recordId = int(input("Entrez l'identifiant de la commande à supprimer : "))
        self.deleteRecord(recordId)
    
    def update(self):
        recordId = int(input("Entrez l'identifiant de la commande à mettre à jour : "))

        print("Entrez les nouvelles valeurs : ")
        updatedData = {
            "Date": input("Date (YYYY-MM-DD) : "),
            "ClientId": int(input("Id du client : "))
        }

        self.updateRecord(recordId, updatedData)

