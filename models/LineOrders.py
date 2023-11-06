from .DataBase import DataBase
import mysql.connector

class LineOrders(DataBase):
    def __init__(self, connection):
        super().__init__(connection)
        self.tableName = "linesorders"

    def create(self):
        data = {
            "OrderId": int(input("Id de la commande : ")),
            "ProductReference": input("Référence du produit : "),
            "Quantity": int(input("Quantité : "))
        }
        self.createRecord(data)
    
    def read(self):
        orderId = int(input("Entrez l'identifiant de la commande : "))
        productReference = input("Entrez la référence du produit : ")
        self.readLine(orderId, productReference)

    # Overrides the method inherited from DataBase

    def readLine(self, orderId, productReference):
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {self.tableName} WHERE OrderId = %s AND ProductReference = %s"
            cursor.execute(query, (orderId, productReference))

            row = cursor.fetchone()
            if row:
                print(row)
            else:
                print("Aucun enregistrement trouvé avec ces identifiants.")

            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()
    
    def update(self):
        identifier = {
            "OrderId": int(input("Entrez l'identifiant de la commande : ")),
            "ProductReference": input("Entrez la référence du produit : "),
        }

        updatedData = {
            "Quantity": input("Nouvelle quantité : "),
        }

        self.updateRecord(identifier, updatedData)
    
    def delete(self):
        orderId = int(input("Entrez l'identifiant de la commande : "))
        productReference = input("Entrez la référence du produit : ")
        self.deleteRecord(orderId, productReference)
    
    def deleteRecord(self, orderId, productReference):
        try:
            cursor = self.connection.cursor()
            query = f"DELETE FROM {self.tableName} WHERE OrderId = %s AND ProductReference = %s"
            cursor.execute(query, (orderId,productReference))

            if cursor.rowcount:
                print("L'enregistrement a été supprimé avec succès.")
            else:
                print("Aucun enregistrement trouvé.")

            self.connection.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()
