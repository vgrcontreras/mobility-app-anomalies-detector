from pydantic import BaseModel


class ItemModel(BaseModel):
    nome: str
    quantidade: int
    preco_unitario: float
