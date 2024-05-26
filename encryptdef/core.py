"""Módulo que contém as funções principais da ferramenta"""

import os
import time
import cryptocode
from interface import (
    print_menu_de_solicitacao,
    solicitando_dados,
    solicitando_arquivo,
    continuar_sair,
)

from settings import (
    CURRENT_DIR,
    TEMPLATE_MENU_DADOS_ARQUIVO,
    TEMPLATE_MENU_ENCRIPT_DECRIPT,
    TEMPLATE_CONTINUAR_SAIR,
    TEMPLATE_DADOS_ENCRIPT,
    TEMPLATE_KEY_ENCRIPT,
    TEMPLATE_DADOS_DECRIPT,
    TEMPLATE_KEY_DECRIPT,
    TEMPLATE_ARQUIVO_ENCRIPT,
    TEMPLATE_ARQUIVO_DECRIPT,
)


def encript_dados(dados, key):
    """Função recebe dados e uma chave para fazer encriptação dos dados

    Args:
        dados (str): dados para serem encriptados
        key (str): chave referente a encriptação dos dados
    """
    cifra_incriptions = cryptocode.encrypt(dados, key)
    print(f"\n [-] 🔒 ENCRIPTADO: {cifra_incriptions}")
    print(f" [-] 🔑 KEY: {key}")


def decript_dados(dados, key):
    """Função recebe dados encriptados e uma chave para decodificar os
    dados, caso não encontre a chave ele retorna False, caso de certo
    impre o resulto e retorna True

    Args:
        dados (str): dados para serem decriptados
        key (str): chave referente a encriptação dos dados

    Returns:
        bool: Retorna True se ele conseguir decriptar, caso contrario
        retorna False
    """
    decrypt_cifras = cryptocode.decrypt(dados, key)
    print("\n 🔐 [D E C R I P T A N D O. . .]\n")
    time.sleep(2)

    if not decrypt_cifras:
        print("\n [X] KEY NÃO ECONTRADA, TENTE UMA CHAVE CORRETA!\n")
        return False

    print(f"\n [!] 🔓 DECODIFICADO: {decrypt_cifras}")
    print(f" [!] 🔑 KEY: {key}")
    return True


def encript_arquivo(lista_dados):
    """Função recebe uma lista com dados para fazer encriptação do arquivo.
    Função Abre o arquivo e faz um for em cada linha do arquivo, encriptando as
    linhas e salvando em uma lista, depois cria um novo arquivo e cola
    toda a informação que está na lista.

    Args:
        lista_dados (list): lista de dados que contem nome/caminho do arquivo,
    chave para encriptar e nome do novo arquivo encriptado.

    Returns:
        bool: retorna True caso a encriptação der certo, retorna False caso
        de algo errado.
    """

    arquivo, chave, novo_arquivo = lista_dados

    if not os.path.isabs(arquivo):
        novo_arquivo_path = os.path.join(CURRENT_DIR, novo_arquivo)

    try:
        with open(arquivo, "r") as file_:
            linhas_encriptadas = []

            for linha in file_:
                linha_encript = cryptocode.encrypt(linha, chave)
                linhas_encriptadas.append(linha_encript + "\n")

        with open(novo_arquivo_path, "w") as file_a:
            file_a.writelines(linhas_encriptadas)

        print("\n 🔒 [A R Q U I V O -- E N C R I P T A D O]\n")
        print(f" {novo_arquivo_path}")
        return True

    except FileNotFoundError:
        print(f"\n [X] ARQUIVO {arquivo} NÃO ENCONTRADO!\n")
        print(
            " [X] COLOQUE O ARQUIVO NO DIRETORIO ATUAL,"
            "OU INFORME O CAMINHO EXATO DO ARQUIVO, EXEMPLO: /tmp/teste.txt"
        )
        return False


def decript_arquivo(lista_dados):
    """Função recebe uma lista com dados para fazer decriptação do arquivo.
    Função Abre o arquivo e faz um for em cada linha do arquivo, decriptando as
    linhas caso a chave estiver correta, sera salvo cada linha em uma lista,
    e esta lista depois sera salva dentro de um novo arquivo.

    Args:
        lista_dados (list): lista de dados que contem nome/caminho do arquivo,
    chave para decriptar e nome do novo arquivo decriptado.

    Returns:
        bool: retorna True caso a decriptação der certo, retorna False caso
        de algo errado.
    """

    arquivo, chave, novo_arquivo = lista_dados

    if not os.path.isabs(arquivo):
        novo_arquivo_path = os.path.join(CURRENT_DIR, novo_arquivo)

    try:
        with open(arquivo, "r") as file_:
            linhas_decriptadas = []

            for linha in file_:
                linha_decript = cryptocode.decrypt(linha, chave)

                if not linha_decript:
                    print(
                        "\n [X] KEY NÃO ECONTRADA, TENTE UMA CHAVE CORRETA!\n"
                    )
                    return False

                linhas_decriptadas.append(linha_decript)

        with open(novo_arquivo_path, "w") as file_a:
            file_a.writelines(linhas_decriptadas)

        print("\n 🔓 [A R Q U I V O -- D E C R I P T A D O]\n")
        print(f" 📄 {novo_arquivo_path}")
        return True

    except FileNotFoundError:
        print(f"\n [X] ARQUIVO {arquivo!r} NÃO ENCONTRADO!")
        print(
            " [X] COLOQUE O ARQUIVO NO DIRETORIO ATUAL"
            " OU INFORME O CAMINHO EXATO DO ARQUIVO, EXEMPLO: /tmp/teste.txt"
        )
        return False


def main():
    """Função principal que ira chamar todas as outras funções"""
    while True:

        opcao_dados_arquivo = print_menu_de_solicitacao(
            TEMPLATE_MENU_DADOS_ARQUIVO
        )

        if opcao_dados_arquivo == 1:
            opcao_dados_encript_decript = print_menu_de_solicitacao(
                TEMPLATE_MENU_ENCRIPT_DECRIPT
            )

            if opcao_dados_encript_decript == 1:
                dados_encript, chave_dados_encript = solicitando_dados(
                    TEMPLATE_DADOS_ENCRIPT, TEMPLATE_KEY_ENCRIPT
                )

                encript_dados(dados=dados_encript, key=chave_dados_encript)

            if opcao_dados_encript_decript == 2:
                dados_decript, chave_dados_decript = solicitando_dados(
                    TEMPLATE_DADOS_DECRIPT, TEMPLATE_KEY_DECRIPT
                )

                decript_dados(dados=dados_decript, key=chave_dados_decript)

        if opcao_dados_arquivo == 2:
            opcao_arquivo_encript_decript = print_menu_de_solicitacao(
                TEMPLATE_MENU_ENCRIPT_DECRIPT
            )

            if opcao_arquivo_encript_decript == 1:
                lista_arquivo_encript = solicitando_arquivo(
                    TEMPLATE_ARQUIVO_ENCRIPT
                )

                encript_arquivo(lista_arquivo_encript)

            if opcao_arquivo_encript_decript == 2:
                lista_arquivo_decript = solicitando_arquivo(
                    TEMPLATE_ARQUIVO_DECRIPT
                )

                decript_arquivo(lista_arquivo_decript)

        if continuar_sair(template=TEMPLATE_CONTINUAR_SAIR):
            break
