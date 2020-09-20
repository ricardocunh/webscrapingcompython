import requests

# CAPTURANDO COOKIES DE UM SITE

url = 'https://www.submarino.com.br/'

r = requests.get(url)

# CAPTURANDO O COOKIE
cookie = r.cookies.get_dict()

# fazendo a requisição direcionado a busca Notebook
busca = 'notebook'
url = 'https://www.submarino.com.br/busca?conteudo={0}'.format(busca)

r = requests.get(url, cookies=cookie)

# SALVANDO O ARQUIVO
with open('submarino.html', 'wb') as f:
	f.write(r.content)
