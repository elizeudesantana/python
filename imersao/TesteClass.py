#!/usr/bin/python

import datetime

# by: Elizeu de Santana em: 27/05/2019--------------------------------------------
class Usuario:
	"""Um usuario membro da Class FriendFace, implementacao [nome completo e aniversario]."""

	def __init__(self, nome_completo, aniversario): 
		""" Construtor da classe e faz a separacao do primeiro nome e ultimo"""
		self.nome = nome_completo
		self.aniversario =	aniversario #yyyymmdd

		# Extraindo o primeiro nome
		nome_separado = nome_completo.split(" ")
		self.nome_primeiro = nome_separado[0]
		self.nome_ultimo = nome_separado[-1]

	def idade(self): # Metodo
		"""Retorna a idade em anos."""
		hoje = datetime.date(2019,05,28)
		yyyy = int(self.aniversario[0:4])
		mm = int(self.aniversario[4:6])
		dd = int(self.aniversario[6:8])

		dob = datetime.date(yyyy, mm, dd) # Aniversario
		idade_em_dias = (hoje - dob).days
		idade_em_anos = idade_em_dias / 365
		return int(idade_em_anos)

usuario = Usuario("Elizeu de Santana", "19680225")

print "Primeiro nome : ", usuario.nome_primeiro
print "Segundo nome  : ", usuario.nome_ultimo
print "Nome Completo : ", usuario.nome
print "Idade usuario : ", usuario.idade()

#help(Usuario)




	
	