from DBConnect import DBConnection
from mysql import connector

#____________________________________________________________Citas____________________________________________________________________


def AgendarCita(id_paciente, id_doctor, tipo_cita, fecha, estatus_cita= "Agendada"):
    
    """
    Agrega una cita a la base de datos

    Args:
        id_paciente (int): ID del paciente
        id_doctor (int): ID del doctor
        tipo_cita (str): Tipo de cita
        fecha (str): Fecha de la cita

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta agregar la cita
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Citas (IDPaciente, IDDoctor, TipoCita, EstatusCita, Fecha) VALUES (%s, %s, %s, %s, %s)", (id_paciente, id_doctor, tipo_cita, estatus_cita, fecha))
        connection.commit()
        return {"status": 200, "message": "Cita agregada exitosamente"}

    except connector.Error as err:
        print("Error al agregar la cita: {}".format(err))
        return {"status": 500, "message": "Error al agregar la cita"}

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarCitas():
    """
    Consulta todas las citas de la base de datos

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta consultar las citas
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT IDCita, IDPaciente, IDDoctor, TipoCita, EstatusCita, Fecha FROM Citas")
        result = cursor.fetchall()

        citas = []
        for cita in result:
            citas.append({
                "id_cita": cita[0],
                "id_paciente": cita[1],
                "id_doctor": cita[2],
                "tipo_cita": cita[3],
                "estatus_cita": cita[4],
                "fecha": cita[5]
            })
        return {"status": 200, "result": citas}

    except connector.Error as err:
        print("Error al consultar las citas: {}".format(err))
        return {"status": 500, "message": "Error al consultar las citas"}

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarCita(id_cita):
    """
    Consulta una cita de la base de datos

    Args:
        id_cita (int): ID de la cita

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta consultar la cita
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT IDCita, IDPaciente, IDDoctor, TipoCita, EstatusCita, Fecha FROM Citas WHERE IDCita = %s", (id_cita,))
        result = cursor.fetchone()

        if result:
            cita = []
            cita.append({
                "id_cita": result[0],
                "id_paciente": result[1],
                "id_doctor": result[2],
                "tipo_cita": result[3],
                "estatus_cita": result[4],
                "fecha": result[5]
            })
            return {"status": 200, "result": cita}
        else:
            return {"status": 404, "message": "Cita no encontrada"}

    except connector.Error as err:
        print("Error al consultar la cita: {}".format(err))
        return {"status": 500, "message": "Error al consultar la cita"}

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarCitasPaciente(idPaciente):
    """
    Consulta las citas de un paciente específico

    Args:
        idPaciente (int): ID del paciente

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Citas WHERE IDPaciente = %s", (idPaciente,))
        result = cursor.fetchall()

        citas = []
        for cita in result:
            citas.append({
                "id_cita": cita[0],
                "id_paciente": cita[1],
                "id_doctor": cita[2],
                "tipo_cita": cita[3],
                "estatus_cita": cita[4],
                "fecha": cita[5]
            })
        return {"status": 200, "result": citas}

    except connector.Error as err:
        print("Error al consultar las citas: {}".format(err))
        return {"status": 500, "message": "Error al consultar las citas"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarCitasDoctor(idDoctor):
    """
    Consulta las citas de un doctor específico

    Args:
        idDoctor (int): ID del doctor

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Citas WHERE IDDoctor = %s", (idDoctor,))
        result = cursor.fetchall()

        citas = []
        for cita in result:
            citas.append({
                "id_cita": cita[0],
                "id_paciente": cita[1],
                "id_doctor": cita[2],
                "tipo_cita": cita[3],
                "estatus_cita": cita[4],
                "fecha": cita[5]
            })
        return {"status": 200, "result": citas}

    except connector.Error as err:
        print("Error al consultar las citas: {}".format(err))
        return {"status": 500, "message": "Error al consultar las citas"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ActualizarCita(idCita, idPaciente, idDoctor, tipoCita, estatusCita, fecha):
    """
    Actualiza una cita de la base de datos

    Args:
        idCita (int): ID de la cita
        idPaciente (int): ID del paciente
        idDoctor (int): ID del doctor
        tipoCita (str): Tipo de cita
        estatusCita (str): Estatus de la cita
        fecha (str): Fecha de la cita

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta actualizar la cita
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE Citas SET IDPaciente = %s, IDDoctor = %s, TipoCita = %s, EstatusCita = %s, Fecha = %s WHERE IDCita = %s", (idPaciente, idDoctor, tipoCita, estatusCita, fecha, idCita))
        connection.commit()
        return {"status": 200, "message": "Cita actualizada exitosamente"}

    except connector.Error as err:
        print("Error al actualizar la cita: {}".format(err))
        return {"status": 500, "message": "Error al actualizar la cita"}

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ActualizarEstatusCita(idCita, estatusCita):
    """
    Actualiza el estatus de una cita de la base de datos

    Args:
        idCita (int): ID de la cita
        estatusCita (str): Estatus de la cita

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta actualizar el estatus de la cita
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE Citas SET EstatusCita = %s WHERE IDCita = %s", (estatusCita, idCita))
        connection.commit()
        return {"status": 200, "message": "Estatus de la cita actualizado exitosamente"}

    except connector.Error as err:
        print("Error al actualizar el estatus de la cita: {}".format(err))
        return {"status": 500, "message": "Error al actualizar el estatus de la cita"}

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def EliminarCita(idCita):
    """
    Elimina una cita de la base de datos

    Args:
        idCita (int): ID de la cita

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta eliminar la cita
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Citas WHERE IDCita = %s", (idCita,))
        connection.commit()
        return {"status": 200, "message": "Cita eliminada exitosamente"}

    except connector.Error as err:
        print("Error al eliminar la cita: {}".format(err))
        return {"status": 500, "message": "Error al eliminar la cita"}

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")