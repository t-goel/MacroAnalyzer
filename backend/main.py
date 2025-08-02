from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MacroFactor API is live"}