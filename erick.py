def buscaPorNome(list: []):
    try:
        nome = input("Digite o nome para a consulta: ")
        for usuario in list:
            if usuario['nome'] == nome:
                cond = f"O usuário {nome} {usuario['email']} se encontra na lista"
                break
            else:
                cond = "Usuário não encontrado!"
        print(cond)
    except:
        print("Ainda não há uma lista. Favor insira ao menos um usuário")


def excluiAlunoPorEmail(list: []):
    email = input("DIgite o email para a exclusão do usuário: ")
    try:
        usuarioNaoEncontrado = True
        for usuario in list:
            if usuario['email'] == email:
                usuarioNaoEncontrado = False
                verificacao = input(
                    f"Gostaria de excluir o usuário {usuario['nome']} {usuario['email']}? S - Confirma, N - Abnega: ").upper()[0]
                if (verificacao == "S"):
                    list.pop(list.index(usuario))
                elif (verificacao == "N"):
                    return
        if usuarioNaoEncontrado:
            print("usuario Nao Encontrado")
    except:
        print("Ainda não há uma lista!")
