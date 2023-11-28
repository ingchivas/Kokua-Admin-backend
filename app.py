import datetime
import json
import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.AseguradorasYPolizas import *
from backend.Facturas import *
from backend.Ordenes import *
from backend.Usuarios import *
from backend.Citas import *
from backend.Pacientes import *


app = FastAPI()

# Configurar el middleware de CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return FileResponse("frontend/index.html")

#______________________________________________________Aseguradoras_________________________________________________________________

@app.get("/aseguradoras/Todas")
async def getAseguradoras():
    return ConsultarAseguradoras()

@app.get("/aseguradoras/Aseguradora/{id}")
async def getAseguradora(id: int):
    return ConsultarAseguradora(id)

@app.post("/aseguradoras/RegistrarAseguradora")
async def postAseguradora(aseguradora: dict):
    try:
        NombreAseguradora = aseguradora["NombreAseguradora"]
        Direccion = aseguradora["Direccion"]
        NumContacto = aseguradora["NumContacto"]
        return RegistrarAseguradora(NombreAseguradora, Direccion, NumContacto)
    except:
        return {"status": 400, "message": "Error al registrar la aseguradora"}
    
@app.post("/aseguradoras/ActualizarAseguradora")
async def postAseguradora(aseguradora: dict):
    try:
        IDAseguradora = aseguradora["IDAseguradora"]
        NombreAseguradora = aseguradora["NombreAseguradora"]
        Direccion = aseguradora["Direccion"]
        NumContacto = aseguradora["NumContacto"]
        return ActualizarAseguradora(IDAseguradora, NombreAseguradora, Direccion, NumContacto)
    except:
        return {"status": 400, "message": "Error al actualizar la aseguradora"}

@app.delete("/aseguradoras/EliminarAseguradora/{id}")
async def deleteAseguradora(id: int):
    return EliminarAseguradora(id)


#______________________________________________________Polizas_________________________________________________________________

@app.get("/polizas/Todas")
async def getPolizas():
    return ConsultarPolizas()

@app.get("/polizas/Poliza/{id}")
async def getPoliza(id: int):
    return ConsultarPoliza(id)

@app.post("/polizas/RegistrarPoliza")
async def postPoliza(poliza: dict):
    try:
        IDAseguradora = poliza["IDAseguradora"]
        Vigencia_de_Poliza = poliza["Vigencia_de_Poliza"]
        TipoDePoliza = poliza["TipoDePoliza"]
        SumaAsegurada = poliza["SumaAsegurada"]
        FechaInicio = poliza["FechaInicio"]
        Prima = poliza["Prima"]
        return RegistrarPoliza(IDAseguradora, Vigencia_de_Poliza, TipoDePoliza, SumaAsegurada, FechaInicio, Prima)
    except:
        return {"status": 400, "message": "Error al registrar la poliza"}
    
@app.post("/polizas/ActualizarPoliza")
async def postPoliza(poliza: dict):
    try:
        IDPoliza = poliza["IDPoliza"]
        IDAseguradora = poliza["IDAseguradora"]
        Vigencia_de_Poliza = poliza["Vigencia_de_Poliza"]
        TipoDePoliza = poliza["TipoDePoliza"]
        SumaAsegurada = poliza["SumaAsegurada"]
        FechaInicio = poliza["FechaInicio"]
        Prima = poliza["Prima"]
        return ActualizarPoliza(IDPoliza, IDAseguradora, Vigencia_de_Poliza, TipoDePoliza, SumaAsegurada, FechaInicio, Prima)
    except:
        return {"status": 400, "message": "Error al actualizar la poliza"}

@app.delete("/polizas/EliminarPoliza/{id}")
async def deletePoliza(id: int):
    return EliminarPoliza(id)

@app.get("/polizas/PolizasPorAseguradora/{id}")
async def getPolizasPorAseguradora(id: int):
    return ConsultarPolizasAseguradora(id)

@app.get("/polizas/PolizasPorTipo/{tipo}")
async def getPolizasPorTipo(tipo: str):
    return ConsultarPolizasPorTipo(tipo)

#______________________________________________________Facturas_________________________________________________________________

@app.get("/facturas/Todas")
async def getFacturas():
    return ConsultarFacturas()

@app.get("/facturas/Factura/{id}")
async def getFactura(id: int):
    return ConsultarFacturaPorID(id)

@app.get("/facturas/CitaAsociada/{id}")
async def getCitaAsociada(id: int):
    return ConsultarCitaAsociada(id)

@app.post("/facturas/RegistrarFactura")
async def postFactura(factura: dict):
    try:
        IDCita = factura["IDCita"]
        Costo = factura["Costo"]
        return InsertarFactura(IDCita, Costo)
    except:
        return {"status": 400, "message": "Error al registrar la factura"}

