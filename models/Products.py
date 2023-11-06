from .DataBase import DataBase
import mysql.connector

class Products(DataBase):
    def __init__(self, connection):
        super().__init__(connection)
        self.tableName = "products"

    def create(self):
        data = {
            "Reference": input("Référence (5 chiffres) : "),
            "Designation": input("Désignation : "),
            "Price": float(input("Prix : ")),
            "Stock": int(input("Stock : "))
        }
        self.createRecord(data)

    def read(self):
        recordReference = input("Entrez la référence du produit à afficher : ")
        self.readLine(recordReference)

    def readLine(self, recordReference):
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {self.tableName} WHERE Reference = %s"
            cursor.execute(query, (recordReference,))

            row = cursor.fetchone()
            if row:
                print(row)
            else:
                print("Aucun enregistrement trouvé.")

            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()

    def update(self):
        recordReference = input("Entrez la référence du produit à mettre à jour : ")

        print("Entrez les nouvelles valeurs (laisser vide pour ne pas changer) :")
        updatedData = {
            "Designation": input("Désignation : "),
            "Price": float(input("Prix : ")),  
            "Stock": int(input("Stock : "))
        }

        self.updateRecordByReference(recordReference, updatedData)

    def updateRecordByReference(self, reference, updatedData):
        try:
            setElements = ', '.join([f"{key} = %s" for key in updatedData.keys()])
            values = list(updatedData.values())
            
            cursor = self.connection.cursor()
            query = f"UPDATE {self.tableName} SET {setElements} WHERE Reference = %s" 
            values.append(reference)
            cursor.execute(query, values)
            self.connection.commit()

            if cursor.rowcount:
                print("L'enregistrement a été mis à jour avec succès.")
            else:
                print("Aucun enregistrement trouvé avec cette référence.")

            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()

    def delete(self):
        recordId = input("Entrez la référence du produit à supprimer : ")
        self.deleteRecord(recordId)

    def deleteRecord(self, recordId):
        try:
            cursor = self.connection.cursor()
            query = f"DELETE FROM {self.tableName} WHERE Reference = %s"
            cursor.execute(query, (recordId,))

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