from bs4 import BeautifulSoup

with open('arquivo02.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

'''
# Acessando o PAI do elemento atual com parent
# OBS. A tag HTML não tem PAI, ela é raiz!
print(soup.parent)

# Para que funcione, vamos pegar a title
tag_title = soup.title
print(tag_title)

# Acessando o pai da tag title
print(tag_title.parent)


# Acessando o pai da tag TD
print(soup.td.parent)

# Acessando o irmão do TD
print(soup.td.next_sibling.next_sibling)
'''

# INTERANDO NOS ELEMENTOS
for sibling in soup.p.next_sibling:
	print(repr(sibling))