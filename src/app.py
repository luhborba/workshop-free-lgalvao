import streamlit as st

st.set_page_config(
    page_title="Validador Excel", 
    page_icon=":snake:"
)

st.title("Sistema de Envio de informações para o Domino PMJP-SMS")
st.header("Neste sistema você vai enviar as informações dos servidores(as) do seu setor, para que seja possível realizar a inserção no dominio")

arquivo = st.file_uploader("Carregue seu arquivo Excel aqui", type=["xlsx"])

if arquivo is not None:
    st.success("A estrutura do arquivo está Correta")