@app.put("/facturas/ActualizarFactura")
async def putFactura(factura: dict):
    try:
        IDFactura = factura["IDFactura"]
        NuevoCosto = factura["NuevoCosto"]
        return ActualizarFactura(IDFactura, NuevoCosto)
    except:
        return {"status": 400, "message": "Error al actualizar la factura"}

@app.delete("/facturas/EliminarFactura/{id}")
async def deleteFactura(id: int):
    return EliminarFactura(id)

@app.get("/facturas/FacturasOrdenadasPorCosto")
async def getFacturasOrdenadasPorCosto():
    return ConsultarFacturasOrdenadasPorCosto()

#______________________________________________________Ordenes_________________________________________________________________

@app.get("/ordenes/Todas")
async def getOrdenes():
    return ConsultarTodasLasOrdenes()

@app.get("/ordenes/Orden/{id}")
async def getOrden(id: int):
    return ConsultarOrdenPorID(id)

@app.get("/ordenes/OrdenesPorPaciente/{id_paciente}")
async def getOrdenesPorPaciente(id_paciente: int):
    return ConsultarOrdenesPorPaciente(id_paciente)

@app.get("/ordenes/OrdenesPorMedicina/{id_medicina}")
async def getOrdenesPorMedicina(id_medicina: int):
    return ConsultarOrdenesPorMedicina(id_medicina)

@app.get("/ordenes/OrdenesPorProveedor/{id_proveedor}")
async def getOrdenesPorProveedor(id_proveedor: int):
    return ConsultarOrdenesPorProveedor(id_proveedor)

@app.get("/ordenes/OrdenesPorCosto")
async def getOrdenesPorCosto(mayor_a_menor: bool = True):
    return ConsultarOrdenesPorCosto(mayor_a_menor)

@app.get("/ordenes/OrdenesPorEstatus/{estatus}")
async def getOrdenesPorEstatus(estatus: str):
    return ConsultarOrdenesPorEstatus(estatus)

@app.get("/ordenes/OrdenesPorCantidad")
async def getOrdenesPorCantidad(mayor_a_menor: bool = True):
    return ConsultarOrdenesPorCantidad(mayor_a_menor)

@app.get("/ordenes/OrdenesPorEntregaEsperada/{fecha_entrega}")
async def getOrdenesPorEntregaEsperada(fecha_entrega: str):
    return ConsultarOrdenesPorEntregaEsperada(fecha_entrega)

@app.get("/ordenes/OrdenesPorFechaOrden/{fecha_orden}")
async def getOrdenesPorFechaOrden(fecha_orden: str):
    return ConsultarOrdenesPorFechaOrden(fecha_orden)

@app.get("/ordenes/OrdenesPorFechaEntrega/{fecha_entrega}")
async def getOrdenesPorFechaEntrega(fecha_entrega: str):
    return ConsultarOrdenesPorFechaEntrega(fecha_entrega)

@app.post("/ordenes/ActualizarOrden")
async def putOrden(IDOrden: dict):
    try:
        IDOrden = IDOrden["IDOrden"]
        IDMedicina = IDOrden["IDMedicina"]
        IDProveedor = IDOrden["IDProveedor"]
        Cantidad = IDOrden["Cantidad"]
        Costo = IDOrden["Costo"]
        FechaOrden = IDOrden["FechaOrden"]
        FechaEntrega = IDOrden["FechaEntrega"]
        Estatus = IDOrden["Estatus"]
        return ActualizarOrden(IDOrden, IDMedicina, IDProveedor, Cantidad, Costo, FechaOrden, FechaEntrega, Estatus)
    except:
        return {"status": 400, "message": "Error al actualizar la orden"}
    
@app.post("/ordenes/RegistrarOrden")
async def postOrden(orden: dict):
    try:
        IDMedicina = orden["IDMedicina"]
        IDProveedor = orden["IDProveedor"]
        Cantidad = orden["Cantidad"]
        Costo = orden["Costo"]
        FechaOrden = orden["FechaOrden"]
        FechaEntrega = orden["FechaEntrega"]
        Estatus = orden["Estatus"]
        return InsertarOrden(IDMedicina, IDProveedor, Cantidad, Costo, FechaOrden, FechaEntrega, Estatus)
    except:
        return {"status": 400, "message": "Error al registrar la orden"}

@app.delete("/ordenes/EliminarOrden/{IDOrden}")
async def deleteOrden(IDOrden: int):
    return EliminarOrden(IDOrden)


#______________________________________________________Usuarios_________________________________________________________________

@app.get("/usuarios/Todos")
async def getUsuarios():
    return ConsultarUsuarios()

