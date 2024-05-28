"""Módulo que contém as configurações do logging"""

import logging
import os
from logging import handlers
from typing import Optional, Union

from encryptdef.settings import console

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()

log_instance = logging.getLogger("encryptdef")  # Criando stancia de log

# Objeto de formatação de como será exibido os logs
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    "l:%(lineno)d f:%(filename)s: %(message)s"
)


# Controle de logs do usuario pela variavel de ambiente
# export LOG_LEVEL=debug        log level em formato DEV para exibir os debug
def get_logger(
    logfile: Union[str, os.PathLike[str]] = "encryptdef.log"
) -> logging.Logger:
    """Returns a configured logger."""

    # Responsavel por salvar os log em arquivo
    fh = handlers.RotatingFileHandler(
        # Nome do arquivo
        logfile,
        # maxBytes = 10**6 Tamanho maximo do arquivo, depois cria outro arquivo
        maxBytes=10**6,
        # backupCount=10 >> Quantidade de arquivos para manter no backup
        backupCount=10,
    )

    fh.setLevel(LOG_LEVEL)  # Nivel que será exibido

    fh.setFormatter(fmt)  # Adicionando a formtação ao Handler que foi criado
    log_instance.addHandler(fh)  # Por fim adiciona o Handler ao log
    log_instance.setLevel(LOG_LEVEL)  # export LOG_LEVEL=debug
    return log_instance


log = get_logger()


def print_and_record_log(msg: str, style: Optional[str] = None) -> None:
    """
    Logs a message and prints it to the console with a specified style.

    Args:
        msg (str): The message to be logged and printed.
        style (Optional[str]): The style of the log message. Possible values
        are "critical", "error", "warning", "info", and "debug".
        Defaults to None.

    Returns:
        None
    """

    match style:
        case "critical":
            log.critical(msg.strip())
            console.print(msg, style="critical")
        case "error":
            log.error(msg.strip())
            console.print(msg, style="error")
        case "warning":
            log.warning(msg.strip())
            console.print(msg, style="warning")
        case "info":
            log.info(msg.strip())
            console.print(msg, style="info")
        case "debug":
            log.debug(msg.strip())
            console.print(msg, style="debug")
        case _:
            log.info(msg.strip())
            console.print(msg)
