from forex_python.converter import CurrencyRates

def get_exchange_rate(from_currency, to_currency):
    currency_rates = CurrencyRates()
    exchange_rate = currency_rates.get_rate(from_currency, to_currency)
    return exchange_rate

def convert_currency(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    print("Welcome to the Currency Converter!")

    while True:
        try:
            from_currency = input("Enter the source currency code (e.g., USD): ").upper()
            to_currency = input("Enter the target currency code (e.g., EUR): ").upper()
            amount = float(input("Enter the amount to convert: "))
            
            exchange_rate = get_exchange_rate(from_currency, to_currency)
            converted_amount = convert_currency(amount, exchange_rate)

            print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            print(f"Exchange Rate: 1 {from_currency} = {exchange_rate:.4f} {to_currency}")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
        except KeyError:
            print("Invalid currency code. Please enter a valid currency code.")
        except Exception as e:
            print(f"An error occurred: {e}")

        try_again = input("Do you want to convert another amount? (yes/no): ").lower()
        if try_again != 'yes':
            break

if __name__ == "__main__":
    main()
