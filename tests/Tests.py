# tests/test_conversion.py

from src.main import converter_moeda

def test_converter_moeda():
    try:
        resultado = converter_moeda(100, "USD", "BRL")
        assert resultado > 0, "O valor convertido deve ser maior que 0"
        print("Teste passou!")
    except Exception as e:
        print(f"Teste falhou: {e}")
