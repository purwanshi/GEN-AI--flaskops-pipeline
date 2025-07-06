import requests

info = requests.get("http://localhost:5000/info")
print("Info endpoint:", info.text)

phone = requests.get("http://localhost:5000/phone")
print("Phone endpoint:", phone.text)
