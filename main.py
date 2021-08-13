from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"msg": "This is root!"}

@app.get("/hello")
def hello():
   return {"msg": "Hello, World!"}
