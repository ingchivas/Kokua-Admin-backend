import datetime
import json
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.AseguradorasYPolizas import *
from backend.Facturas import *

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



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
