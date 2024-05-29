"""Módulo que contém as funções principais da ferramenta"""

import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, List, Optional, Union

import rich_click as click
from rich.progress import Progress

from encryptdef.cryptocode import InvalidEncryptedFormat, decrypt, encrypt
from encryptdef.interactive_interface import (
    print_continue_or_leave,
    print_get_max_workers,
    print_request_menu,
    print_requesting_file,
    print_requesting_message,
)
from encryptdef.log import print_and_record_log
from encryptdef.settings import CURRENT_DIR, console
from encryptdef.template import (
    TEMPLATE_CONTINUE_LEAVE,
    TEMPLATE_DECRYPT_FILE,
    TEMPLATE_DECRYPT_KEY,
    TEMPLATE_DECRYPT_MESSAGE,
    TEMPLATE_DECRYPTED,
    TEMPLATE_DECRYPTED_FILE,
    TEMPLATE_DECRYPTED_MESSAGE,
    TEMPLATE_ENCRYPT_FILE,
    TEMPLATE_ENCRYPT_KEY,
    TEMPLATE_ENCRYPT_MESSAGE,
    TEMPLATE_ENCRYPTED,
    TEMPLATE_ENCRYPTED_FILE,
    TEMPLATE_ENCRYPTED_MESSAGE,
    TEMPLATE_ERROR_EMPTY_FIELD,
    TEMPLATE_FILE_NOT_FOUND,
    TEMPLATE_INFO_FILE,
    TEMPLATE_INVALID_KEY,
    TEMPLATE_MENU_ENCRYPT_DECRYPT,
    TEMPLATE_MENU_MESSAGE_FILE,
    TEMPLATE_TASK_DESCRIPTION,
    TEMPLATE_TYPE_ERROR,
)


def get_new_file_path(file: str, new_file: str) -> str:
    """
    Retorna o caminho completo do novo arquivo.

    Args:
        file (str): Caminho do arquivo original.
        new_file (str): Nome do novo arquivo.

    Returns:
        str: Caminho completo do novo arquivo.
    """
    return (
        os.path.join(CURRENT_DIR, new_file)
        if not os.path.isabs(file)
        else new_file
    )


def read_file(file: str) -> List[str]:
    """
    Lê o conteúdo do arquivo e retorna uma lista de linhas.

    Args:
        file (str): Caminho do arquivo a ser lido.

    Returns:
        List[str]: Lista de linhas do arquivo.

    Raises:
        FileNotFoundError: Se o arquivo não for encontrado.
    """
    with open(file, "r", encoding="utf-8", errors="ignore") as file_:
        return file_.readlines()


def write_file(new_file_path: str, processed_lines: List[str]) -> None:
    """
    Escreve as linhas processadas em um novo arquivo.

    Args:
        new_file_path (str): Caminho do novo arquivo.
        processed_lines (List[str]): Lista de linhas processadas.

    Raises:
        IOError: Se ocorrer um erro ao escrever no arquivo.
    """
    with open(new_file_path, "w", encoding="utf-8") as file_a:
        file_a.writelines(processed_lines)


def process_lines(
    lines: List[str],
    key: str,
    process_line_func: Callable[[str, str], Union[str, bool]],
    max_workers: int,
) -> List[str]:
    """
    Processa cada linha do arquivo usando a função fornecida.

    Args:
        lines (List[str]): Lista de linhas do arquivo.
        key (str): Chave para criptografar ou descriptografar.
        process_line_func (Callable[[str, str], Union[str, bool]]): Função para
        processar
        cada linha.
        max_workers (int): Número máximo de núcleos da CPU a serem usados.

    Returns:
        List[str]: Lista de linhas processadas.

    Raises:
        Exception: Se ocorrer um erro durante o processamento das linhas.
    """
    # Lista para armazenar as linhas processadas com seus índices originais
    indexed_processed_lines = []

    with Progress() as progress:
        task = progress.add_task(TEMPLATE_TASK_DESCRIPTION, total=len(lines))

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submete as linhas para processamento junto com seus índices
            future_to_index = {
                executor.submit(
                    process_line_func, line.rstrip("\n"), key
                ): index
                for index, line in enumerate(lines)
            }

            for future in as_completed(future_to_index):
                result = future.result()

                if result is False:
                    raise ValueError(TEMPLATE_INVALID_KEY)

                if not isinstance(result, str):
                    raise TypeError(TEMPLATE_TYPE_ERROR % {type(result)})

                # Adiciona o resultado junto com o índice original
                indexed_processed_lines.append(
                    (future_to_index[future], result)
                )

                # Atualiza a barra de progresso
                progress.update(task, advance=1)

    # Ordena os resultados processados pela ordem original das linhas
    indexed_processed_lines.sort(key=lambda x: x[0])

    # Retorna apenas as linhas processadas, na ordem correta
    return [line + "\n" for index, line in indexed_processed_lines]


