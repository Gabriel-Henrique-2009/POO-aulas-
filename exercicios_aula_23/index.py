import streamlit as st
from template.manterclienteui import ManterClienteUI
from template.manteratendimentoui import ManterAtendimentoUI

class IndexUI:
    @staticmethod
    def main():
        st.sidebar.title("Menu")
        op = st.sidebar.selectbox("Selecione a opção", ["Manter Clientes", "Manter Atendimentos"])
        
        if op == "Manter Clientes":
            ManterClienteUI.main()
        if op == "Manter Atendimentos":
            ManterAtendimentoUI.main()