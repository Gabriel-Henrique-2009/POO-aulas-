import streamlit as st
from template.manterclienteui import ManterClienteUI
from template.manteratendimentoui import ManterAtendimentoUI
from template.manterservicoui import ManterServicoUI
from template.manterhorarioui import ManterHorarioUI
from template.manterprofissionalui import ManterProfissionalUI

class IndexUI:
    @staticmethod
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Profissionais", "Atendimentos"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()
        if op == "Atendimentos": ManterAtendimentoUI.main()

IndexUI.main()