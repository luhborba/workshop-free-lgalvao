# Documentação de Projeto Data Quality
Documentação produzida utilizando o MkDocs, se deseja saber mais acesse [mkdocs.org](https://www.mkdocs.org).

Este projeto de Data Quality foi desenvolvido após Workshop do [Luciano Vasconcelos Filho](https://www.linkedin.com/in/lucianovasconcelosf/).

**GitHub do Projeto:** [Deputados-LuhBorba](https://github.com/luhborba/projeto_camara_deputados)<br>
**Documentação do Projeto:**  [Documentacao](https://luhborba.github.io/workshop-free-lgalvao/)<br>



## Stack do Projeto

- python
- streamlit
- selenium
- pytest
- taskipy
- pydantic
- openpyxl
- mkdocs
- mkdocstrings
- mkdocs-material

## Proposta do Projeto

O projeto tem como objetivo realizar um processo de validação de estrutura de uma planilha no Excel, considerando que hoje no mundo corporativo esta é uma ferramenta amplamente usada, assim buscando definições padrões para envios de dados considerando um estrutura de contrato pre-definida.

A abordagem utilizada é criar um App no Streamlit que realize todo processo de validação, ferramenta com criação de testes, buscando assim um qualidade no dado enviado.

## Estrutura do Projeto

O projeto está basicamente dividido em 4 (quatro) arquivos, todos eles dentro da pasta `src`.

- app.py
- backend.py
- contrato.py
- frontend.py

### Contrato de Schema

Este aqui é específico para o contrato de dados do case de vendas, trabalhado neste projeto.

::: src.contrato.Vendas

### App.py

Aqui é particularmente faço a união entre o frontend e backend, carregando assim todas as validações propostas no backend e trazendo todos os visuais carregados no frontend.
```python
# Importando Classe do Arquivo FrontEnd
from frontend import ExcelValidadorUI
# Importando Função do Arquivo BackEnd
from backend import process_excel
```
Função especifica para interligar frontend e backend, de forma que o projeto tenha uma organização e padronização.

::: src.app.main

### Frontend.py

Este arquivo é para configuração do frontend da página, assim deixando de forma separada do `app.py`.

```python
# Importando Streamlit
import streamlit as st
```

::: src.frontend.ExcelValidadorUI

### Backend.py

Este arquivo é para configuração do backend da página, fazendo toda validação dos arquivos 'xlsx'.
```python
# Importando Pandas
import pandas as pd
# Importando classe de Vendas do arquivo de contratos.py
from contrato import Vendas
```

::: src.backend.process_excel