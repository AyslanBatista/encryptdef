"""Módulo que contém toda parte de interação com o usuário"""

import os
import sys
from typing import List, Tuple

from rich.markdown import Markdown

from encryptdef.log import print_and_record_log
from encryptdef.settings import console
from encryptdef.template import (
    TEMPLATE_ERROR_EMPTY_FIELD,
    TEMPLATE_ERROR_INVALID_CHOICE,
    TEMPLATE_GET_MAX_WORKERS,
    TEMPLATE_INFO,
    TEMPLATE_LOGO,
)
from encryptdef.utils import clear_console


def print_template_logo(info: bool = False) -> None:
    """
    Limpa o terminal e imprime a logo da ferramenta.

    Args:
        info (bool): Se True, imprime também as informações da ferramenta.
    """
    clear_console()
    console.print(TEMPLATE_LOGO)

    if info:
        md = Markdown(TEMPLATE_INFO)
        console.print(md)


def get_user_input(prompt: str, password: bool = False) -> str:
    """
    Solicita a entrada do usuário com um prompt.

    Args:
        prompt (str): Mensagem a ser exibida ao solicitar a entrada.
        password (bool): Se True, esconde a entrada do usuário (uso de senha).

    Returns:
        str: A entrada fornecida pelo usuário.
    """
    return console.input(prompt, password=password).strip()


def validate_and_get_input(prompts: List[str]) -> List[str]:
    """
    Valida e solicita uma lista de entradas do usuário com base nos prompts
    fornecidos.

    Args:
        prompts (List[str]): Lista de mensagens a serem exibidas ao solicitar
        a entrada.

    Returns:
        List[str]: Lista de entradas fornecidas pelo usuário.
    """
    while True:

        try:
            inputs = [
                get_user_input(prompt, "🔑" in prompt) for prompt in prompts
            ]

            if any(not input for input in inputs):
                raise ValueError(TEMPLATE_ERROR_EMPTY_FIELD)
            return inputs

        except ValueError as e:
            clear_console()
            print_template_logo()
            print_and_record_log(str(e), "error")


def print_request_menu(menu: str) -> int:
    """
    Imprime o template de entrada e o menu fornecido, solicitando a escolha do
    usuário.

    Args:
        menu (str): Template do menu a ser impresso.

    Returns:
        int: Número da opção escolhida pelo usuário.
    """
    print_template_logo(info=True)
    while True:
        console.print(menu)

        try:
            choice = console.input("\n[?] : ")

            if choice == "3":
                sys.exit(1)

            if choice not in ("1", "2"):
                raise ValueError(TEMPLATE_ERROR_INVALID_CHOICE)

            return int(choice)

        except ValueError as e:
            clear_console()
            print_template_logo(info=True)
            print_and_record_log(str(e), "error")


def print_requesting_message(
    template_message: str, template_key: str
) -> Tuple[str, str]:
    """
    Solicita dados e chave do usuário.

    Args:
        template_message (str): Template da solicitação de dados.
        template_key (str): Template da solicitação de chave.

    Returns:
        Tuple[str, str]: Contendo os dados e a chave fornecidos pelo usuário.
    """
    print_template_logo()
    data, key = validate_and_get_input([template_message, template_key])
    return data, key


def print_success_message(
    message: str,
    template_title: str,
    template_result: str,
) -> None:
    """
    Imprime uma mensagem de sucesso e o depois o resultado.

    Args:
        message (str): A mensagem que foi criptografada ou descriptografada.
        requesting (int): Número da opção escolhida pelo usuário.
    """
    print_and_record_log(template_title, "debug")
    print_and_record_log(template_result % message, "debug")


def print_requesting_file(template_file: str) -> List[str]:
    """
    Solicita nome do arquivo, chave e novo nome do arquivo do usuário.

    Args:
        template_file (str): Template da solicitação do arquivo.

    Returns:
        List[str]: Lista contendo as informações fornecidas pelo usuário.
    """
    print_template_logo()
    data_template = template_file.split("\n")
    return validate_and_get_input(data_template)


def print_get_max_workers(lines: List[str]) -> int:
    """
    Determina o número máximo de núcleos da CPU a serem usados.

    Args:
        lines (List[str]): Lista de linhas do arquivo.

    Returns:
        int: Número máximo de núcleos da CPU a serem usados.
    """
    while True:
        try:
            max_workers = os.cpu_count()
            if max_workers is None:
                max_workers = 1

            if len(lines) > 500:
                use_more_cores = int(
                    console.input(TEMPLATE_GET_MAX_WORKERS % max_workers)
                )
                console.print("\n", end="")

                if not use_more_cores or use_more_cores > max_workers:
                    raise ValueError(TEMPLATE_ERROR_INVALID_CHOICE)

                return use_more_cores

            return 1

        except ValueError as e:
            print_and_record_log(str(e), "error")


def print_continue_or_leave(template: str) -> str:
    """
    Solicita ao usuário se deseja continuar ou sair.

    Args:
        template (str): Template da solicitação.

    Returns:
        str: Resposta do usuário.
    """
    return get_user_input(template)
