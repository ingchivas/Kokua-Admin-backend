from DBConnect import DBConnection
import mysql.connector

# ______________________________________________________Ordenes_________________________________________________________________

def ConsultarTodasLasOrdenes():
    """
    Consulta todas las órdenes registradas en la base de datos

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ordenes")
        result = cursor.fetchall()
        
        if result:
            return {"status": 200, "result": result}
        else:
            return {"status": 404, "message": "Órdenes no encontradas"}

    except mysql.connector.Error as err:
        print("Error al consultar las órdenes: {}".format(err))
        return {"status": 500, "message": "Error al consultar las órdenes"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def ConsultarOrdenPorID(id_orden):
    """
    Consulta una orden específica por su ID

    Args:
        id_orden (int): ID de la orden a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ordenes WHERE IDOrden = %s", (id_orden,))
        result = cursor.fetchone()
        if result:
            return {"status": 200, "result": result}
        else:
            return {"status": 404, "message": "Orden no encontrada"}
    except mysql.connector.Error as err:
        print("Error al consultar la orden: {}".format(err))
        return {"status": 500, "message": "Error al consultar la orden"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def ConsultarOrdenesPorPaciente(id_paciente):
    """
    Consulta todas las órdenes registradas en la base de datos

    Args:
        id_paciente (int): ID del paciente a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta 
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ordenes WHERE IDUsuario = %s", (id_paciente,))
        result = cursor.fetchall()
        if result:
            return {"status": 200, "result": result}
        else:
            return {"status": 404, "message": "Órdenes no encontradas para el paciente"}
    except mysql.connector.Error as err:
        print("Error al consultar las órdenes por paciente: {}".format(err))
        return {"status": 500, "message": "Error al consultar las órdenes por paciente"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def ConsultarOrdenesPorMedicina(id_medicina):
    """
    Consulta todas las órdenes registradas en la base de datos

    Args:
        id_medicina (int): ID de la medicina a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ordenes WHERE IDMedicina = %s", (id_medicina,))
        result = cursor.fetchall()
        if result:
            return {"status": 200, "result": result}
        else:
            return {"status": 404, "message": "Órdenes no encontradas para la medicina"}
    except mysql.connector.Error as err:
        print("Error al consultar las órdenes por medicina: {}".format(err))
        return {"status": 500, "message": "Error al consultar las órdenes por medicina"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def ConsultarOrdenesPorProveedor(id_proveedor):
    """
    Consulta todas las órdenes registradas en la base de datos

    Args:
        id_proveedor (int): ID del proveedor a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ordenes WHERE IDProveedor = %s", (id_proveedor,))
        result = cursor.fetchall()
        if result:
            return {"status": 200, "result": result}
        else:
            return {"status": 404, "message": "Órdenes no encontradas para el proveedor"}
    except mysql.connector.Error as err:
        print("Error al consultar las órdenes por proveedor: {}".format(err))
        return {"status": 500, "message": "Error al consultar las órdenes por proveedor"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def ConsultarOrdenesPorCosto(mayor_a_menor=True):
    """
    Consulta todas las órdenes registradas en la base de datos

    Args:
        mayor_a_menor (bool): Orden en la que se devolverán las órdenes

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor(dictionary=True)
        if mayor_a_menor:
            cursor.execute("SELECT * FROM Ordenes ORDER BY CostoTotal DESC")
        else:
            cursor.execute("SELECT * FROM Ordenes ORDER BY CostoTotal ASC")
        result = cursor.fetchall()
        if result:
            return {"status": 200, "result": result}
        else:
            return {"status": 404, "message": "Órdenes no encontradas"}
    except mysql.connector.Error as err:
        print("Error al consultar las órdenes por costo: {}".format(err))
        return {"status": 500, "message": "Error al consultar las órdenes por costo"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def ConsultarOrdenesPorEstatus(estatus):
    """
    Consulta todas las órdenes registradas en la base de datos

    Args:
        estatus (str): Estatus a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ordenes WHERE Estatus = %s", (estatus,))
        result = cursor.fetchall()
        if result:
            return {"status": 200, "result": result}
        else:
            return {"status": 404, "message": "Órdenes no encontradas para el estatus especificado"}
    except mysql.connector.Error as err:
        print("Error al consultar las órdenes por estatus: {}".format(err))
        return {"status": 500, "message": "Error al consultar las órdenes por estatus"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def ConsultarOrdenesPorCantidad(mayor_a_menor=True):
    """
    Consulta todas las órdenes registradas en la base de datos

    Args:
        mayor_a_menor (bool): Orden en la que se devolverán las órdenes

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor(dictionary=True)
        if mayor_a_menor:
            cursor.execute("SELECT * FROM Ordenes ORDER BY CantidadOrdenada DESC")
        else:
            cursor.execute("SELECT * FROM Ordenes ORDER BY CantidadOrdenada ASC")
        result = cursor.fetchall()
        if result:
            return {"status": 200, "result": result}
        else:
            return {"status": 404, "message": "Órdenes no encontradas"}
    except mysql.connector.Error as err:
        print("Error al consultar las órdenes por cantidad: {}".format(err))
        return {"status": 500, "message": "Error al consultar las órdenes por cantidad"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def ConsultarOrdenesPorEntregaEsperada(fecha_entrega):
    """
    Consulta todas las órdenes registradas en la base de datos

    Args:
        fecha_entrega (str): Fecha de entrega esperada a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ordenes WHERE EntregaEsperada = %s", (fecha_entrega,))
        result = cursor.fetchall()
        if result:
            return {"status": 200, "result": result}
        else:
            return {"status": 404, "message": "Órdenes no encontradas para la fecha de entrega esperada"}
    except mysql.connector.Error as err:
        print("Error al consultar las órdenes por entrega esperada: {}".format(err))
        return {"status": 500, "message": "Error al consultar las órdenes por entrega esperada"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def ConsultarOrdenesPorFechaOrden(fecha_orden):
    """
    Consulta todas las órdenes registradas en la base de datos

    Args:
        fecha_orden (str): Fecha de orden a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ordenes WHERE FechaOrden = %s", (fecha_orden,))
        result = cursor.fetchall()
        if result:
            return {"status": 200, "result": result}
        else:
            return {"status": 404, "message": "Órdenes no encontradas para la fecha de orden"}
    except mysql.connector.Error as err:
        print("Error al consultar las órdenes por fecha de orden: {}".format(err))
        return {"status": 500, "message": "Error al consultar las órdenes por fecha de orden"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def ConsultarOrdenesPorFechaEntrega(fecha_entrega):
    """
    Consulta todas las órdenes registradas en la base de datos

    Args:
        fecha_entrega (str): Fecha de entrega a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ordenes WHERE FechaEntrega = %s", (fecha_entrega,))
        result = cursor.fetchall()
        if result:
            return {"status": 200, "result": result}
        else:
            return {"status": 404, "message": "Órdenes no encontradas para la fecha de entrega"}
    except mysql.connector.Error as err:
        print("Error al consultar las órdenes por fecha de entrega: {}".format(err))
        return {"status": 500, "message": "Error al consultar las órdenes por fecha de entrega"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def InsertarOrden(IDMedicina, IDProveedor, Cantidad, Costo, FechaOrden, FechaEntrega, Estatus):
    """
    Inserta una orden en la base de datos

    Args:
        IDMedicina (int): ID de la medicina a ordenar
        IDProveedor (int): ID del proveedor de la medicina
        Cantidad (int): Cantidad de medicina a ordenar
        Costo (float): Costo total de la orden
        FechaOrden (str): Fecha en la que se ordenó la medicina
        FechaEntrega (str): Fecha en la que se espera que llegue la medicina
        Estatus (str): Estatus de la orden

    Returns:
        (dict): Diccionario con el resultado de la inserción
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Ordenes (IDMedicina, IDProveedor, CantidadOrdenada, CostoTotal, FechaOrden, EntregaEsperada, Estatus) VALUES (%s, %s, %s, %s, %s, %s, %s)", (IDMedicina, IDProveedor, Cantidad, Costo, FechaOrden, FechaEntrega, Estatus))
        connection.commit()
        return {"status": 200, "result": "Orden registrada"}
    except mysql.connector.Error as err:
        print("Error al registrar la orden: {}".format(err))
        return {"status": 500, "message": "Error al registrar la orden"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def ActualizarOrden(IDorden, IDMedicina, IDProveedor, Cantidad, Costo, FechaOrden, FechaEntrega, Estatus):
    """
    Actualiza una orden en la base de datos

    Args:
        IDorden (int): ID de la orden a actualizar
        IDMedicina (int): ID de la medicina a ordenar
        IDProveedor (int): ID del proveedor de la medicina
        Cantidad (int): Cantidad de medicina a ordenar
        Costo (float): Costo total de la orden
        FechaOrden (str): Fecha en la que se ordenó la medicina
        FechaEntrega (str): Fecha en la que se espera que llegue la medicina
        Estatus (str): Estatus de la orden

    Returns:
        (dict): Diccionario con el resultado de la actualización
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE Ordenes SET IDMedicina = %s, IDProveedor = %s, CantidadOrdenada = %s, CostoTotal = %s, FechaOrden = %s, EntregaEsperada = %s, Estatus = %s WHERE IDOrden = %s", (IDMedicina, IDProveedor, Cantidad, Costo, FechaOrden, FechaEntrega, Estatus, IDorden))
        connection.commit()
        return {"status": 200, "result": "Orden actualizada"}
    except mysql.connector.Error as err:
        print("Error al actualizar la orden: {}".format(err))
        return {"status": 500, "message": "Error al actualizar la orden"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def EliminarOrden(IDORden):
    """
    Elimina una orden específica por su ID

    Args:
        IDORden (int): ID de la orden a eliminar

    Returns:
        (dict): Diccionario con el resultado de la eliminación
    """
    connection = DBConnection()
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Ordenes WHERE IDOrden = %s", (IDORden,))
        connection.commit()
        return {"status": 200, "result": "Orden eliminada"}
    except mysql.connector.Error as err:
        print("Error al eliminar la orden: {}".format(err))
        return {"status": 500, "message": "Error al eliminar la orden"}
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()