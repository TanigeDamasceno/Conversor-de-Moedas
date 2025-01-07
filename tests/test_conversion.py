# tests/test_conversion.py

import pytest
from src.main import converter_moeda  # Certifique-se de que o caminho está correto

def test_converter_moeda():
    """
    Testa a função converter_moeda para verificar se ela retorna um valor maior que 0
    ao converter 100 USD para BRL.
    """
    valor_origem = 100
    moeda_origem = "USD"
    moeda_destino = "BRL"
    
    try:
        resultado = converter_moeda(valor_origem, moeda_origem, moeda_destino)
        assert resultado > 0, "O valor convertido deve ser maior que 0"
    except Exception as e:
        pytest.fail(f"Erro inesperado: {e}")
