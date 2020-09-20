from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag 

with open('arquivo02.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')


# Retornando o primeiro elemento encontrado
print(soup.title)
print(soup.head.title)
print(soup.a)
print(soup.a.img)


# Retornando todos os dados contidos em PAI
print(soup.table.contents)

# Verificando o tipo de dado
print(type(soup.contents))

# Retorna o tamanho da lista
print(len(soup.contents))

# Retornando o segundo item da lista
print(soup.table.contents[1])

# Retornando apenas o spam
print(soup.table.contents[1].span)

# Retornando apenas o spam sem as tags
print(soup.table.contents[1].span.string)

# Interando com a lista um a um
for child in soup.table.contents:
	print(child)

# Acessando os filhos de seus filhos e não apenas o pai
print(len(list(soup.descendants)))



# Realizando a impressão de todo o conteúdo
for tag in soup.descendants:
	if isinstance(tag, NavigableString):
		print(tag)
	else:
		print(tag.name)


# Realizando a impressão apenas das tags
for tag in soup.descendants:
	if isinstance(tag, Tag):
		print(tag)
	else:
		print(tag.name)


# DIFERENÇAS ENTRE STRING E STRIPPED_STRINGS

# -> String é um descendente, com string você vai conseguir interagir todas as strings descendentes

# ->Stripped_Strings - você só pegará o necessário removendo os espaços extras


# EXEMPLO COM STRING
for string in soup.aside.strings:
	#gerando a representações (repr) que o python vai ler
	print(repr(string))

# EXEMPLO COM STRIPPED_STRINGS

for string in soup.aside.stripped_strings:
	print(repr(string))

