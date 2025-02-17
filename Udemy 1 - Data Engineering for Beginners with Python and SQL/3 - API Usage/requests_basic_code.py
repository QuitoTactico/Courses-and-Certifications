import requests

url = "https://www.google.com"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# saving it

with open("./request_basic_response.html", "w") as file:
    file.write(response.text)
