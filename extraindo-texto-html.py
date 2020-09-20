# EXTRAÍNDO OS TEXTOS DO HTML

from bs4 import BeautifulSoup

with open('arquivo.html', 'r') as f:
	soup = BeautifulSoup(f, 'html5lib')

'''
# Buscando todos os textos de todas as tags
print(soup.get_text())
'''

# Pegando textos de tags especificas
print(soup.p.get_text())
