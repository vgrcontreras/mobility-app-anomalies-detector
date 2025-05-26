from datetime import date

from include.scripts.gerar_vendas import gerar_item, gerar_venda


def test_gerar_venda():
    venda = gerar_venda(1)

    assert isinstance(venda.pedido_id, int)
    assert isinstance(venda.cliente, str)
    assert isinstance(venda.valor_total, float)
    assert isinstance(venda.data_pedido, date)
    assert isinstance(venda.canal_venda, str)
    # assert isinstance(venda.itens, list[ItemModel])


def test_gerar_item():
    item = gerar_item()

    assert isinstance(item.nome, str)
    assert isinstance(item.quantidade, int)
    assert isinstance(item.preco_unitario, float)
