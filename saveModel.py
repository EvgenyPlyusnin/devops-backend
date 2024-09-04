from pydantic import BaseModel


class SaveModel(BaseModel):
    text: str
