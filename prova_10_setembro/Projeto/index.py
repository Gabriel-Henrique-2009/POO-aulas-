import streamlit as st
from template.manterclienteui import ManterClienteUI
from template.manterconvenioui import ManterConvenioUI

class IndexUI:
    @staticmethod
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Convenio"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Convenio": ManterConvenioUI.main()

IndexUI.main()