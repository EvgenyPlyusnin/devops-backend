from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from saveModel import SaveModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def save(data: SaveModel):
    try:
        file = open('data.txt', 'w')
        file.write(data.text)
        return {"status": "success"}
    except:
        return {"status": "error"}
