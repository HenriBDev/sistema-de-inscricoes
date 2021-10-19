import os

os.system("CLS")


def adicionaNovosUsuarios(list: []):
    os.system("CLS")

    while True:
        try:
            qtdalunos = int(input("Informe quantos alunos deseja adicionar: "))
            cont = 0
            while(cont < qtdalunos):
                umAluno = criaAluno(list)
                list.append(umAluno)
                qtdalunos -= 1
            os.system("CLS")
            break
        except:
            os.system("CLS")
            print("Favor, digite apenas números!")


def criaAluno(listaAlunos):
    os.system("CLS")

    novoAluno = {}
    novoAluno["nome"] = input("Digite o nome do aluno: ")
    if len(listaAlunos) > 0:
        existeEmail = True
    else:
        existeEmail = False
        novoAluno["email"] = input("Digite o email do aluno: ")
    while existeEmail:
        novoAluno["email"] = input("Digite o email do aluno: ")

        for usuario in listaAlunos:
            if usuario["email"] == novoAluno["email"]:
                existeEmail = True
                break
        else:
            existeEmail = False
        if existeEmail:
            os.system("CLS")
            print(
                f"Email {usuario['email']} já existente, digite outro por favor.")
    return novoAluno


def listarUsuarios(list: []):
    os.system("CLS")

    if len(list) > 0:
        print("\n*** Lista de Inscritos por Ordem de Inscrição.\n")
        for usuario in list:
            print("Nome: " + usuario["nome"] +
                  "  ===  " + "Email: " + usuario["email"])
    else:
        print("Não há usuários cadastrados!\n")

    os.system('pause')
    os.system("CLS")


def exibirUsuariosAlfabetica(list: []):
    os.system("CLS")

    if len(list) > 0:
        nomesOrdenados = sorted(list, key=lambda k: k["nome"])
        for nome in nomesOrdenados:
            print(f'Nome: {nome["nome"]} \tE-mail: {nome["email"]}')
    else:
        print("Não há usuários cadastrados!\n")

    os.system('pause')
    os.system("CLS")

def buscaPorNome(list: []):
    os.system("CLS")

    try:
        nome = input("Digite o nome para a consulta: ")
        for usuario in list:
            if usuario['nome'] == nome:
                cond = f"O usuário Nome: {nome} Email: {usuario['email']} está cadastrado"
                break
            else:
                cond = "Usuário não encontrado!"
        print(cond)
    except:
        print("Ainda não há uma lista. Favor insira ao menos um usuário")

    os.system("pause")
    os.system("CLS")


def excluiAlunoPorEmail(list: []):
    os.system("CLS")

    email = input("DIgite o email para a exclusão do usuário: ")

    usuarioNaoEncontrado = True
    for usuario in list:
        if usuario['email'] == email:
            usuarioNaoEncontrado = False
            while True:
                verificacao = input(
                    f"Gostaria de excluir o usuário Nome: {usuario['nome']} Email: {usuario['email']}? S - Confirma, N - Abnega: ").upper()[0]
                if (verificacao == "S"):
                    list.pop(list.index(usuario))
                    print("Usuário deletado com sucesso!")
                    break
                elif (verificacao == "N"):
                    break
                else:
                    print("Digite apenas S ou N!")

    if usuarioNaoEncontrado:
        print("usuario Nao Encontrado")

    os.system("pause")
    os.system("CLS")


def alterarNome(list: []):
    email = input("Digite o email do usuário para alterar o nome: ")
    usuarioNaoEncontrado = True
    for usuario in list:
        if usuario["email"] == email:
            usuarioNaoEncontrado = False
            while True:
                verificacao = input(
                    f"Gostaria de alterar o nome do usuário Nome: {usuario['nome']} Email: {usuario['email']}? S - Confirma, N - Abnega: ").upper()[0]

                if (verificacao == "S"):
                    novoNome = input("Digite o novo nome: ")
                    usuario["nome"] = novoNome
                    print("Nome alterado!")
                    return True
                elif (verificacao == "N"):
                    return True
                else:
                    print("Digite apenas S ou N!")
    if usuarioNaoEncontrado:
        print("usuario Nao Encontrado")

    os.system("pause")
    os.system("CLS")


def menu():
    listaAlunos = []

    while True:
        menuLayout()

        try:
            op = int(input("\nEscolha uma opção de (1 a 7): "))

            if(op == 1):
                adicionaNovosUsuarios(listaAlunos)
            elif(op == 2):
                listarUsuarios(listaAlunos)
            elif(op == 3):
                exibirUsuariosAlfabetica(listaAlunos)
            elif(op == 4):
                buscaPorNome(listaAlunos)
            elif(op == 5):
                excluiAlunoPorEmail(listaAlunos)
            elif(op == 6):
                alterarNome(listaAlunos)
            elif(op == 7):
                os.system("CLS")
                print("Encerrando o programa!")
                os.system("pause")
                break
            else:
                os.system("CLS")
                print("Opção inválida!")
                os.system("pause")
                os.system("CLS")
        except:
            os.system("CLS")
            print("Favor, digite apenas números!")


def menuLayout():
    print("\nO que deseja fazer??\n")
    print("1 - Cadastrar novos usuários!")
    print("2 - Exibir todos os usuários cadastrados!")
    print("3 - Exibir todos os usuários cadastros em ordem alfabetica!")
    print("4 - Verificar se um usuário faz parte da lista de participantes!")
    print("5 - Remover um usuário cadastrado pelo seu email!")
    print("6 - Alterar o nome de um usuário cadastrado!")
    print("7 - Finaliza a operação!")


def mensagemEntrada():
    print("Olá. Seja Bem vindo ao app de gestão de inscritos!")


def main():
    mensagemEntrada()
    menu()


if __name__ == "__main__":
    main()
