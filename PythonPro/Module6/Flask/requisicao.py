from requests import post, get

resp = post("http://localhost:5000/api", json={"key": "value"})

print(resp.ok)

print(resp.text)

print(get("http://localhost:5000/api").text)