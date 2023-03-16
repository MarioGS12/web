import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?symbols=USD&access_key=bf9f3e2331f18b18649b03e456b38bc2")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"]["USD"]
    print(f"1 EUR is equal to {rate} USD")

if __name__ == "__main__":
    main()
