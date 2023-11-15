from DBConnect import DBConnection
import mysql.connector


#______________________________________________________Usuarios_________________________________________________________________

def Login(username, password):
    """ 
    Consulta un usuario específico por su username y password

    Args:
        username (str): Nombre de usuario
        password (str): Contraseña del usuario

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE Username = %s AND Password = %s", (username, password))
        result = cursor.fetchone()

        if result:
            return {"status": 200, "result": True}
        else:
            return {"status": 404, "result": False}

    except mysql.connector.Error as err:
        print("Error al consultar el usuario: {}".format(err))
        return {"status": 500, "message": "Error al consultar el usuario"}

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarUsuarios():
    """ 
    Consulta todos los usuarios registrados en la base de datos

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Usuarios")
        result = cursor.fetchall()

        if result:
            usuarios = []
            for usuario in result:
                usuarios.append({
                    "IDUsuario": usuario[0],
                    "Username": usuario[1],
                    "Password": usuario[2],
                    "TipoAcceso": usuario[3]
                })
            return {"status": 200, "result": usuarios}
        else:
            return {"status": 404, "message": "Usuarios no encontrados"}
    
    except mysql.connector.Error as err:
        print("Error al consultar los usuarios: {}".format(err))
        return {"status": 500, "message": "Error al consultar los usuarios"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarUsuario(id_usuario):
    """ 
    Consulta un usuario específico por su ID

    Args:
        id_usuario (int): ID del usuario a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE IDUsuario = %s", (id_usuario,))
        result = cursor.fetchone()

        if result:
            usuario = []
            usuario.append({
                "IDUsuario": result[0],
                "Username": result[1],
                "Password": result[2],
                "TipoAcceso": result[3]
            })
            return {"status": 200, "result": usuario}
        else:
            return {"status": 404, "message": "Usuario no encontrado"}

    except mysql.connector.Error as err:
        print("Error al consultar el usuario: {}".format(err))
        return {"status": 500, "message": "Error al consultar el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def CrearUsuarioPorTipo(username, password, tipo_acceso=1):
    """ 
    Crea un nuevo usuario en la base de datos

    Args:
        tipo_usuario (str): Tipo de usuario a crear
        username (str): Nombre de usuario
        password (str): Contraseña del usuario
        tipo_acceso (str): Tipo de acceso del usuario

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Usuarios (Username, Password, TipoAcceso) VALUES (%s, %s, %s)", (username, password, tipo_acceso))
        connection.commit()

        return {"status": 201, "message": "Usuario creado correctamente"}
    
    except mysql.connector.Error as err:
        print("Error al crear el usuario: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al crear el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def CrearUsuarioPaciente(username, password, nombre, apellido, padecimiento, estatus_paciente, saldo_actual, tipo_acceso="Paciente"):
    """ 
    Crea un nuevo usuario de tipo paciente en la base de datos

    Args:
        username (str): Nombre de usuario
        password (str): Contraseña del usuario
        tipo_acceso (str): Tipo de acceso del usuario
        nombre (str): Nombre del paciente
        apellido (str): Apellido del paciente
        padecimiento (str): Padecimiento del paciente
        estatus_paciente (str): Estatus del paciente
        saldo_actual (float): Saldo actual del paciente

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Usuarios (Username, Password, TipoAcceso) VALUES (%s, %s, %s)", (username, password, tipo_acceso))
        connection.commit()

        id_usuario = cursor.lastrowid
        cursor.execute("INSERT INTO Pacientes (IDUsuario, Nombre, Apellido, Padecimento, EstatusPaciente, SaldoActual) VALUES (%s, %s, %s, %s, %s, %s)", (id_usuario, nombre, apellido, padecimiento, estatus_paciente, saldo_actual))
        connection.commit()

        return {"status": 201, "message": "Usuario creado correctamente", "id_usuario": id_usuario}
    
    except mysql.connector.Error as err:
        print("Error al crear el usuario: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al crear el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def CrearUsuarioPacienteExistente(IDPaciente, username, password, tipo_acceso="Paciente"):
    """ 
    Crea un nuevo usuario de tipo paciente en la base de datos

    Args:
        IDPaciente (int): ID del paciente a asociar
        username (str): Nombre de usuario
        password (str): Contraseña del usuario
        tipo_acceso (str): Tipo de acceso del usuario

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Usuarios (Username, Password, TipoAcceso) VALUES (%s, %s, %s)", (username, password, tipo_acceso))
        connection.commit()

        id_usuario = cursor.lastrowid
        cursor.execute("UPDATE Pacientes SET IDUsuario = %s WHERE IDPaciente = %s", (id_usuario, IDPaciente))
        connection.commit()

        return {"status": 201, "message": "Usuario creado correctamente", "id_usuario": id_usuario}
    
    except mysql.connector.Error as err:
        print("Error al crear el usuario: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al crear el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarUsuarioPorPaciente(id_paciente):
    """ 
    Consulta un usuario específico por su ID de paciente

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
        cursor.execute("SELECT * FROM Usuarios INNER JOIN Pacientes ON Usuarios.IDUsuario = Pacientes.IDUsuario WHERE Pacientes.IDPaciente = %s", (id_paciente,))
        result = cursor.fetchone()

        if result:
            usuario = []
            usuario.append({
                "IDUsuario": result[0],
                "Username": result[1],
                "Password": result[2],
                "TipoAcceso": result[3]
            })
            return {"status": 200, "result": usuario}
        else:
            return {"status": 404, "message": "Usuario no encontrado"}

    except mysql.connector.Error as err:
        print("Error al consultar el usuario: {}".format(err))
        return {"status": 500, "message": "Error al consultar el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def CrearUsuarioDoctor(username, password, cedula_profesional, nombre, apellido, fecha_nacimiento, costo_cita, especialidad, tipo_acceso="Medico"):
    """ 
    Crea un nuevo usuario de tipo doctor en la base de datos

    Args:
        username (str): Nombre de usuario
        password (str): Contraseña del usuario
        tipo_acceso (str): Tipo de acceso del usuario
        cedula_profesional (int): Cédula profesional del doctor
        nombre (str): Nombre del doctor
        apellido (str): Apellido del doctor
        fecha_nacimiento (date): Fecha de nacimiento del doctor
        costo_cita (float): Costo de la cita del doctor
        especialidad (str): Especialidad del doctor

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Usuarios (Username, Password, TipoAcceso) VALUES (%s, %s, %s)", (username, password, tipo_acceso))
        connection.commit()

        id_usuario = cursor.lastrowid
        cursor.execute("INSERT INTO Doctores (IDUsuario, CedulaProfesional, Nombre, Apellido, FechaNacimiento, CostoCita, Especialidad) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id_usuario, cedula_profesional, nombre, apellido, fecha_nacimiento, costo_cita, especialidad))
        connection.commit()

        return {"status": 201, "message": "Usuario creado correctamente", "id_usuario": id_usuario}
    
    except mysql.connector.Error as err:
        print("Error al crear el usuario: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al crear el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def CrearUsuarioDoctorExistente(IDDoctor, username, password, tipo_acceso="Medico"):
    """ 
    Crea un nuevo usuario de tipo doctor en la base de datos

    Args:
        IDDoctor (int): ID del doctor a asociar
        username (str): Nombre de usuario
        password (str): Contraseña del usuario
        tipo_acceso (str): Tipo de acceso del usuario

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Usuarios (Username, Password, TipoAcceso) VALUES (%s, %s, %s)", (username, password, tipo_acceso))
        connection.commit()

        id_usuario = cursor.lastrowid
        cursor.execute("UPDATE Doctores SET IDUsuario = %s WHERE IDDoctor = %s", (id_usuario, IDDoctor))
        connection.commit()

        return {"status": 201, "message": "Usuario creado correctamente", "id_usuario": id_usuario}
    
    except mysql.connector.Error as err:
        print("Error al crear el usuario: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al crear el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ConsultarUsuarioPorDoctor(id_doctor):
    """ 
    Consulta un usuario específico por su ID de doctor

    Args:
        id_doctor (int): ID del doctor a consultar

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Usuarios INNER JOIN Doctores ON Usuarios.IDUsuario = Doctores.IDUsuario WHERE Doctores.IDDoctor = %s", (id_doctor,))
        result = cursor.fetchone()

        if result:
            usuario = []
            usuario.append({
                "IDUsuario": result[0],
                "Username": result[1],
                "Password": result[2],
                "TipoAcceso": result[3]
            })
            return {"status": 200, "result": usuario}
        else:
            return {"status": 404, "message": "Usuario no encontrado"}

    except mysql.connector.Error as err:
        print("Error al consultar el usuario: {}".format(err))
        return {"status": 500, "message": "Error al consultar el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def CrearUsuarioAdministrador(username, password, tipo_acceso="Administrador"):
    """ 
    Crea un nuevo usuario de tipo administrador en la base de datos

    Args:
        username (str): Nombre de usuario
        password (str): Contraseña del usuario
        tipo_acceso (str): Tipo de acceso del usuario

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Usuarios (Username, Password, TipoAcceso) VALUES (%s, %s, %s)", (username, password, tipo_acceso))
        connection.commit()

        id_usuario = cursor.lastrowid

        return {"status": 201, "message": "Usuario creado correctamente", "id_usuario": id_usuario}
    
    except mysql.connector.Error as err:
        print("Error al crear el usuario: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al crear el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def CrearUsuarioProveedor(username, password, nombre, ubicacion, num_contacto, tipo_acceso="Proveedor"):
    """ 
    Crea un nuevo usuario de tipo proveedor en la base de datos

    Args:
        username (str): Nombre de usuario
        password (str): Contraseña del usuario
        tipo_acceso (str): Tipo de acceso del usuario
        nombre (str): Nombre del proveedor
        ubicacion (str): Ubicación del proveedor
        num_contacto (str): Número de contacto del proveedor

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Usuarios (Username, Password, TipoAcceso) VALUES (%s, %s, %s)", (username, password, tipo_acceso))
        connection.commit()

        id_usuario = cursor.lastrowid
        cursor.execute("INSERT INTO Proveedores (IDUsuario, Nombre, Ubicacion, NumContacto) VALUES (%s, %s, %s, %s)", (id_usuario, nombre, ubicacion, num_contacto))
        connection.commit()

        return {"status": 201, "message": "Usuario creado correctamente", "id_usuario": id_usuario}
    
    except mysql.connector.Error as err:
        print("Error al crear el usuario: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al crear el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def CrearUsuarioProveedorExistente(IDProveedor, username, password, tipo_acceso="Proveedor"):
    """ 
    Crea un nuevo usuario de tipo proveedor en la base de datos

    Args:
        IDProveedor (int): ID del proveedor a asociar
        username (str): Nombre de usuario
        password (str): Contraseña del usuario
        tipo_acceso (str): Tipo de acceso del usuario

    Returns:
        (dict): Diccionario con el resultado de la consulta
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta realizar la consulta
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Usuarios (Username, Password, TipoAcceso) VALUES (%s, %s, %s)", (username, password, tipo_acceso))
        connection.commit()

        id_usuario = cursor.lastrowid
        cursor.execute("UPDATE Proveedores SET IDUsuario = %s WHERE IDProveedor = %s", (id_usuario, IDProveedor))
        connection.commit()

        return {"status": 201, "message": "Usuario creado correctamente", "id_usuario": id_usuario}
    
    except mysql.connector.Error as err:
        print("Error al crear el usuario: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al crear el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def ActualizarUsuario(id_usuario, username, password, tipo_acceso):
    """ 
    Actualiza un usuario específico por su ID

    Args:
        id_usuario (int): ID del usuario a actualizar
        username (str): Nombre de usuario
        password (str): Contraseña del usuario
        tipo_acceso (str): Tipo de acceso del usuario

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta realizar la actualización
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE Usuarios SET Username = %s, Password = %s, TipoAcceso = %s WHERE IDUsuario = %s", (username, password, tipo_acceso, id_usuario))
        connection.commit()
        return {"status": 200, "message": "Usuario actualizado correctamente"}
    
    except mysql.connector.Error as err:
        print("Error al actualizar el usuario: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al actualizar el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def EliminarUsuario(id_usuario):
    """ 
    Elimina un usuario específico por su ID

    Args:
        id_usuario (int): ID del usuario a eliminar

    Returns:
        (dict): Diccionario con el resultado de la operación
    """
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}

    # Intenta realizar la eliminación
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE IDUsuario = %s", (id_usuario,))
        connection.commit()
        return {"status": 200, "message": "Usuario eliminado correctamente"}
    
    except mysql.connector.Error as err:
        print("Error al eliminar el usuario: {}".format(err))
        connection.rollback()
        return {"status": 500, "message": "Error al eliminar el usuario"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

