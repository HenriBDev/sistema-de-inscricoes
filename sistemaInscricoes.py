
def inscreverCandidato(list, nome, email):
	inscrito = {"nome": nome, "email" : email} # dicionário
	list.append(inscrito)


def listarUsuarios(list):
	print("*** List a de Inscritos por Ordem de Inscrição.")
	for usuario in list:
		print("Nome: " + usuario["nome"] + "	 " + "Email: " + usuario["email"])


def classificarEmOrdemAlfabetica(list):

	novaLista = sorted(list, key=lambda k: k["nome"])
	print("*** Lista de Inscritos em Ordem Alfabetica ***")
	print(novaLista)	


def main():

	candidatos = []
	
	
	inscrito1 = {"nome" : "Gilberto De Melo Junior", "email" : "gilberto@email.com"}
	inscrito2 = {"nome" : "Maria de Oliveira", "email" : "maria@emaiil.com.br"}
	inscrito3 = {"nome" : "Amanda da Silva", "email" : "jose@email.com"}


	inscreverCandidato(candidatos, inscrito1["nome"], inscrito1["email"])
	inscreverCandidato(candidatos, inscrito2["nome"], inscrito2["email"])
	inscreverCandidato(candidatos, inscrito3["nome"], inscrito3["email"])
	listarUsuarios(candidatos)

	classificarEmOrdemAlfabetica(candidatos)


main()