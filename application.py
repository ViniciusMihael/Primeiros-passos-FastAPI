from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_languagens():
    return{"sucess":"foi"}