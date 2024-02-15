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

def main():
    ui = ExcelValidadorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        result, error = process_excel(upload_file)
        ui.display_result(result, error)

if __name__ == "__main__":
    main()
```

### Frontend.py

Este arquivo é para configuração do frontend da página, assim deixando de forma separada do `app.py`.
```python
# Importando Streamlit
import streamlit as st

# Criando Classe para FrontEnd, para melhor organização e uso
class ExcelValidadorUI:

    def __init__(self):
        self.set_page_config()

    # Criando função para configuração das páginas
    def set_page_config(self):
        st.set_page_config(
            page_title="Validador de Planilha",
            page_icon=":snake:"
        )
    
    # Criando função para Header da página
    def display_header(self):
        st.title("Insira sua planilha para realizar a validação!")

    # Criando função para o componente de file uploader
    def upload_file(self):
        return st.file_uploader("Carregue sua planilha", type=["xlsx"])

    # Criando função especifica para mostragem de error
    def display_result(self, result, error):
        if error:
            st.error(f"Erro na validação: {error}")
        else:
            st.success("A planilha está correta")
```

### Backend.py

Este arquivo é para configuração do backend da página, fazendo toda validação dos arquivos 'xlsx'.
```python
# Importando Pandas
import pandas as pd
# Importando classe de Vendas do arquivo de contratos.py
from contrato import Vendas

# Criando função de validação do arquivo excel
def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        # Verificando se há colunas extras
        extras_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extras_cols:
            return False, f"Existem mais colunas que o necessário: {', '.join(extras_cols)}"

        # Validar cada linha com o contrato
        for index, row in df.iterrows():
            try:
                _ = Vendas(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Erro na linha {index + 2}: {e}")
            
        return True, None
    except ValueError as ve:
        return False, str(ve)
    except Exception as e:
        return False, f"Erro Inesperado: {str(e)}"
```