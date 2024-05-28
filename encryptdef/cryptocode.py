"""Modulo Referente a biblioteca Cryptocode:
https://github.com/gdavid7/cryptocode
"""

import hashlib
from base64 import b64decode, b64encode
from typing import Union

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

from encryptdef.template import TEMPLATE_ERROR_INVALID_ENCRYPTED_FORMAT


class InvalidEncryptedFormat(Exception):
    """Formato de string criptografada inválido"""


def encrypt(message: str, password: str) -> str:
    """
    Criptografa uma mensagem usando AES GCM com uma chave derivada por Scrypt.

    Args:
        message (str): A mensagem que será criptografada.
        password (str): A senha usada para derivar a chave de criptografia.

    Returns:
        str: A mensagem criptografada contendo texto cifrado, salt,
        nonce e tag.
    """
    # Gera um salt aleatório
    salt = get_random_bytes(AES.block_size)

    # Usa Scrypt para derivar a chave privada a partir da senha
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32
    )

    # Cria a configuração do cifrador em modo GCM
    cipher = AES.new(private_key, AES.MODE_GCM)
    cipher_text, tag = cipher.encrypt_and_digest(message.encode("utf-8"))

    # Codifica em base64 e retorna uma string formatada
    encrypted_parts = {
        "cipher_text": b64encode(cipher_text).decode("utf-8"),
        "salt": b64encode(salt).decode("utf-8"),
        "nonce": b64encode(cipher.nonce).decode("utf-8"),
        "tag": b64encode(tag).decode("utf-8"),
    }
    return "*".join(encrypted_parts.values())


def decrypt(enc_string: str, password: str) -> Union[str, bool]:
    """
    Descriptografa uma mensagem criptografada usando AES GCM com uma chave
    derivada por Scrypt.

    Args:
        enc_string (str): A mensagem criptografada.
        password (str): A senha usada para derivar a chave de descriptografia.

    Returns:
        str: A mensagem descriptografada ou False se ocorrer um erro.
    """
    enc_parts = enc_string.split("*")
    if len(enc_parts) != 4:
        raise InvalidEncryptedFormat(TEMPLATE_ERROR_INVALID_ENCRYPTED_FORMAT)

    try:
        # Decodifica as partes criptografadas de base64
        cipher_text, salt, nonce, tag = map(b64decode, enc_parts)

        # Gera a chave privada a partir da senha e do salt
        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32
        )

        # Cria a configuração do cifrador em modo GCM
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

        # Descriptografa o texto cifrado e verifica a tag
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)
        return decrypted.decode("utf-8")
    except ValueError:
        return False
