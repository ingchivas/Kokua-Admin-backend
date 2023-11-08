import pyodbc

# Configura las credenciales de la base de datos
server_name = "kokua-srv.mysql.database.azure.com"
database_name = "kokua"
username = "kokuamaster"
password = "ingSoftwareUP2023"

# Crea una conexión a la base de datos
connection = pyodbc.connect(
    f"DRIVER={'ODBC Driver 18 for SQL Server'};SERVER={server_name};DATABASE={database_name};UID={username};PWD={password}"
)

# Imprime el nombre de la base de datos
print(connection.database)
