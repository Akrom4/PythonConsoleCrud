import mysql.connector

class DataBase:
    def __init__(self, connection):
        self.connection = connection
        self.tableName = None

    # Read and prints all the data from a table
    def readAll(self):
        cursor = self.connection.cursor()
        query = f"SELECT * FROM {self.tableName}"
        cursor.execute(query)

        rows = cursor.fetchall()
        objList = []
        for row in rows:
            objList.append(row)
        cursor.close()
        
        return objList

    # Create a new record

    def createRecord(self, data):
        try:
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            query = f"INSERT INTO {self.tableName} ({columns}) VALUES ({placeholders})"
            
            cursor = self.connection.cursor()
            cursor.execute(query, list(data.values()))
            self.connection.commit()
            print("Enregistrement créé avec succès.")
        except mysql.connector.Error as err:
            print(f"Erreur : {err}")
        finally:
            if cursor: 
                cursor.close()

    # Read a single record

    def readLine(self, recordId):
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {self.tableName} WHERE id = %s"
            cursor.execute(query, (recordId,))

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

    # Delete a single record

    def deleteRecord(self, recordId):
        try:
            cursor = self.connection.cursor()
            query = f"DELETE FROM {self.tableName} WHERE id = %s"
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

    # Update a record

    def updateRecord(self, identifier, updatedData):
        try:
            setElements = ', '.join([f"{key} = %s" for key in updatedData.keys()])
            values = list(updatedData.values())

            cursor = self.connection.cursor()

            if isinstance(identifier, dict):  # for composite primary keys
                whereClause = ' AND '.join([f"{key} = %s" for key in identifier.keys()])
                query = f"UPDATE {self.tableName} SET {setElements} WHERE {whereClause}"
                values.extend(identifier.values())
            else:  # for single primary key
                query = f"UPDATE {self.tableName} SET {setElements} WHERE id = %s"
                values.append(identifier)

            cursor.execute(query, values)
            self.connection.commit()

            if cursor.rowcount:
                print("L'enregistrement a été mis à jour avec succès.")
            else:
                print("Aucun enregistrement trouvé avec cet identifiant.")

            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()