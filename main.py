from fastapi import FastAPI, status
from app.router.wanted_router import router as wanted

app = FastAPI(
    title="Interpol and FBI API",
    description="Data metrics provider for FBI and Interpol wanted",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Wanted",
            "description": "Wanted endpoints",
        },
    ],
)

app.include_router(wanted, prefix="/wanted", tags=["Wanted"])

@app.get("/", status_code=status.HTTP_200_OK)
def heartbeat():
    return "Mecanismo de busca do FBI e Interpol funcionando"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
