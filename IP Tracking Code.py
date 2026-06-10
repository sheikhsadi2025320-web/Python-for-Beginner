import requests

ip_address = input("Enter an IP address: ")
url = f"https://ipinfo.io/{ip_address}/geo"

data = requests.get(url).json()
print(f"Tracking IP address: {ip_address}")
print("-" * 30)
print(f"City: {data.get('city')}")
print(f"Region: {data.get('region')}")
print(f"Country: {data.get('country')}")
print(f"Location: {data.get('loc')}")
print(f"Network ISP: {data.get('org')}")
