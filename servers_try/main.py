from fastapi import FastAPI as api

# <NAME_OF_API>
app = api()

@app.get('/')
def index():
    return {"message": "WELCOME"}
