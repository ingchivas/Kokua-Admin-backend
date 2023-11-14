from DBConnect import DBConnection
import mysql.connector
import json

#______________________________________________________Facturas_________________________________________________________________

def ConsultarFacturas():
    """ 
    Consulta todas las facturas registradas en la base de datos

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Factura")
        result = cursor.fetchall()
        return {"status": 200, "message": "Facturas consultadas", "facturas": result}
    
    except mysql.connector.Error as err:
        print("Error al consultar las facturas: {}".format(err))
        return {"status": 500, "message": "Error al consultar las facturas"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarFacturaPorID(id_factura):
    """ 
    Consulta una factura específica por su ID

    Args:
        id_factura (int): ID de la factura a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Factura WHERE idFactura = %s", (id_factura,))
        result = cursor.fetchone()

        if result:
            return {"status": 200, "message": "Factura consultada", "factura": result}
        else:
            return {"status": 404, "message": "Factura no encontrada"}

    except mysql.connector.Error as err:
        print("Error al consultar la factura: {}".format(err))
        return {"status": 500, "message": "Error al consultar la factura"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarCitaAsociada(id_factura):
    """ 
    Consulta la cita asociada a una factura específica

    Args:
        id_factura (int): ID de la factura

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT C.* FROM Citas C INNER JOIN Factura F ON C.IDCita = F.idCita WHERE F.idFactura = %s", (id_factura,))
        result = cursor.fetchone()

        if result:
            return {"status": 200, "message": "Cita consultada", "cita": result}
        else:
            return {"status": 404, "message": "Cita no encontrada"}

    except mysql.connector.Error as err:
        print("Error al consultar la cita asociada: {}".format(err))
        return {"status": 500, "message": "Error al consultar la cita asociada"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def InsertarFactura(id_cita, costo):
    """ 
    Inserta una nueva factura en la base de datos

    Args:
        id_cita (int): ID de la cita asociada a la factura
        costo (float): Costo de la factura

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la inserción
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Factura (idCita, Costo) VALUES (%s, %s)", (id_cita, costo))
        connection.commit()
        return {"status": 201, "message": "Factura insertada correctamente"}

    except mysql.connector.Error as err:
        print("Error al insertar la factura: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al insertar la factura"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ActualizarFactura(id_factura, nuevo_costo):
    """ 
    Actualiza el costo de una factura específica

    Args:
        id_factura (int): ID de la factura a actualizar
        nuevo_costo (float): Nuevo costo de la factura

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la actualización
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE Factura SET Costo = %s WHERE idFactura = %s", (nuevo_costo, id_factura))
        connection.commit()
        return {"status": 200, "message": "Factura actualizada correctamente"}

    except mysql.connector.Error as err:
        print("Error al actualizar la factura: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al actualizar la factura"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def EliminarFactura(id_factura):
    """ 
    Elimina una factura específica

    Args:
        id_factura (int): ID de la factura a eliminar

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la eliminación
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Factura WHERE idFactura = %s", (id_factura,))
        connection.commit()
        return {"status": 200, "message": "Factura eliminada correctamente"}

    except mysql.connector.Error as err:
        print("Error al eliminar la factura: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al eliminar la factura"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarFacturasOrdenadasPorCosto():
    """ 
    Consulta todas las facturas ordenadas por costo

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Factura ORDER BY Costo")
        result = cursor.fetchall()
        return {"status": 200, "message": "Facturas consultadas y ordenadas por costo", "facturas": result}
    
    except mysql.connector.Error as err:
        print("Error al consultar las facturas ordenadas por costo: {}".format(err))
        return {"status": 500, "message": "Error al consultar las facturas ordenadas por costo"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

