from .DataBase import DataBase

class Clients(DataBase):
    def __init__(self, connection, Id=None,LastName=None, FirstName=None, Address=None, City=None):
        super().__init__(connection)
        self.tableName = "clients"
        self.Id = Id
        self.LastName = LastName
        self.FirstName = FirstName
        self.Address = Address
        self.City = City

    # Client Object
    def toObject(self, Id=None, LastName=None,FirstName=None, Address=None, City=None):
        self.Id = Id
        self.LastName = LastName
        self.FirstName = FirstName
        self.Address = Address
        self.City = City

        return self

    # Create a new client
    def create(self):
        data = {
            "LastName": input("Nom de famille : "),
            "FirstName": input("Prénom : "),
            "Address": input("Adresse : "),
            "City": input("Ville : "),
        }
        self.createRecord(data)

    # Read and display a single record

    def read(self):
        recordId = int(input("Entrez l'identifiant du client à afficher : "))
        self.readLine(recordId)

    # Update a record

    def update(self):
        recordId = int(input("Entrez l'identifiant du client à mettre à jour : "))

        print("Entrez les nouvelles valeurs : ")
        updatedData = {
            "LastName": input("Nom de famille : "),
            "FirstName": input("Prénom : "),
            "Address": input("Adresse : "),
            "City": input("Ville : "),
        }

        self.updateRecord(recordId, updatedData)

    def delete(self):
        recordId = int(input("Entrez l'identifiant du client à supprimer : "))
        self.deleteRecord(recordId)
