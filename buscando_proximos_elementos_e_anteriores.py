from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')


# OS FINDS ABAIXO NÃO RESPEITÃO AS HIERARQUIAS, ELES APENAS SEGUEM PARA O PRÓXIMO ELEMENTO
'''
FIND_NEXT
FIND_ALL_NEXT
FIND_PREVIOUS
FIND_ALL_PREVIOUS
'''
'''
producers = soup.find(id='producers')
tag_next = producers.find_next()
print(tag_next)
'''

'''
producers = soup.find(id='producers')
tag_next = producers.find_all_next()
print(tag_next)
'''

'''
# RETORNANDO O PRIMEIRO ELEMENTO ANTERIOR DE UM DETERMINADO ELEMENTO
producers = soup.find(id='quaternaryconsumers')
tag_previous = producers.find_previous()
print(tag_previous)
'''


# RETORNANDO TODOS OS ELEMENTOS ANTERIORES 
producers = soup.find(id='quaternaryconsumers')
tag_previous = producers.find_all_previous()
print(tag_previous)