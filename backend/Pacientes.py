from DBConnect import DBConnection
import mysql.connector

"""

DROP TABLE IF EXISTS `Pacientes`;

CREATE TABLE `Pacientes` (
  `IDPaciente` INT PRIMARY KEY AUTO_INCREMENT,
  `Nombre` VARCHAR(255),
  `Apellido` VARCHAR(255),
  `Padecimento` VARCHAR(255),
  `EstatusPaciente` ENUM('Muerto','Critico', 'Atencion_Constante', 'Estable','Servicio_Expirado'),
  `SaldoActual` DOUBLE,
  `IDUsuario` INT,
  FOREIGN KEY (`IDUsuario`) REFERENCES `Usuarios`(`IDUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Usuarios`;

CREATE TABLE `Usuarios` (
  `IDUsuario` INT PRIMARY KEY AUTO_INCREMENT,
  `Username` VARCHAR(100),
  `Password` VARCHAR(100),
  `TipoAcceso` ENUM('Almacen','Proveedor','Ejecutivo','Compras', 'Medico', 'Paciente', 'Administrador')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

"""


def ConsultarPacientes():
    """ 
    Consulta todos los pacientes registrados en la base de datos

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Pacientes")
        result = cursor.fetchall()

        if result:
            pacientes = []
            for paciente in result:
                pacientes.append({
                    "IDPaciente": paciente[0],
                    "Nombre": paciente[1],
                    "Apellido": paciente[2],
                    "Padecimento": paciente[3],
                    "EstatusPaciente": paciente[4],
                    "SaldoActual": paciente[5],
                    "IDUsuario": paciente[6]
                })
            return {"status": 200, "result": pacientes}
        else:
            return {"status": 404, "message": "Pacientes no encontrados"}
    
    except mysql.connector.Error as err:
        print("Error al consultar los pacientes: {}".format(err))
        return {"status": 500, "message": "Error al consultar los pacientes"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarPacientePorID(id_paciente):
    """ 
    Consulta un paciente específico por su ID

    Args:
        id_paciente (int): ID del paciente a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Pacientes WHERE IDPaciente = {}".format(id_paciente))
        result = cursor.fetchone()

        if result:
            paciente = {
                "IDPaciente": result[0],
                "Nombre": result[1],
                "Apellido": result[2],
                "Padecimento": result[3],
                "EstatusPaciente": result[4],
                "SaldoActual": result[5],
                "IDUsuario": result[6]
            }
            return {"status": 200, "result": paciente}
        else:
            return {"status": 404, "message": "Paciente no encontrado"}
    
    except mysql.connector.Error as err:
        print("Error al consultar el paciente: {}".format(err))
        return {"status": 500, "message": "Error al consultar el paciente"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def AgregarPaciente(paciente):
    """ 
    Agrega un nuevo paciente a la base de datos

    Args:
        paciente (dict): Diccionario con los datos del paciente a agregar

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    
    # primero crear el usuario, obtener el id y luego crear el paciente
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    try:
        TipoAcceso = "Paciente"
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Usuarios (Username, Password, TipoAcceso) VALUES (%s, %s, %s)", (paciente["Username"], paciente["Password"], paciente["TipoAcceso"]))
        connection.commit()
        id_usuario = cursor.lastrowid
        cursor.execute("INSERT INTO Pacientes (Nombre, Apellido, Padecimento, EstatusPaciente, SaldoActual, IDUsuario, Email, Insurance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (paciente["Nombre"], paciente["Apellido"], paciente["Padecimento"], paciente["EstatusPaciente"], paciente["SaldoActual"], id_usuario, paciente["Email"], paciente["Insurance"]))
        connection.commit()
        return {"status": 200, "message": "Paciente agregado exitosamente"}
    
    except mysql.connector.Error as err:
        print("Error al agregar el paciente: {}".format(err))
        return {"status": 500, "message": "Error al agregar el paciente"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def AgregarPacienteSinUsuario(paciente):
    """ 
    Agrega un nuevo paciente a la base de datos sin crear un usuario asociado

    Args:
        paciente (dict): Diccionario con los datos del paciente a agregar

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    
    # primero crear el usuario, obtener el id y luego crear el paciente
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    try:
        TipoAcceso = "Paciente"
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Pacientes (Nombre, Apellido, Padecimento, EstatusPaciente, SaldoActual) VALUES (%s, %s, %s, %s, %s)", (paciente["Nombre"], paciente["Apellido"], paciente["Padecimento"], paciente["EstatusPaciente"], paciente["SaldoActual"], paciente["Email"], paciente["Insurance"]))
        connection.commit()
        return {"status": 200, "message": "Paciente agregado exitosamente"}
    
    except mysql.connector.Error as err:
        print("Error al agregar el paciente: {}".format(err))
        return {"status": 500, "message": "Error al agregar el paciente"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ActualizarPaciente(id_paciente, paciente):
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE Usuarios SET Username = %s, Password = %s, TipoAcceso = %s WHERE IDUsuario = %s", 
                       (paciente["Username"], paciente["Password"], paciente["TipoAcceso"], paciente["IDUsuario"]))
        connection.commit()
        cursor.execute("UPDATE Pacientes SET Nombre = %s, Apellido = %s, Padecimento = %s, EstatusPaciente = %s, SaldoActual = %s, Email = %s, Insurance = %s WHERE IDPaciente = %s", 
                       (paciente["Nombre"], paciente["Apellido"], paciente["Padecimento"], paciente["EstatusPaciente"], paciente["SaldoActual"], paciente["Email"], paciente["Insurance"], id_paciente))
        connection.commit()
        return {"status": 200, "message": "Paciente actualizado exitosamente"}
    
    except mysql.connector.Error as err:
        print("Error al actualizar el paciente: {}".format(err))
        return {"status": 500, "message": "Error al actualizar el paciente"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def EliminarPaciente(id_paciente):
    """ 
    Elimina un paciente específico

    Args:
        id_paciente (int): ID del paciente a eliminar

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    
    # primero eliminar el usuario, obtener el id y luego eliminar el paciente
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT IDUsuario FROM Pacientes WHERE IDPaciente = {}".format(id_paciente))
        result = cursor.fetchone()
        if result:
            id_usuario = result[0]
            cursor.execute("DELETE FROM Usuarios WHERE IDUsuario = {}".format(id_usuario))
            connection.commit()
            cursor.execute("DELETE FROM Pacientes WHERE IDPaciente = {}".format(id_paciente))
            connection.commit()
            return {"status": 200, "message": "Paciente eliminado exitosamente"}
        else:
            return {"status": 404, "message": "Paciente no encontrado"}
    
    except mysql.connector.Error as err:
        print("Error al eliminar el paciente: {}".format(err))
        return {"status": 500, "message": "Error al eliminar el paciente"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")