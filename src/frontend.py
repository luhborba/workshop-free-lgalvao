import streamlit as st

class ExcelValidadorUI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Validador de Planilha",
            page_icon=":snake:"
        )
    
    def display_header(self):
        st.title("Insira sua planilha para realizar a validação!")

    def upload_file(self):
        return st.file_uploader("Carregue sua planilha", type=["xlsx"])

    def display_result(self, result, error):
        if error:
            st.error(f"Erro na validação: {error}")
        else:
            st.success("A planilha está correta")