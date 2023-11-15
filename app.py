import datetime
import json
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.AseguradorasYPolizas import *
from backend.Facturas import *
from backend.Ordenes import *

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
    return {"message": "Bienvenido a la API de Kokua"}

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
