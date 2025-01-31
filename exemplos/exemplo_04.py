import requests
import _json

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": # Adicionar o tokem do ChatGpt
}

data = {
    "model": "gpt-3.5-turbo"
    "messages": [{"role": "user", "content": "Qual é a capital da França?"}]     
}  

response = requests.post(url, headers=headers, data=_json.dumps(data))

print(response.json()['choices'][0]['message']['content'])
