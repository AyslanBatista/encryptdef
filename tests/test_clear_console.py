""" Modulo para testar a função clear_console em utils.py"""

from unittest import mock

from encryptdef.utils import clear_console


@mock.patch("subprocess.run")  # Substitui subprocess.run por um mock
def test_clear_console_posix(mock_run):
    """Test function clear_console"""
    with mock.patch("os.name", "posix"):
        clear_console()

    # Verifica se subprocess.run foi chamado com ["cls"] e check=False
    mock_run.assert_called_once_with(["clear"], check=False)


@mock.patch("subprocess.run")
def test_clear_console_nt(mock_run):
    """Test function clear_console"""
    with mock.patch("os.name", "nt"):
        clear_console()
    mock_run.assert_called_once_with(["cls"], shell=True, check=False)
