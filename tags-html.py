# Acessando as tags HTML

from bs4 import BeautifulSoup

# Abrindo o arquivo para leitura
with open('arquivo.html', 'r') as f:
	# Realizando a instancia de BeautifulSoup
	soup = BeautifulSoup(f, 'lxml')

'''
# Mostrando o conteúdo da TAG
tag = soup.title
print(tag)

# Descobrindo o nome da tag que está sendo acessado
print(tag.name)

tag = soup.p
print(tag)
print(tag.name)
'''

# ACESSANDO OS ATRIBUTOS DO HTML

print(soup.p['class'])

# Mostrando os atributos da tag 'p'
print(soup.p.attrs)

# Mostrando os links na tag 'a'
print(soup.a['href'])

 # ACESSANDO O VALOR DO ATRIBUTO COM O GET, ISSO EVITA ERROS CASO A TAG NÃO EXISTA
print(soup.a.get('href'))
