import os
from datetime import datetime
from random import choice, randint, uniform

from faker import Faker

from include.models.item import ItemModel
from include.models.sales import VendaModel

fake = Faker(locale='pt_BR')


def gerar_item() -> ItemModel:
    return ItemModel(
        nome=fake.word().capitalize(),
        quantidade=randint(1, 10),
        preco_unitario=round(uniform(10.0, 500.0), 2),
    )


def gerar_venda(pedido_id: int) -> VendaModel:
    itens = [gerar_item() for _ in range(randint(1, 5))]
    valor_total = sum(item.quantidade * item.preco_unitario for item in itens)

    return VendaModel(
        pedido_id=pedido_id,
        cliente=fake.name(),
        valor_total=round(valor_total, 2),
        data_pedido=fake.date_this_year(),
        canal_venda=choice(['online', 'loja física', 'representante']),
        itens=itens,
    )


def gerar_jsonl(output_dir: str = 'data', qtd: int = 100_000):
    os.makedirs(output_dir, exist_ok=True)

    today = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    output_file = f"{output_dir}/vendas_{today}.jsonl"

    with open(output_file, 'w', encoding='utf-8') as file:
        for i in range(1, qtd + 1):
            try:
                venda = gerar_venda(i)
                json_file = venda.model_dump_json()
                file.write(json_file + '\n')
            except Exception as e:
                print(f'[ERRO] Pedido {i}: {e}')


if __name__ == '__main__':
    gerar_jsonl()
