from bs4 import BeautifulSoup

with open('arquivo04.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

# BUSCANDO OS ELEMENTOS COM O FIND

'''
# Procurando por tags
tag = soup.find('li')
print(tag)
'''
'''
# BUSCANDO UM PEDAÇO DO TEXTO
tag = soup.find(string='plants')
print(tag)
'''

'''
# BUSCANDO PELO ID
tag = soup.find(id='primaryconsumers')
print(tag)
'''

# BUSCAR PELA CLASSE CSS
'''tag = soup.find(attrs={'class':'primaryconsumerlist'})
print(tag)

# Outra opção de busca pelo CSS
tag = soup.find(class_='primaryconsumerlist')
print(tag)
'''


# CRIANDO UMA FUNÇÃO PARA INTERAGIR COM O FIND
def is_secondary_consumers(tag):
	return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'

secondary_consumer = soup.find(is_secondary_consumers)
print(secondary_consumer.li.div.string)

