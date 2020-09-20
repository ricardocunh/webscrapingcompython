# Utilizando Python no Sublime https://medium.com/experiencecode/configurando-o-python3-no-sublime-usando-ubuntu-763b8ccdda52

import requests
from bs4 import BeautifulSoup

'''
with open('arquivo.html', 'r') as f:
	soup_string = BeautifulSoup(f.read(), 'html.parser')
print(soup_string)
'''

'''
# Criando um objeto beautifulSoup com requests, Buscando a url do Google
r = requests.get('https://www.google.com')
# Criando uma instancia de BeautfulSoup
soup = BeautifulSoup(r.text, 'lxml')
print(soup)
'''


# Criando o arquivo em html5
with open('arquivo.html', 'r') as f:
	soup_string = BeautifulSoup(f.read(), 'html5lib')
print(soup_string)
