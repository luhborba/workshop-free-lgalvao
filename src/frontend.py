import streamlit as st

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