"""Módulo de configurações dos testes"""

import pytest

MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):  # injeção de dependencias
    """Cada teste tem um diretorio no /tmp"""
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield  # protocolo de generators
