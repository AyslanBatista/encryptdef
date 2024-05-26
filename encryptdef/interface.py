"""Módulo que contém toda parte de interação com o usuario"""

import os
from settings import TEMPLATE_INFO, TEMPLATE_LOGO


def print_template_logo(info=False):
    """Função ira limpar limpar o terminal e imprimir a logo
    da ferramenta.

    Args:
        info (bool, optional): Argumento por padrão é False, se for True
        ele irá imprimir as informações da ferramenta.
    """
    os.system("clear")
    print(TEMPLATE_LOGO)

    if info:
        print(TEMPLATE_INFO)


def print_menu_de_solicitacao(menu):
    """Função ira imprimir o template de entrada e depois
    imprimir o template de menu que foi enviado no argumento,
    e através de um input receber e retorna o numero `1` ou `2`
    de acordo com a opção escolhida pelo usuario.

    Returns:
        int: numero da opção que foi escolhida
    """
    print_template_logo(info=True)

    while True:
        print(menu)

        try:
            escolha = int(input("\n [?] : "))

            if escolha not in (1, 2):
                raise ValueError

            break

        except ValueError:
            os.system("clear")
            print_template_logo(info=True)
            print("\n [X] ERRO - ESCOLHA INVALÍDA. TENTA NOVAMENTE!")

    return escolha


def solicitando_dados(template_dados, template_key):
    """Função recebe como argumento dois template para fazer
    uma soliticação ao usuario dos dados e chave, e depois retorna
    essas informações.

    Args:
        template_dados (str): contendo o template da opção que
        deseja, entre encript e decript.
        template_key (str): contendo o template de solitação de
        key, entre encript e decript.

    Raises:
        ValueError: Caso o usuario deixe o input em branco ou
        digite algum espaço vazio.

    Returns:
        tuple: tuple contendo dois valores, os `dados` e a `key`.
    """
    print_template_logo()

    while True:

        try:
            dados = input(f"{template_dados}: ").strip()
            if not dados:
                raise ValueError

            key = input(f"{template_key}:").strip()
            if not key:
                raise ValueError

            break

        except ValueError:
            os.system("clear")
            print_template_logo(info=True)
            print("\n [X] ERRO - CAMPO ESTÁ VAZIO. TENTA NOVAMENTE!")

    return dados, key


def solicitando_arquivo(template_arquivo):
    """Função recebe como argumento um template para fazer a solicitação
    ao usuario do arquivo, chave e novo nome do arquivo.
    A função ira quebrar o template recebido que está em formato de
    string separando pela quebra de linha e transformando em uma lista
    com os elementos, cada elemento será a pergunta do input.
    Após receber o input, é armazenado tudo em uma lista e retornado
    no final da função.

    Args:
        template_arquivo (str): String com todas as perguntas do input
        separado por quebra de linha.

    Raises:
        ValueError: Caso o usuario deixe o input em branco ou
        digite algum espaço vazio.

    Returns:
        list: Lista contendo todas as informações recebidas do usuario
    """
    print_template_logo()

    dados_template = template_arquivo.split("\n")
    dados_arquivo = []

    while True:

        try:
            for template in dados_template:

                dados = input(f"{template}: ").strip()
                if not dados:
                    raise ValueError

                dados_arquivo.append(dados)

            break

        except ValueError:
            os.system("clear")
            print_template_logo(info=True)
            print("\n [X] ERRO - CAMPO ESTÁ VAZIO. TENTA NOVAMENTE!")

    return dados_arquivo


def continuar_sair(template):
    """Função recebe um template e usa como pergunta em um input
    para o usuario, e retorn o input do usuario

    Args:
        template (str): string que contém um pergunta para o input

    Returns:
        Any: retorna o input do usuario
    """
    return input(template)
