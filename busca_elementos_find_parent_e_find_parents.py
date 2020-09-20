from bs4 import BeautifulSoup

with open('arquivo04.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')


# OBSERVAÇÃO

# O "FIND" E O "FIND_ALL" PROCURAM PARA BAIXO DOS ELEMENTOS PAI

# O "FIND_PARENT" E O "FIND_PARENTS" ELES BUSCAM PARA CIMA DA ÁRVORE DO PAI


primaryconsumers = soup.find_all(class_='primaryconsumerlist')
primaryconsumer = primaryconsumers[0]
print(primaryconsumer)


# ENCONTRAR TODOS OS PAIS DO "UL"
parent_ul = primaryconsumer.find_parents('ul')
print(parent_ul)