def process_file(
    data_list: List[str],
    process_line_func: Callable[[str, str], Union[str, bool]],
) -> bool:
    """
    Processa o conteúdo de um arquivo linha por linha usando a função fornecida
    e salva o resultado em um novo arquivo.

    Args:
        data_list (List[str]): Lista contendo [arquivo, chave, novo_arquivo].
        process_line_func (Callable[[str, str], Union[str, bool]]): Função para
        processar
        cada linha do arquivo.

    Returns:
        bool: True se o processamento for bem-sucedido, False caso contrário.
    """
    file, key, new_file = data_list
    new_file_path = get_new_file_path(file, new_file)

    try:
        lines = read_file(file)
        max_workers = print_get_max_workers(lines)
        processed_lines = process_lines(
            lines, key, process_line_func, max_workers
        )

        if not processed_lines:
            return False

        write_file(new_file_path, processed_lines)
        print_and_record_log(
            (
                TEMPLATE_ENCRYPTED_FILE % new_file_path
                if process_line_func is encrypt
                else TEMPLATE_DECRYPTED_FILE % new_file_path
            ),
            "debug",
        )

        return True

    except FileNotFoundError:
        print_and_record_log(TEMPLATE_FILE_NOT_FOUND % file, "error")
        console.print(TEMPLATE_INFO_FILE)
        return False

    except ValueError as e:
        print_and_record_log(str(e), "error")
        return False

    except TypeError as e:
        print_and_record_log(str(e), "error")
        return False


def encrypt_file(data_list: List[str]) -> bool:
    """
    Criptografa o conteúdo de um arquivo linha por linha e salva o resultado
    em um novo arquivo.

    Args:
        data_list (List[str]): Lista contendo [arquivo, chave, novo_arquivo].

    Returns:
        bool: True se a criptografia for bem-sucedida, False caso contrário.
    """
    return process_file(data_list, encrypt)


def decrypt_file(data_list: List[str]) -> bool:
    """
    Descriptografa o conteúdo de um arquivo linha por linha e salva o resultado
    em um novo arquivo.

    Args:
        data_list (List[str]): Lista contendo [arquivo, chave, novo_arquivo].

    Returns:
        bool: True se a descriptografia for bem-sucedida, False caso contrário.
    """
    return process_file(data_list, decrypt)


def encrypt_message(message: str, key: str) -> None:
    """
    Criptografa os dados usando a chave fornecida e exibe o resultado.

    Args:
        message (str): Dados a serem criptografados.
        key (str): Chave para criptografia.
    """
    encrypted_message = encrypt(message, key)
    print_and_record_log(TEMPLATE_ENCRYPTED_MESSAGE, "debug")
    print_and_record_log(TEMPLATE_ENCRYPTED % encrypted_message, "debug")