@app.get("/usuarios/Usuario/{id}")
async def getUsuario(id: int):
    return ConsultarUsuario(id)

@app.post("/usuarios/Login")
async def login(usuario: dict):
    try:
        username = usuario["username"]
        password = usuario["password"]
        return Login(username, password)
    except:
        return {"status": 400, "message": "Error al iniciar sesión"}

@app.post("/usuarios/CrearUsuarioPorTipo")
async def postUsuario(usuario: dict):

    try:
        tipo_acceso = usuario["tipo_acceso"]
        username = usuario["username"]
        password = usuario["password"]
        return CrearUsuarioPorTipo(username, password, tipo_acceso)
    except:
        pass

    try:
        username = usuario["username"]
        password = usuario["password"]
        return CrearUsuarioPorTipo(username, password)
    except:
        return {"status": 400, "message": "Error al crear el usuario"}

@app.post("/usuarios/CrearUsuarioPaciente")
async def postUsuarioPaciente(usuario: dict):
    try:
        username = usuario["username"]
        password = usuario["password"]
        nombre = usuario["nombre"]
        apellido = usuario["apellido"]
        padecimiento = usuario["padecimiento"]
        estatus_paciente = usuario["estatus_paciente"]
        saldo_actual = usuario["saldo_actual"]
        return CrearUsuarioPaciente(username, password, nombre, apellido, padecimiento, estatus_paciente, saldo_actual)

    except:
        return HTTPException(status_code=400, detail="Error al crear el usuario")

@app.post("/usuarios/CrearUsuarioPacienteExistente")
async def postUsuarioPacienteExistente(usuario: dict):
    try:
        IDPaciente = usuario["IDPaciente"]
        username = usuario["username"]
        password = usuario["password"]
        return CrearUsuarioPacienteExistente(IDPaciente, username, password)
    except:
        return HTTPException(status_code=400, detail="Error al crear el usuario")
    
@app.post("/usuarios/CrearUsuarioDoctor")
async def postUsuarioDoctor(usuario: dict):
    try:
        username = usuario["username"]
        password = usuario["password"]
        cedula_profesional = usuario["cedula_profesional"]
        nombre = usuario["nombre"]
        apellido = usuario["apellido"]
        fecha_nacimiento = usuario["fecha_nacimiento"]
        costo_cita = usuario["costo_cita"]
        especialidad = usuario["especialidad"]
        return CrearUsuarioDoctor(username, password, cedula_profesional, nombre, apellido, fecha_nacimiento, costo_cita, especialidad)
    except:
        return HTTPException(status_code=400, detail="Error al crear el usuario")

@app.post("/usuarios/CrearUsuarioDoctorExistente")
async def postUsuarioDoctorExistente(usuario: dict):
    try:
        IDDoctor = usuario["IDDoctor"]
        username = usuario["username"]
        password = usuario["password"]
        return CrearUsuarioDoctorExistente(IDDoctor, username, password)
    except:
        return HTTPException(status_code=400, detail="Error al crear el usuario")
    
@app.post("/usuarios/CrearUsuarioProovedor")
async def postUsuarioProovedor(usuario: dict):
    try:
        username = usuario["username"]
        password = usuario["password"]
        nombre = usuario["nombre"]
        ubicacion = usuario["ubicacion"]
        num_contacto = usuario["num_contacto"]
        return CrearUsuarioProveedor(username, password, nombre, ubicacion, num_contacto)
    except:
        return HTTPException(status_code=400, detail="Error al crear el usuario")
    
@app.post("/usuarios/CrearUsuarioProovedorExistente")
async def postUsuarioProovedorExistente(usuario: dict):
    try:
        IDProveedor = usuario["IDProveedor"]
        username = usuario["username"]
        password = usuario["password"]
        return CrearUsuarioProveedorExistente(IDProveedor, username, password)
    except:
        return HTTPException(status_code=400, detail="Error al crear el usuario")
    
@app.post("/usuarios/CrearUsuarioAdministrador")
async def postUsuarioAdministrador(usuario: dict):
    try:
        username = usuario["username"]
        password = usuario["password"]
        return CrearUsuarioAdministrador(username, password)
    except:
        return HTTPException(status_code=400, detail="Error al crear el usuario")
    
@app.delete("/usuarios/EliminarUsuario/{id}")
async def deleteUsuario(id: int):
    return EliminarUsuario(id)


# ____________________________________________________________Citas________________________________________________________________________

@app.get("/citas/Todas")
async def getCitas():
    return ConsultarCitas()

@app.get("/citas/Cita/{id}")
async def getCita(id: int):
    return ConsultarCita(id)

