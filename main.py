from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola, Luis!"}


@app.get("/")
async def root():
    return {"message": "Hola, Luis!"}
