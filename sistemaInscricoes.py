
def inscreverCandidato(list, nome, email):
	inscrito = {"nome": nome, "email": email} # dicionário
	list.append(inscrito)

# H2
def listarUsuarios(list):
	print("*** List a de Inscritos por Ordem de Cadastro.")
	for usuario in list:
		print("Nome: " + usuario["nome"] + "	 " + "Email: " + usuario["email"])


def classificarEmOrdemAlfabetica(list):

	novaLista = sorted(list, key=lambda k: k["nome"])
	print("*** Lista de Inscritos em Ordem Alfabetica ***")
	print(novaLista)


# H6
def alterarNome(list, email, novoNome):
	for usuario in list:
		if usuario["email"] == email:
			usuario["nome"] = novoNome


def main():

	candidatos = []

	inscrito1 = {"nome": "Gilberto De Melo Junior", "email": "gilberto@email.com"}
	inscrito2 = {"nome": "Maria de Oliveira", "email": "maria@email.com.br"}
	inscrito3 = {"nome": "Amanda da Silva", "email": "jose@email.com"}


	inscreverCandidato(candidatos, inscrito1["nome"], inscrito1["email"])
	inscreverCandidato(candidatos, inscrito2["nome"], inscrito2["email"])
	inscreverCandidato(candidatos, inscrito3["nome"], inscrito3["email"])
	listarUsuarios(candidatos)

	print('\n')
	classificarEmOrdemAlfabetica(candidatos)
	print('\n')

	# Mudar nome
	nome = "Maria Sanches"
	alterarNome(candidatos, "maria@email.com.br", nome)
	listarUsuarios(candidatos)


main()