@app.get("/citas/CitasPorPaciente/{id_paciente}")
async def getCitasPorPaciente(id_paciente: int):
    return ConsultarCitasPaciente(id_paciente)

@app.get("/citas/CitasPorDoctor/{id_doctor}")
async def getCitasPorDoctor(id_doctor: int):
    return ConsultarCitasDoctor(id_doctor)

@app.post("/citas/RegistrarCita")
async def postCita(cita: dict):
    try:
        IDPaciente = cita["IDPaciente"]
        IDDoctor = cita["IDDoctor"]
        TipoCita = cita["TipoCita"]
        EstatusCita = cita["EstatusCita"]
        Fecha = cita["Fecha"]
        return AgendarCita(IDPaciente, IDDoctor, TipoCita, Fecha, EstatusCita)
    except:
        return HTTPException(status_code=400, detail="Error al registrar la cita")
    
@app.post("/citas/ActualizarCita")
async def putCita(cita: dict):
    try:
        IDCita = cita["IDCita"]
        IDPaciente = cita["IDPaciente"]
        IDDoctor = cita["IDDoctor"]
        TipoCita = cita["TipoCita"]
        EstatusCita = cita["EstatusCita"]
        Fecha = cita["Fecha"]
        return ActualizarCita(IDCita, IDPaciente, IDDoctor, TipoCita, EstatusCita, Fecha)
    except:
        return HTTPException(status_code=400, detail="Error al actualizar la cita")
    
@app.post("/citas/ActualizarEstatusCita")
async def putCita(cita: dict):
    try:
        IDCita = cita["IDCita"]
        EstatusCita = cita["EstatusCita"]
        return ActualizarEstatusCita(IDCita, EstatusCita)
    except:
        return HTTPException(status_code=400, detail="Error al actualizar la cita")

@app.delete("/citas/EliminarCita/{id}")
async def deleteCita(id: int):
    return EliminarCita(id)

# ____________________________________________________________Pacientes________________________________________________________________________

@app.get("/pacientes/Todos")
async def getPacientes():
    return ConsultarPacientes()

@app.get("/pacientes/Paciente/{id}")
async def getPaciente(id: int):
    return ConsultarPacientePorID(id)

@app.post("/pacientes/AgregarPaciente")
async def postPaciente(paciente: dict):
    try:
        Nombre = paciente["Nombre"]
        Apellido = paciente["Apellido"]
        Padecimento = paciente["Padecimento"]
        EstatusPaciente = paciente["EstatusPaciente"]
        SaldoActual = paciente["SaldoActual"]
        Username = paciente["Username"]
        Password = paciente["Password"]
        TipoAcceso = paciente["TipoAcceso"]
        
        return AgregarPaciente({
            "Nombre": Nombre,
            "Apellido": Apellido,
            "Padecimento": Padecimento,
            "EstatusPaciente": EstatusPaciente,
            "SaldoActual": SaldoActual,
            "Username": Username,
            "Password": Password
        })
    except:
        return {"status": 400, "message": "Error al agregar el paciente"}
    
@app.post("/pacientes/AgregarPacienteSinUsuario")
async def postPaciente(paciente: dict):
    try:
        Nombre = paciente["Nombre"]
        Apellido = paciente["Apellido"]
        Padecimento = paciente["Padecimento"]
        EstatusPaciente = paciente["EstatusPaciente"]
        SaldoActual = paciente["SaldoActual"]
        
        return AgregarPacienteSinUsuario({
            "Nombre": Nombre,
            "Apellido": Apellido,
            "Padecimento": Padecimento,
            "EstatusPaciente": EstatusPaciente,
            "SaldoActual": SaldoActual
        })
    except:
        return {"status": 400, "message": "Error al agregar el paciente"}

@app.post("/pacientes/ActualizarPaciente/{id}")
async def putPaciente(id: int, paciente: dict):
    try:
        Nombre = paciente["Nombre"]
        Apellido = paciente["Apellido"]
        Padecimento = paciente["Padecimento"]
        EstatusPaciente = paciente["EstatusPaciente"]
        SaldoActual = paciente["SaldoActual"]
        Username = paciente["Username"]
        Password = paciente["Password"]
        TipoAcceso = paciente["TipoAcceso"]
        
        return ActualizarPaciente(id, {
            "Nombre": Nombre,
            "Apellido": Apellido,
            "Padecimento": Padecimento,
            "EstatusPaciente": EstatusPaciente,
            "SaldoActual": SaldoActual,
            "Username": Username,
            "Password": Password,
            "TipoAcceso": TipoAcceso
        })
    except:
        return {"status": 400, "message": "Error al actualizar el paciente"}

@app.delete("/pacientes/EliminarPaciente/{id}")
async def deletePaciente(id: int):
    return EliminarPaciente(id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
