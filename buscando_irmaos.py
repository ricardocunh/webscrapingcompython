from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
 	soup = BeautifulSoup(f, 'lxml')

# FIND_NEXT_SIBLING => ELE BUSCA PARA BAIXO SOMENTE OS IRMÃOS
# find_next_sibling

# FIND_PREVIOUS_SIBLING => ELE BUSCA SOMENTE IRMÃOS PARA CIMA
# find_previous_sibling

'''
# O EXEMPLO ABAIXO RETORNA APENAS UM IRMÃO QUE ENCONTRAR PARA BAIXO
producers = soup.find(id='producers')
next_subling = producers.find_next_sibling()
print(next_subling)
'''

'''
# RETORNANDO TODOS OS IRMÃOS QUE FOR ENCONTRADO, A DIFERENÇA É O "S" NO FINAL DA PALAVRA NEXT_SUBLINGS
producers = soup.find(id='producers')
next_sublings = producers.find_next_siblings
print(next_sublings)
'''

'''
# BUSCANDO O IRMÃO ANTERIOR
producers = soup.find(id='quaternaryconsumers')
previous_sibling = producers.find_previous_sibling()
print(previous_sibling)
'''

# BUSCANDO OS IRMÃOS ACIMA
producers = soup.find(id='quaternaryconsumers')
previous_siblings = producers.find_previous_siblings()
print(previous_siblings)