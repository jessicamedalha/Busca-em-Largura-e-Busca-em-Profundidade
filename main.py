from Busca_largura import busca_largura
from Busca_profundidade import busca_profundidade

class main():
	def __init__(self):

		while(1):
			busca = input("Digite 'l' para busca por largura, 'p' para busca em profundidade ou 's' para sair:")
			if(busca == 'l'):
				busca_largura()
			if(busca == 'p'):
				busca_profundidade()
			if(busca == 's'):
				break

n = main()
