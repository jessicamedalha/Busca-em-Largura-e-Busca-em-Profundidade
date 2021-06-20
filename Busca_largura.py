import random
import numpy as np

class filas_de_busca():

	def __init__(self):
		self.fila_pai = []
		self.fila_filhos = []


	def add_pai(elemento):
		fila_pai.append(elemento)
	def add_fiho(elemento):
		fila_filhos.append(elemento)
	def remove_pai():
		fila_pai.pop(0)
	def remove_filho():
		fila_filhos.pop(0)


class busca_largura():
	def __init__():
		self.entrada = 2
		self.saida = 3
		self.parede = 0
		self.caminho = 1
		self.direcoes = []


	def ponto_de_partida(self):
		for i in range(len(self.labirinto)):
			for j in range(len(self.labirinto)):
				if(labirinto[i][j] == self.entrada):
					self.posicao_i = i
					self.posicao_j = j 
					

	def percorre_labirinto(self):
		while(True):
			if(self.tem_direcoes() == True ):
				self.direcoes = sample(range(0, 5), 4)
				for i in range(len(self.direcoes)):
					if(self.verifica_direcao(i) == True):
						if(self.tem_direcoes() == True):
							self.add_pai()
							self.remove_filho()
						else:
							self.remove_filho()

			else:

	def tem_direcoes(self):
		contador = 0
		#direita
		if((self.labirinto[self.posicao_i + 1][self.posicao_j] == self.caminho) or (self.labirinto[self.posicao_i + 1][self.posicao_j] == self.saida)):
			contador+=1

		#esquerda
		elif((self.labirinto[self.posicao_i - 1][self.posicao_j] == self.caminho) or (self.labirinto[self.posicao_i - 1][self.posicao_j] == self.saida)):
			contador+=(10)

		#cima
		elif((self.labirinto[self.posicao_i][self.posicao_j - 1] == self.caminho) or (self.labirinto[self.posicao_i ][self.posicao_j - 1] == self.saida)):
			contador += 100


		#baixo
		elif((self.labirinto[self.posicao_i][self.posicao_j + 1] == self.caminho) or (self.labirinto[self.posicao_i ][self.posicao_j + 1] == self.saida)):
			contador 1000





	def verifica_direcao():
	def tem_netos():

