from datetime import date

from pydantic import BaseModel

from include.models.item import ItemModel


class VendaModel(BaseModel):
    pedido_id: int
    cliente: str
    valor_total: float
    data_pedido: date
    canal_venda: str
    itens: list[ItemModel]
