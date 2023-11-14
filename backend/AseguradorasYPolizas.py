import mysql.connector
import json
from DBConnect import DBConnection


#------------------------Aseguradoras------------------------#

def RegistrarAseguradora(NombreAseguradora, Direccion, NumContacto):
    """
    Registra una aseguradora en la base de datos

    Args:
        IDAseguradora (int): ID de la aseguradora
        NombreAseguradora (str): Nombre de la aseguradora
        Direccion (str): Dirección de la aseguradora
        NumContacto (str): Número de contacto de la aseguradora

    Returns:
        bool: True si se registró correctamente, False si no
    """

    
    connection = DBConnection()
    cursor = connection.cursor()

    IDAseguradora = cursor.execute("SELECT MAX(IDAseguradora) FROM Aseguradoras")
    IDAseguradora = cursor.fetchone()[0]
    IDAseguradora = IDAseguradora + 1

    try:
        cursor.execute("INSERT INTO Aseguradoras (IDAseguradora, NombreAseguradora, Direccion, NumContacto) VALUES (%s, %s, %s, %s)",
                       (IDAseguradora, NombreAseguradora, Direccion, NumContacto))
        connection.commit()
        return {"status": 200, "message": "Aseguradora registrada"}
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return 
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarAseguradoras():
    """
    Consulta las aseguradoras registradas en la base de datos

    Returns:
        Aseguradoras (dict): Lista de aseguradoras
    """

    connection = DBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM Aseguradoras")
        result = cursor.fetchall()
        
        if len(result) > 0:
            # Convertir el resultado a un diccionario
            aseguradoras = []
            for i in result:
                aseguradoras.append({
                    'IDAseguradora': i[0],
                    'NombreAseguradora': i[1],
                    'Direccion': i[2],
                    'NumContacto': i[3]
                })
            return {"status": 200, "result": aseguradoras }
        else:
            return None
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return None
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarAseguradora(IDAseguradora):
    """
    Consulta una aseguradora registrada en la base de datos

    Args:
        IDAseguradora (int): ID de la aseguradora

    Returns:
        Aseguradora (dict): Aseguradora
    """

    connection = DBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM Aseguradoras WHERE IDAseguradora = %s", (IDAseguradora,))
        result = cursor.fetchall()
        
        if len(result) > 0:
            # Convertir el resultado a un diccionario
            aseguradora = []
            for i in result:
                aseguradora.append({
                    'IDAseguradora': i[0],
                    'NombreAseguradora': i[1],
                    'Direccion': i[2],
                    'NumContacto': i[3]
                })
            return {"status": 200, "result": aseguradora}
        else:
            return None
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return None
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarAseguradorasPolizas(IDAseguradora):
    """
    Consulta las aseguradoras registradas en la base de datos

    Args:
        IDAseguradora (int): ID de la aseguradora

    Returns:
        Aseguradoras (dict): Lista de aseguradoras
    """

    connection = DBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM Aseguradoras WHERE IDAseguradora = %s", (IDAseguradora,))
        result = cursor.fetchall()
        
        if len(result) > 0:
            # Convertir el resultado a un diccionario
            aseguradoras = []
            for i in result:
                aseguradoras.append({
                    'IDAseguradora': i[0],
                    'NombreAseguradora': i[1],
                    'Direccion': i[2],
                    'NumContacto': i[3]
                })
            return {"status": 200, "result": aseguradoras }
        else:
            return None
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return None
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def EliminarAseguradora(IDAseguradora):
    """
    Elimina una aseguradora registrada en la base de datos

    Args:
        IDAseguradora (int): ID de la aseguradora

    Returns:
        bool: True si se eliminó correctamente, False si no
    """

    connection = DBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM Aseguradoras WHERE IDAseguradora = %s", (IDAseguradora,))
        connection.commit()
        return {"status": 200, "message": "Aseguradora eliminada"}
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return False
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ActualizarAseguradora(IDAseguradora, NombreAseguradora, Direccion, NumContacto):
    """
    Actualiza una aseguradora registrada en la base de datos

    Args:
        IDAseguradora (int): ID de la aseguradora
        NombreAseguradora (str): Nombre de la aseguradora
        Direccion (str): Dirección de la aseguradora
        NumContacto (str): Número de contacto de la aseguradora

    Returns:
        bool: True si se actualizó correctamente, False si no
    """

    connection = DBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE Aseguradoras SET NombreAseguradora = %s, Direccion = %s, NumContacto = %s WHERE IDAseguradora = %s", (NombreAseguradora, Direccion, NumContacto, IDAseguradora))
        connection.commit()
        return {"status": 200, "message": "Aseguradora actualizada"}
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return False
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")


#------------------------Polizas------------------------#


def RegistrarPoliza(IDAseguradora, Vigencia_de_Poliza, TipoDePoliza, SumaAsegurada, FechaInicio, Prima):
        """
        Registra una poliza en la base de datos

        Args:
            IDAseguradora (int): ID de la aseguradora
            Vigencia_de_Poliza (str): Vigencia de la poliza
            TipoDePoliza (str): Tipo de poliza
            SumaAsegurada (int): Suma asegurada
            FechaInicio (str): Fecha de inicio de la poliza
            Prima (int): Prima

        Returns:
            bool: True si se registró correctamente, False si no
        """
    
        connection = DBConnection()
        cursor = connection.cursor()
    
        try:
            cursor.execute("INSERT INTO Polizas (IDAseguradora, Vigencia_de_Poliza, TipoDePoliza, SumaAsegurada, FechaInicio, Prima) VALUES (%s, %s, %s, %s, %s, %s)", (IDAseguradora, Vigencia_de_Poliza, TipoDePoliza, SumaAsegurada, FechaInicio, Prima))
            connection.commit()
            return {"status": 200, "message": "Poliza registrada"}
        
        except mysql.connector.Error as err:
            print("Error de conexión: {}".format(err))
            return False
        
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexión cerrada")

