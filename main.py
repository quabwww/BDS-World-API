from fastapi import FastAPI, HTTPException, Response, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from Funciones.funciones import function
import uvicorn
import requests
import json

app = FastAPI()

app.mount("/funcion/images/",
          StaticFiles(directory="Funciones-IMG-ES"),
          name="/funcion/images/")


@app.get("/")
def on_route():
    contenido = json.dumps({"API": "BDS World",
                            "Discord Soporte": "https://discord.gg/dru9uRYKqq"}, indent=4)
    return Response(content=contenido, media_type="application/json")

function_info = function

function_responses = {
    func.lower(): response
    for func, response in function_info.items()
}


def buscar_palabra(parte):
    parte = parte.lower()
    return [
        func.lower() for func in function_responses if func.startswith(parte)
    ]


@app.get("/funcion/{command}")
def funciones(command: str):
    busqueda = buscar_palabra(command.strip())

    if not busqueda:
        raise HTTPException(
            status_code=404, detail="No se encontró la función")

    function_name = busqueda[0]
    response = function_responses.get(function_name)
    if response:
        return JSONResponse(content=response, status_code=200)

    raise HTTPException(status_code=404, detail="No se encontró la función")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
