import requests

class CurrencyConverter:
    def __init__(self, api_url="https://api.bcb.gov.br/conversao"):
        self.api_url = api_url
        self.rates = {}

    def fetch_exchange_rates(self, base_currency):
        try:
            response = requests.get(self.api_url + base_currency)
            if response.status_code == 200:
                self.rates = response.json().get("rates", {})
                print(f"Taxas de câmbio atualizadas para {base_currency}.")
            else:
                print("Erro ao buscar taxas de câmbio.")
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: {e}")

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            print("Moeda inválida ou não suportada.")
            return None

        converted_amount = amount * self.rates[to_currency] / self.rates[from_currency]
        return converted_amount

    def menu(self):
        print("--- Conversor de Moedas ---")
        base_currency = input("Digite a moeda base (ex: USD, EUR, BRL): ").upper()
        self.fetch_exchange_rates(base_currency)

        if self.rates:
            while True:
                print("\nOpções:")
                print("1. Converter Moeda")
                print("2. Sair")
                choice = input("Escolha uma opção: ")

                if choice == "1":
                    try:
                        from_currency = input("De qual moeda deseja converter? ").upper()
                        to_currency = input("Para qual moeda deseja converter? ").upper()
                        amount = float(input("Digite o valor a ser convertido: "))
                        result = self.convert(amount, from_currency, to_currency)

                        if result is not None:
                            print(f"{amount:.2f} {from_currency} é equivalente a {result:.2f} {to_currency}.")
                    except ValueError:
                        print("Por favor, insira um valor numérico válido.")
                elif choice == "2":
                    print("Encerrando o programa...")
                    break
                else:
                    print("Escolha inválida, tente novamente.")

if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.menu()
