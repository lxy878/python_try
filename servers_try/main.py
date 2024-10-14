from fastapi import FastAPI as api, params

# <NAME_OF_API>
app = api()

@app.get('/')
def index():
    return {"message": "WELCOME"}

@app.post('/create')
def index(payload: dict = params.Body()):
    return {"message": payload}