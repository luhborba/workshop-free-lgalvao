import pytest
from datetime import datetime
from src.contrato import Vendas
from pydantic import ValidationError

# Teste com dados válidos
def test_dados_validos():
    dados_validos = {
        "email": "comprador@gmail.com",
        "data": datetime.now(),
        "id_compra": 2,
        "valor_compra": 100.5,
        "vendedor": "Luciano",
    }

    venda = Vendas(**dados_validos)
    assert venda.email == dados_validos["email"]
    assert venda.data == dados_validos["data"]
    assert venda.id_compra == dados_validos["id_compra"]
    assert venda.valor_compra == dados_validos["valor_compra"]
    assert venda.vendedor == dados_validos["vendedor"]