"""Módulo que contém as configurações da ferramenta"""

import os

CURRENT_DIR = os.getcwd()

TEMPLATE_LOGO = """\n

███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗    ██████╗ ███████╗███████╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝    ██╔══██╗██╔════╝██╔════╝
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║       ██║  ██║█████╗  █████╗  
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║       ██║  ██║██╔══╝  ██╔══╝  
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║       ██████╔╝███████╗██║
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝       ╚═════╝ ╚══════╝╚═╝                                                                                    
"""

TEMPLATE_INFO = """
 [F] ⚙  FERRAMENTA: encryptdef
 [T] 🔐 TIPO: Encriptação/Decriptação
"""

TEMPLATE_MENU_DADOS_ARQUIVO = """\n
 [1] 🔠 DADOS.
 [2] 📄 ARQUIVOS.\n
"""

TEMPLATE_MENU_ENCRIPT_DECRIPT = """
 [E N C R I P T A Ç Ã O] / [D E C R I P T A Ç Ã O] ?

 [1] 🔒 ENCRIPTAÇÃO.
 [2] 🔓 DECRIPTAÇÃO."""

TEMPLATE_DADOS_ENCRIPT = """
 🔒 [E N C R I P T A Ç Ã O]

 [!] 🔠 DEGITE A INFORAMAÇÃO QUE DESEJA ENCRYPTA"""

TEMPLATE_KEY_ENCRIPT = " [!] 🔑 DEGITE A KEY PARA ENCRIPTAÇÃO"

TEMPLATE_DADOS_DECRIPT = """
 🔓 [D E C R I P T A Ç Ã O]

 [!] 🔠 DEGITE O TEXTO ENCRIPTADO"""

TEMPLATE_KEY_DECRIPT = " [!] 🔑 DEGITE A KEY DA ENCRIPTAÇÃO"

TEMPLATE_ARQUIVO_ENCRIPT = """\
 [file] 📄 DIGITE O NOME DO ARQUIVO QUE DESEJA ENCRIPTAR
 [key] 🔑 DEGITE A KEY PARA ENCRIPTAÇÃO
 [new-file] 🔒📄 DIGITE O NOME PARA O NOVO ARQUIVO ECRIPTADO"""

TEMPLATE_ARQUIVO_DECRIPT = """\
 [file] 🔒📄 DIGITE O NOME DO ARQUIVO ENCRIPTADO
 [key] 🔑 DEGITE A KEY DA ENCRIPTAÇÃO
 [new-file] 📄 DIGITE O NOME PARA O NOVO ARQUIVO DECRIPTADO"""

TEMPLATE_CONTINUAR_SAIR = """
 [?] PRESSIONE ENTER PARA CONTINUAR, OU QUALQUER TECLA PARA SAIR:"""
