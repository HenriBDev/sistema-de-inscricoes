import shutil
import os

def limparTela():
    os.system("CLS")

def verificaSeContemTexto(dado):
    return bool(str(dado).strip())

def verificaSeDivisivelPor2(num):
    return num % 2 == 0

def verificaSeForList(dado):
    return isinstance(dado, (list))

def stringParaList(stringParaConversao):
    comprimentoString = len(stringParaConversao)
    listFinal = [None for caracteresString in range(comprimentoString)]
    posicaoAtual = 0
    for indice in listFinal:
        listFinal[posicaoAtual] = stringParaConversao[posicaoAtual]
        posicaoAtual += 1
    return listFinal

def listParaString(listParaConversao):
    return "".join(listParaConversao)

def printFormatado(texto = "", preenchimento = " ", alinhamento = "esquerda", repetir = 1, laterais = "", inverteLateral = True):

    larguraTerminal = shutil.get_terminal_size()[0]
    terminalPar = verificaSeDivisivelPor2(larguraTerminal)
    larguraTexto = larguraTerminal
    existeTexto = bool(texto)
    existeLaterais = verificaSeContemTexto(laterais)
    existePreenchimento = verificaSeContemTexto(preenchimento)
    textoFormatado = []
    textoQuebrado = []

    if repetir < 1: repetir = 1

    if alinhamento != "esquerda" and alinhamento != "direita" and alinhamento != "centralizado": alinhamento = "esquerda"

    if existePreenchimento:
        caracteresPreenchimento = stringParaList(str(preenchimento))
    else:
        caracteresPreenchimento = [" "]

    if existeLaterais:
        caracteresLaterais = stringParaList(laterais)
        qtdCaracteresLaterais = len(caracteresLaterais)
        larguraTexto -= qtdCaracteresLaterais * 2 + 2 
        if larguraTexto <= 0:
            caracteresAMais = 1
            caracteresLaterais.pop()
            if larguraTexto < 0:
                caracteresAMais += (larguraTexto * -1) // 2 + 1
                del caracteresLaterais[qtdCaracteresLaterais - caracteresAMais + 1 : qtdCaracteresLaterais]
            larguraTexto = 2 if terminalPar else 1
        caracteresLaterais.reverse()

    textoQuebrado = dividirLinhasECaracteres(texto, larguraTexto)

    qtdLinhas = len(textoQuebrado)

    for linhaAtual in range(qtdLinhas):
        qtdCaracteresTexto = len(textoQuebrado[linhaAtual])
        textoQuebrado[linhaAtual] = preencherLinha(qtdEspacosVazios = larguraTexto - qtdCaracteresTexto,
                                                   preenchimento = caracteresPreenchimento,
                                                   tipoPreenchimento = alinhamento,
                                                   linha = textoQuebrado[linhaAtual])
        if existeLaterais:
            textoQuebrado[linhaAtual].insert(0," ")
            textoQuebrado[linhaAtual].append(" ")
            espacoLateral = larguraTerminal - larguraTexto - 2
            if inverteLateral:
                textoQuebrado[linhaAtual] = preencherLinha(qtdEspacosVazios = espacoLateral,
                                                           preenchimento = caracteresLaterais,
                                                           tipoPreenchimento = "centralizado",
                                                           linha = textoQuebrado[linhaAtual])
            else:
                textoQuebrado[linhaAtual] = preencherLinha(qtdEspacosVazios = espacoLateral // 2,
                                                           preenchimento = caracteresLaterais,
                                                           tipoPreenchimento = "direita",
                                                           linha = textoQuebrado[linhaAtual])
                caracteresLaterais.reverse()
                textoQuebrado[linhaAtual] = preencherLinha(qtdEspacosVazios = espacoLateral // 2 + (0 if terminalPar else 1),
                                                           preenchimento = caracteresLaterais,
                                                           tipoPreenchimento = "esquerda",
                                                           linha = textoQuebrado[linhaAtual])
                caracteresLaterais.reverse()

    for r in range(repetir):
        for linhaAtual in range(qtdLinhas):
            textoFormatado.append(textoQuebrado[linhaAtual])
            
    for linha in textoFormatado:
        linhaEmString = listParaString(linha)
        print(linhaEmString, end = "")

def preencherLinha(qtdEspacosVazios, preenchimento, tipoPreenchimento = "centralizado", linha = [""]):
    indice = 0
    caracterAtual = 1
    qtdCaracteresPreenchimento = len(preenchimento)
    while caracterAtual <= qtdEspacosVazios:
        if indice >= qtdCaracteresPreenchimento:
            indice = 0
        if tipoPreenchimento == "direita" or tipoPreenchimento == "centralizado" and caracterAtual <= qtdEspacosVazios:
            linha.insert(0, preenchimento[indice])
            caracterAtual += 1
        if tipoPreenchimento == "esquerda" or tipoPreenchimento == "centralizado" and caracterAtual <= qtdEspacosVazios:
            linha.append(preenchimento[indice])
            caracterAtual += 1
        indice += 1
    return linha

def dividirLinhasECaracteres(texto, larguraLinha):
    textoQuebrado = []
    linhaPar = verificaSeDivisivelPor2(larguraLinha)
    multiplasLinhas = verificaSeForList(texto)
    if multiplasLinhas:
        totalLinhas = len(texto)
    else:
        totalLinhas = 1
    for linha in range(totalLinhas):
        caracteres = stringParaList(texto[linha] if multiplasLinhas else texto)
        totalCaracteres = len(caracteres)
        caracteresPar = verificaSeDivisivelPor2(totalCaracteres)
        if totalCaracteres > larguraLinha:
            totalDivisoes = totalCaracteres // larguraLinha + (1 if not caracteresPar and linhaPar else 0)
        else:
            totalDivisoes = 1
        for linhaDividida in range(totalDivisoes):
            inicioLinha = linhaDividida * larguraLinha
            finalLinha = inicioLinha + larguraLinha
            linhaAtual = texto[linha][inicioLinha : finalLinha] if multiplasLinhas else texto[inicioLinha : finalLinha]
            caracteresLinha = stringParaList(linhaAtual)
            textoQuebrado.append(caracteresLinha)
    return textoQuebrado