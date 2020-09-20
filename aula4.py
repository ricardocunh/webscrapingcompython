from bs4 import BeautifulSoup
from bs4.element import Tag

with open('arquivo03.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

# FAZENDO A IMPRESSÃO DA TAG <UL> DO ARQUIVO 03 COM DOIS NEXT_ELEMENT
#print(soup.div.next_element.next_element)

# FAZENDO A IMPRESSÃO DAS <LI> 
#print(soup.div.next_element.next_element.next_element.next_element)

'''
# INTERANDO COM OS ELEMENTOS A PARTIR DO UL
for e in soup.ul.next_elements:
	if isinstance(e, Tag):
		print(e)
'''

# fAZENDO A IMPRESSÃO DOS ELEMENTOS ANTERIORES A PARTIR DO LI
for e in soup.li.previous_elements:
	print(repr(e))