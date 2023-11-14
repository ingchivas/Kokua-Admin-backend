import mysql.connector

# Datos de conexión
host = "kokua-srv.mysql.database.azure.com"
user = "kokuamaster"
password = "ingSoftwareUP2023"
database = "KOKUA"

def DBConnection():
    # Intenta establecer la conexión
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Conexión establecida")
            return connection    

    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return None  



    # finally:
    #     # Cerrar la conexión al finalizar
    #     if 'connection' in locals() and connection.is_connected():
    #         cursor.close()
    #         connection.close()
    #         print("Conexión cerrada")