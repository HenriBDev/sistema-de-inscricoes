#  H1
def cadastrarUsuario(list: [], nome: str, email: str):
	inscrito = {"nome": nome, "email": email} # dicionário
	list.append(inscrito)


# H2
def listarUsuarios(list: []):
	for usuario in list:
		print("Nome: " + usuario["nome"] + "	 " + "Email: " + usuario["email"])


# H3
def classificarEmOrdemAlfabetica(list):
	novaLista = sorted(list, key=lambda k: k["nome"])
	for usuario in novaLista:
		print("Nome: " + usuario["nome"] + "	 " + "Email: " + usuario["email"])


# H4
def buscaPorNome(list: [], nome: str):
	for usuario in list:
		if usuario["nome"] == nome:
			return True
	return False


# H5
def deletarUsuario(list: [], email: str):
	for usuario in list:
		if usuario["email"] == email:
			list.pop(usuario)
			return True
	return False


# H6
def alterarNome(list: [], email: str, novoNome: str):
	for usuario in list:
		if usuario["email"] == email:
			usuario["nome"] = novoNome
			return True
	return False

def main():

	candidatos = []

	inscrito1 = {"nome": "Gilberto De Melo Junior", "email": "gilberto@email.com"}
	inscrito2 = {"nome": "Maria de Oliveira", "email": "maria@email.com.br"}
	inscrito3 = {"nome": "Amanda da Silva", "email": "jose@email.com"}


	cadastrarUsuario(candidatos, inscrito1["nome"], inscrito1["email"])
	cadastrarUsuario(candidatos, inscrito2["nome"], inscrito2["email"])
	cadastrarUsuario(candidatos, inscrito3["nome"], inscrito3["email"])

	print('Lista de usuários por ordem de cadastro:')
	listarUsuarios(candidatos)
	print('\n')

	print('Lista de usuários em ordem alfabética:')
	classificarEmOrdemAlfabetica(candidatos)
	print('\n')

	nome = "Maria Sanches"
	resultado = alterarNome(candidatos, "maria@email.com.br", nome)
	if resultado == True:
		print("Nome alterado.")
	else:
		print("Usuario nao encontrado.")
	listarUsuarios(candidatos)


if __name__ == "__main__":
	main()