def ConsultarPoliza(IDPoliza):
    """
    Consulta una poliza registrada en la base de datos

    Args:
        IDPoliza (int): ID de la poliza

    Returns:
        Poliza (dict): Poliza
    """

    connection = DBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM Polizas WHERE IDPoliza = %s", (IDPoliza,))
        result = cursor.fetchall()
        
        if len(result) > 0:
            # Convertir el resultado a un diccionario
            poliza = []
            for i in result:
                poliza.append({
                    'IDPoliza': i[0],
                    'IDAseguradora': i[1],
                    'Vigencia_de_Poliza': i[2],
                    'TipoDePoliza': i[3],
                    'SumaAsegurada': i[4],
                    'FechaInicio': i[5],
                    'Prima': i[6]
                })
            return {"status": 200, "result": poliza}
        else:
            return None
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return None
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarPolizas():
    """
    Consulta las polizas registradas en la base de datos

    Returns:
        Polizas (dict): Lista de polizas
    """

    connection = DBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM Polizas")
        result = cursor.fetchall()
        
        if len(result) > 0:
            # Convertir el resultado a un diccionario
            polizas = []
            for i in result:
                polizas.append({
                    'IDPoliza': i[0],
                    'IDAseguradora': i[1],
                    'Vigencia_de_Poliza': i[2],
                    'TipoDePoliza': i[3],
                    'SumaAsegurada': i[4],
                    'FechaInicio': i[5],
                    'Prima': i[6]
                })
            return {"status": 200, "result": polizas}
        else:
            return None
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return None
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarPolizasAseguradora(IDAseguradora):
    """
    Consulta las polizas registradas en la base de datos

    Args:
        IDAseguradora (int): ID de la aseguradora

    Returns:
        Polizas (dict): Lista de polizas
    """

    connection = DBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM Polizas WHERE IDAseguradora = %s", (IDAseguradora,))
        result = cursor.fetchall()
        
        if len(result) > 0:
            # Convertir el resultado a un diccionario
            polizas = []
            for i in result:
                polizas.append({
                    'IDPoliza': i[0],
                    'IDAseguradora': i[1],
                    'Vigencia_de_Poliza': i[2],
                    'TipoDePoliza': i[3],
                    'SumaAsegurada': i[4],
                    'FechaInicio': i[5],
                    'Prima': i[6]
                })
            return {"status": 200, "result": polizas}
        else:
            return None
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return None
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarPolizasPorTipo(TipoDePoliza):
    """
    Consulta las polizas registradas en la base de datos

    Args:
        TipoDePoliza (str): Tipo de poliza

    Returns:
        Polizas (dict): Lista de polizas
    """

    connection = DBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM Polizas WHERE TipoDePoliza = %s", (TipoDePoliza,))
        result = cursor.fetchall()
        
        if len(result) > 0:
            # Convertir el resultado a un diccionario
            polizas = []
            for i in result:
                polizas.append({
                    'IDPoliza': i[0],
                    'IDAseguradora': i[1],
                    'Vigencia_de_Poliza': i[2],
                    'TipoDePoliza': i[3],
                    'SumaAsegurada': i[4],
                    'FechaInicio': i[5],
                    'Prima': i[6]
                })
            return {"status": 200, "result": polizas}
        else:
            return None
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return None
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ActualizarPoliza(IDPoliza, IDAseguradora, Vigencia_de_Poliza, TipoDePoliza, SumaAsegurada, FechaInicio, Prima):
    """
    Actualiza una poliza registrada en la base de datos

    Args:
        IDPoliza (int): ID de la poliza
        IDAseguradora (int): ID de la aseguradora
        Vigencia_de_Poliza (str): Vigencia de la poliza
        TipoDePoliza (str): Tipo de poliza
        SumaAsegurada (int): Suma asegurada
        FechaInicio (str): Fecha de inicio de la poliza
        Prima (int): Prima

    Returns:
        bool: True si se actualizó correctamente, False si no
    """

    connection = DBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE Polizas SET IDAseguradora = %s, Vigencia_de_Poliza = %s, TipoDePoliza = %s, SumaAsegurada = %s, FechaInicio = %s, Prima = %s WHERE IDPoliza = %s", (IDAseguradora, Vigencia_de_Poliza, TipoDePoliza, SumaAsegurada, FechaInicio, Prima, IDPoliza))
        connection.commit()
        return {"status": 200, "message": "Poliza actualizada"}
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return False
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def EliminarPoliza(IDPoliza):
    """
    Elimina una poliza registrada en la base de datos

    Args:
        IDPoliza (int): ID de la poliza

    Returns:
        bool: True si se eliminó correctamente, False si no
    """

    connection = DBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM Polizas WHERE IDPoliza = %s", (IDPoliza,))
        connection.commit()
        return {"status": 200, "message": "Poliza eliminada"}
    
    except mysql.connector.Error as err:
        print("Error de conexión: {}".format(err))
        return False
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")