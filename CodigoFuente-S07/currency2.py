import requests

def main():
    base = input("First Currency: ")
    other = input("Second Currency: ")
    res = requests.get("http://data.fixer.io/api/latest",params={"access_key":'bf9f3e2331f18b18649b03e456b38bc2',"base": base, "symbols": other})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()