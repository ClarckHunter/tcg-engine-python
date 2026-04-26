from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.get("/game/state")
def get_state():
    return {
        "turn": "player1",
        "hand": ["A♠", "7♥"]
    }

print("sexo")