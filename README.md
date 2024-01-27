# Projeto WorkShop Free - Luciano Galvão

## Leve em consideração que esta sendo usando Linux, com Pyenv e Poetry:
Você pode seguir esse guia que utilizei para utilização no WSL, assim você pode começar a partir da instalação do `PyEnv`: [GitHub que pode ser usado como guia](https://github.com/luhborba/Wsl-Pyenv-Poetry)

1. Clone o repositório:
```bash
git clone https://github.com/luhborba/workshop-free-lgalvao.git
cd workshop-free-lgalvao
```

2. Configure a versão correta do Python com `pyenv`
```bash
pyenv install 3.11.7
pyenv local 3.11.7
```

3. Ativando Poetry
```bash
poetry shell
```