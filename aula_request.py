import requests


# METODO GET

url = 'https://www.youtube.com/results?'

payload = {'search_query':'web scraping python'}

r = requests.get(url, params=payload)

print(r.text)

# Salvando o arquivo em html

with open('youtube.html', 'wb') as f:
	f.write(r.content)


