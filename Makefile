.PHONY: install virtualenv lint fmt clean build publish-test publish

# Variáveis para simplificar comandos
VENV_BIN=.venv/bin
PYTHON=$(VENV_BIN)/python
PIP=$(PYTHON) -m pip

install: ## Instalar dependências para o ambiente de desenvolvimento
	@echo "Instalando dependências para o ambiente de desenvolvimento..."
	@$(PIP) install -e '.[dev]'

virtualenv: ## Criar ambiente virtual
	@echo "Criando ambiente virtual..."
	@python -m venv .venv

lint: ## Executar linters
	@echo "Executando linters..."
	@$(VENV_BIN)/mypy encryptdef
	@$(VENV_BIN)/pflake8

fmt: ## Formatar código
	@echo "Formatando código..."
	@$(VENV_BIN)/isort encryptdef
	@$(VENV_BIN)/black encryptdef

clean: ## Limpar arquivos desnecessários
	@echo "Limpando arquivos desnecessários..."
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

build: clean ## Construir pacotes
	@echo "Construindo pacotes..."
	@$(PYTHON) setup.py sdist bdist_wheel

publish-test: build ## Publicar no TestPyPI
	@echo "Publicando no TestPyPI..."
	@$(VENV_BIN)/twine upload --repository testpypi dist/*

publish: build ## Publicar no PyPI
	@echo "Publicando no PyPI..."
	@$(VENV_BIN)/twine upload dist/*
