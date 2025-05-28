import requests

def get_crypto_price(symbol="BTC"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data[symbol.lower()]["usd"]
        print(f"Harga {symbol.upper()} saat ini: ${price}")
    else:
        print("Gagal mengambil data harga.")

if __name__ == "__main__":
    symbol = input("Masukkan simbol crypto (contoh: btc, eth, doge): ").strip()
    get_crypto_price(symbol)
