from fastapi import FastAPI
from mangum import Mangum

app=FastAPI()

handler=Mangum(app)

@app.get("/")
async def root():
	return {"statusCode":200,"body":"hello world"}


@app.get("/users")
async def users():
	return {"statusCode":200,"body":"hello users"}
