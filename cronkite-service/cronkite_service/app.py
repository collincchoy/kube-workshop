from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def healthz():
    return {"status": "up"}
