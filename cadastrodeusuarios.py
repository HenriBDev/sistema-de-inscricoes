
def criarCandidato(list: []):

    novoCandidato = {}
    novoCandidato["nome"] = input("Digite o nome do candidato: ")
    novoCandidato["email"] = input("Digite o email do candidato: ")
    return novoCandidato

def adicionarNovoCandidato(list: []):
    qtdCandidatos = int(input("informe quantos candidatos deseja adicionar a sua lista: "))
    valor = 0
    while(valor < qtdCandidatos):
        umCandidato = criarCandidato(list)
        list.append(umCandidato)
        qtdCandidatos -= 1
    print("Candidatos adicionados com sucesso!")

def listarUsuarios(list: []):
	for usuario in list:
		print("Nome: " + usuario["nome"] + "	 " + "Email: " + usuario["email"])


def classificarEmOrdemAlfabetica(list: []):
	novaLista = sorted(list, key=lambda k: k["nome"])
	for usuario in novaLista:
		print("Nome: " + usuario["nome"] + "	 " + "Email: " + usuario["email"])


def buscaPorNome(list: [], nome: str):
	for usuario in list:
		if usuario["nome"] == nome:
			return True
	return False


def deletarUsuario(list: [], email: str):
	for usuario in list:
		if usuario["email"] == email:
			list.pop(usuario)
			return True
	return False


def alterarNome(list: [], email: str, novoNome: str):
	for usuario in list:
		if usuario["email"] == email:
			usuario["nome"] = novoNome
			return True
	return False


def main():

	candidatos = []

	adicionarNovoCandidato(candidatos)
	print(candidatos)

	#print('Lista de usuários por ordem de cadastro:')
	#listarUsuarios(candidatos)
	#print('\n')

	#print('Lista de usuários em ordem alfabética:')
	#classificarEmOrdemAlfabetica(candidatos)
	#print('\n')

	#nome = "Maria Sanches"
	#resultado = alterarNome(candidatos, "maria@email.com.br", nome)
	#if resultado == True:
		#print("Nome alterado.")
	#else:
		#print("Usuario nao encontrado.")
	#listarUsuarios(candidatos)


if __name__ == "__main__":
	main()
