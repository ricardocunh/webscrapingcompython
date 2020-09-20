from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')


'''
# FIND ALL RETORNA UMA LISTA COM TODAS AS OCORRÊNCIAS DE UL
tag_list = soup.find_all('ul')
print(tag_list)

'''

'''
# LIMITANDO O NÚMERO DE OCORRÊNCIA QUE SERÁ RETORNADO
tag_list = soup.find_all('ul', limit=2)
print(tag_list)
'''

'''
# RETORNAR TODOS OS TEXTOS EM FORMATO DE LIST
tag_list = soup.find_all(string=True)
print(tag_list)
'''

'''
# PESQUISAR UMA LISTA DE TEXTO CONTIDAS NO ARQUIVO
tag_list = soup.find_all(string=['rabbit', 'bear'])
print(tag_list)
'''

'''
# BUSCAR TODAS AS OCORRÊNCIA QUE TENHAM OUTRA CLASS
tag_list = soup.find_all(class_=['producerlist', 'primaryconsumerlist'])
print(tag_list)
'''

'''
# BUSCANDO DENTRO DE UMA TAG ESPECIFICA
tag_list = soup.ul.find_all('div')
print(tag_list)
'''

# PASSANDO MAIS DE UM ARGUMENTO
tag_list = soup.find_all('div', class_='name')
print(tag_list)