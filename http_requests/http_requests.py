import requests
url = "https://icanhazdadjoke.com/"
response = requests.get(url,
    headers={
        "Accept": "text/plain"
    })

print(response)
print(response.ok)
print(response.text)

# Why did the half blind man fall in the well? 
# Because he couldn't see that well!
print("--------------")

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat"})
data = response.json()
print(data["results"][0]["joke"])
# print(data['joke'])