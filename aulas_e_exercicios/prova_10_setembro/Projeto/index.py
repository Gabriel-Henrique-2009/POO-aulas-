import streamlit as st
from aulas_e_exercicios.prova_10_setembro.Projeto.template.manterclienteui import ManterClienteUI
from aulas_e_exercicios.prova_10_setembro.Projeto.template.manterconvenioui import ManterConvenioUI

class IndexUI:
    @staticmethod
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Convenio"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Convenio": ManterConvenioUI.main()

IndexUI.main()