def decrypt_message(message: str, key: str) -> bool:
    """
    Descriptografa os dados usando a chave fornecida. Se a descriptografia
    falhar, retorna False; caso contrário, exibe o resultado e retorna True.

    Args:
        message (str): Dados a serem descriptografados.
        key (str): Chave para descriptografia.

    Returns:
        bool: True se a descriptografia for bem-sucedida, False caso contrário.
    """
    try:
        decrypted_message = decrypt(message, key)
        if not decrypted_message:
            print_and_record_log(TEMPLATE_INVALID_KEY, "error")
            return False

        print_and_record_log(TEMPLATE_DECRYPTED_MESSAGE, "debug")
        print_and_record_log(TEMPLATE_DECRYPTED % decrypted_message, "debug")
        return True

    except InvalidEncryptedFormat as e:
        print_and_record_log(str(e), "error")
        return False


def process_keyfile_and_args(
    keyfile: Optional[str],
    message: Optional[str],
    file: Optional[str],
    template_key: str,
) -> str:
    """
    Obtém a chave de criptografia e valida os argumentos.

    Processa a chave de criptografia a partir de um arquivo ou solicita ao
    usuário, e valida se 'message' ou 'file' foram fornecidos corretamente.

    Args:
        keyfile (Optional[str]): Caminho para o arquivo com a chave. Se None,
        a chave será solicitada.
        message (Optional[str]): Dados para criptografar ou descriptografar.
        Usado se 'file' não for fornecido.
        file (Optional[str]): Caminho do arquivo a ser criptografado ou
        descriptografado. Usado se 'message' não for fornecido.
        template_key (str): Template para solicitar a chave ao usuário,
        se necessário.

    Returns:
        str: A chave de criptografia obtida.

    Raises:
        click.UsageError: Se ambos ou nenhum dos argumentos 'message' e 'file'
        forem fornecidos.
        SystemExit: Se o arquivo de chave não for encontrado, ou se a chave
        fornecida for inválida.
    """
    if message and file:
        raise click.UsageError(
            "Você deve fornecer apenas um dos argumentos: --message ou --file,"
            "não ambos."
        )
    if not message and not file:
        raise click.UsageError(
            "Você deve fornecer um dos argumentos: --message ou --file."
        )

    key: Optional[str] = None
    if keyfile:
        try:
            key = "".join(read_file(keyfile)).strip()
        except FileNotFoundError:
            print_and_record_log(TEMPLATE_FILE_NOT_FOUND % keyfile, "error")
            sys.exit(1)
    else:
        while not key or key.isspace():
            key = console.input(template_key, password=True).strip()
            if key.isspace():
                print_and_record_log(TEMPLATE_ERROR_EMPTY_FIELD, "error")

    if key is None:
        print_and_record_log(TEMPLATE_ERROR_EMPTY_FIELD, "error")
        sys.exit(1)

    return key


def interactive_mode() -> None:
    """
    Função principal do modo interativo que chama outras funções.
    """
    while True:
        file_message_option = print_request_menu(TEMPLATE_MENU_MESSAGE_FILE)
        match file_message_option:
            case 1:
                message_encrypt_decrypt_option = print_request_menu(
                    TEMPLATE_MENU_ENCRYPT_DECRYPT
                )
                match message_encrypt_decrypt_option:
                    case 1:
                        message, key = print_requesting_message(
                            TEMPLATE_ENCRYPT_MESSAGE, TEMPLATE_ENCRYPT_KEY
                        )
                        encrypt_message(message, key)
                    case 2:
                        message, key = print_requesting_message(
                            TEMPLATE_DECRYPT_MESSAGE, TEMPLATE_DECRYPT_KEY
                        )
                        decrypt_message(message, key)

            case 2:
                file_encrypt_decrypt_option = print_request_menu(
                    TEMPLATE_MENU_ENCRYPT_DECRYPT
                )
                match file_encrypt_decrypt_option:
                    case 1:
                        file_list = print_requesting_file(
                            TEMPLATE_ENCRYPT_FILE
                        )
                        encrypt_file(file_list)
                    case 2:
                        file_list = print_requesting_file(
                            TEMPLATE_DECRYPT_FILE
                        )
                        decrypt_file(file_list)

        if print_continue_or_leave(TEMPLATE_CONTINUE_LEAVE):
            break
