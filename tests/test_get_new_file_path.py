""" Modulo para testar a função get_new_file_path"""

import os

from encryptdef.core import get_new_file_path


def test_get_new_file_path_positive():
    """Test function get_new_file_path"""
    file = "file_test.txt"
    new_file = "encrypt_file_test.txt"
    current_dir = os.getcwd()
    file_path = get_new_file_path(file, new_file, current_dir)

    assert file_path == os.path.join(os.getcwd(), new_file)


def test_get_new_file_path_positive_exact_file_path():
    """Test function get_new_file_path"""
    file = "file_test.txt"
    new_file = "encrypt_file_test.txt"

    current_dir = os.getcwd()
    new_file_path = os.path.join(current_dir, new_file)
    file_path_get = get_new_file_path(file, new_file_path, current_dir)

    assert file_path_get == new_file_path
